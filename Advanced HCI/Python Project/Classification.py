import pickle
import numpy as np
import os
import sqlite3
from keras.models import load_model
import cv2
import random
#import pyttsx3



model = load_model('finalmodel2.h5')


image_x, image_y = (50,50)

def keras_process_image(img):
	img = cv2.resize(img, (image_x, image_y))
	img = np.array(img, dtype=np.float32)
	img = np.reshape(img, (1, image_x, image_y, 1))
	return img

def keras_predict(model, image):
	processed = keras_process_image(image)
	pred_probab = model.predict(processed)[0]
	pred_class = list(pred_probab).index(max(pred_probab))

	print("predicted class")
	print(pred_class)


	return max(pred_probab), pred_class

def get_pred_text_from_db(pred_class):
	conn = sqlite3.connect("gesture_db.db")
	cmd = "SELECT g_name FROM gesture WHERE g_id="+str(pred_class)
	cursor = conn.execute(cmd)
	for row in cursor:
		return row[0]




def recognize():
	#engine = pyttsx3.init()
	global prediction
	cam = cv2.VideoCapture(1)
	if cam.read()[0] == False:
		cam = cv2.VideoCapture(0)

	x, y, w, h = 300, 100, 300, 300
	while True:
		text = ""
		pred_class=0

		img = cam.read()[1]
		img = cv2.flip(img, 1)
		ret,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
		thresh=cv2.GaussianBlur(thresh,(5,5),0)
		thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
		thresh = thresh[y:y+h, x:x+w]
		contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]

		if len(contours) > 0:
			contour = max(contours, key = cv2.contourArea)
			#print(cv2.contourArea(contour))
			if cv2.contourArea(contour) > 10000:
				x1, y1, w1, h1 = cv2.boundingRect(contour)
				save_img = thresh[y1:y1+h1, x1:x1+w1]

				if w1 > h1:
					save_img = cv2.copyMakeBorder(save_img, int((w1-h1)/2) , int((w1-h1)/2) , 0, 0, cv2.BORDER_CONSTANT, (0, 0, 0))
				elif h1 > w1:
					save_img = cv2.copyMakeBorder(save_img, 0, 0, int((h1-w1)/2) , int((h1-w1)/2) , cv2.BORDER_CONSTANT, (0, 0, 0))

				pred_probab, pred_class = keras_predict(model, save_img)
				print(pred_class, pred_probab)
				if pred_probab*100 > 99:
					text = get_pred_text_from_db(pred_class+1)
					print(text)
		blackboard = np.zeros((480, 640, 3), dtype=np.uint8)
		blackboard2=np.zeros((480,640,3),dtype=np.uint8)
		cv2.putText(blackboard, text, (30, 200), cv2.FONT_HERSHEY_TRIPLEX, 1.3, (255, 255, 255))
		
		if text=='Na':
			cv2.putText(blackboard2,'this is Na',(30,250),cv2.FONT_HERSHEY_TRIPLEX,1.3,(255,0,0))
		cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
		res = np.hstack((img, blackboard))
		res2=np.vstack((blackboard,blackboard2))
		cv2.imshow("Recognizing gesture", res2)
		cv2.imshow("thresh", thresh)

		#if text!="":
		#	if text=="Na":
		#		engine.say("Na")
		#		engine.runAndWait()
		#	elif text=="Ni":
		#		engine.say("Ni")
		#		engine.runAndWait()
		#	elif text=="Nu":
		#		engine.say("Nu")
		#		engine.runAndWait()
		#	elif text=="Ne":
		#		engine.say("Ne")
		#		engine.runAndWait()
		#	elif text=="No":
		#		engine.say("No")
		#		engine.runAndWait()
		#	else:
		#		continue




		if cv2.waitKey(1) == ord('q'):
			break

keras_predict(model, np.zeros((50, 50), dtype=np.uint8))
recognize()
