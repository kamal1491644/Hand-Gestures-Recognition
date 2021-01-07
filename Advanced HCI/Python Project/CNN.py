import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dense
from keras import optimizers
from keras.layers import Flatten, Dropout
from keras.utils.np_utils import to_categorical
from keras.layers.convolutional import Conv2D, MaxPooling2D
import random
import pickle
import pandas as pd
import cv2
from google.colab import files
from keras.callbacks import LearningRateScheduler, ModelCheckpoint
np.random.seed(0)


with open("signlanguage/train_images", "rb") as f:
  train_images = np.array(pickle.load(f))
with open("signlanguage/train_labels", "rb") as f:
  train_labels = np.array(pickle.load(f), dtype=np.int32)

with open("signlanguage/val_images", "rb") as f:
  val_images = np.array(pickle.load(f))
with open("signlanguage/val_labels", "rb") as f:
  val_labels = np.array(pickle.load(f), dtype=np.int32)

with open("signlanguage/test_images", "rb") as f:
  test_images = np.array(pickle.load(f))
with open("signlanguage/test_labels", "rb") as f:
  test_labels = np.array(pickle.load(f), dtype=np.int32)

print(train_images.shape)
print(test_images.shape)
print(val_images.shape)

plt.imshow(train_images[100])
plt.axis("off")
print(train_images[1000].shape)
print(train_labels[1000])
print(train_images.shape)
train_images = train_images.reshape(9600, 50, 50, 1)
test_images = test_images.reshape(1200, 50, 50, 1)
val_images = val_images.reshape(1200, 50, 50, 1)
train_labels=train_labels-1
test_labels=test_labels-1
val_labels=val_labels-1
train_labels = to_categorical(train_labels, 5)
test_labels = to_categorical(test_labels, 5)
val_labels = to_categorical(val_labels, 5)

def model_CNN():
  model = Sequential()
  model.add(Conv2D(16, (2, 2), input_shape=(50, 50, 1), activation='relu'))

  model.add(MaxPooling2D(pool_size=(2, 2),strides=(2,2),padding='same'))

  model.add(Conv2D(32, (5, 5), activation='relu'))

  model.add(MaxPooling2D(pool_size=(5, 5),strides=(5,5),padding='same'))

  model.add(Conv2D(64, (5, 5), activation='relu'))

  model.add(Flatten())
  model.add(Dense(128, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(5, activation='softmax'))
  adam=Adam(lr=0.001)
  model.compile(loss='categorical_crossentropy',optimizer=adam, metrics=['accuracy'])
  return model
model = model_CNN()
print(model.summary())

history=model.fit(train_images,train_labels,validation_data=(val_images,val_labels),batch_size=500,epochs=10)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.legend(['training','test'])
plt.title('Accuracy')
plt.xlabel('epoch')


plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Loss')
plt.xlabel('epoch')

score = model.evaluate(test_images, test_labels, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])
model.save('finalmodel2.h5')
files.download('finalmodel2.h5')
