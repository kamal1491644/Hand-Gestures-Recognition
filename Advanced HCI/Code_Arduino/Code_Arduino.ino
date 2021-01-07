
const int FLEX_PIN_1=A0;
const int FLEX_PIN_2=A1;
const int FLEX_PIN_3=A2;
const int FLEX_PIN_4=A3;
const int FLEX_PIN_5=A4;

const float VCC = 4.98; 
const float R_DIV = 47500.0;



const float STRAIGHT_RESISTANCE = 37300.0; 
const float BEND_RESISTANCE = 90000.0; 



void setup() {
  Serial.begin(9600);
  pinMode(FLEX_PIN_1, INPUT);
  pinMode(FLEX_PIN_2, INPUT);
  pinMode(FLEX_PIN_3, INPUT);
  pinMode(FLEX_PIN_4, INPUT);
  pinMode(FLEX_PIN_5, INPUT);  

}

void loop() {
  int flexADC_1 = analogRead(FLEX_PIN_1);
  float flexV_1 = flexADC_1 * VCC / 1023.0;
  float flexR_1 = R_DIV * (VCC / flexV_1 - 1.0);
  Serial.println("Resistance 1: " + String(flexR_1) + " ohms");
  float angle_1 = map(flexR_1, STRAIGHT_RESISTANCE, BEND_RESISTANCE,0,90.0);
  Serial.println("Bend1 1: " + String(angle_1) + " degrees");





  int flexADC_2 = analogRead(FLEX_PIN_2);
  float flexV_2 = flexADC_2 * VCC / 1023.0;
  float flexR_2 = R_DIV * (VCC / flexV_2 - 1.0);
  Serial.println("Resistance 2: " + String(flexR_2) + " ohms");
  float angle_2 = map(flexR_2, STRAIGHT_RESISTANCE, BEND_RESISTANCE,0,90.0);
  Serial.println("Bend1 2: " + String(angle_2) + " degrees");



  int flexADC_3 = analogRead(FLEX_PIN_3);
  float flexV_3 = flexADC_3 * VCC / 1023.0;
  float flexR_3 = R_DIV * (VCC / flexV_3 - 1.0);
  Serial.println("Resistance 3: " + String(flexR_3) + " ohms");
  float angle_3 = map(flexR_3, STRAIGHT_RESISTANCE, BEND_RESISTANCE,0, 90.0);
  Serial.println("Bend1 3: " + String(angle_3) + " degrees");



  int flexADC_4 = analogRead(FLEX_PIN_4);
  float flexV_4 = flexADC_4 * VCC / 1023.0;
  float flexR_4 = R_DIV * (VCC / flexV_4 - 1.0);
  Serial.println("Resistance 4: " + String(flexR_4) + " ohms");
  float angle_4 = map(flexR_4, STRAIGHT_RESISTANCE, BEND_RESISTANCE,0, 90.0);
  Serial.println("Bend1 4: " + String(angle_4) + " degrees");



  int flexADC_5 = analogRead(FLEX_PIN_5);
  float flexV_5 = flexADC_5 * VCC / 1023.0;
  float flexR_5 = R_DIV * (VCC / flexV_5 - 1.0);
  Serial.println("Resistance 5: " + String(flexR_5) + " ohms");
  float angle_5 = map(flexR_5, STRAIGHT_RESISTANCE, BEND_RESISTANCE,0, 90.0);
  Serial.println("Bend1 5: " + String(angle_5) + " degrees");
  Serial.println("\n");


  if (angle_1>-5 && angle_2>-5 && angle_2<19 && angle_3>-5 && angle_3<19 && angle_4>-5 && angle_5>-5)
  {
    Serial.println("Na");  
  }

  else if(angle_1>-5 && angle_2<-5 && angle_3<-5 && angle_4>-5 && angle_5>-5)
  {
    Serial.println("Ni");
  }
  else if(angle_1>-5 && angle_2>-5 && angle_2<19 && angle_3>-5 && angle_4>-5 && angle_5>-5)
  {
    Serial.println("Nu");  
  }
  else if(angle_1<-5 && angle_2<-5 && angle_3<-5 && angle_4<-5 && angle_5<-5)
  {
    Serial.println("Ne");
  }
  else if (angle_1>-5 && angle_2<-5 && angle_3>-5 && angle_4>-5 && angle_5>-5)
  {
    Serial.println("No");  
  }
  else
  {
    Serial.println("None");
  }

}
