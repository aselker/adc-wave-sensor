
#include <Servo.h>
Servo myservo;
String tempPos;
float tempPosNum;
int pos;

void setup() {
  // put your setup code here, to run once:
  myservo.attach(9);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    tempPos = Serial.readStringUntil('\n');
    //while (true) {
      //char tmp = Serial.read();
      //if (tmp == '\n') break;
      //tempPos += tmp;
    //}
    Serial.println(tempPos);
    tempPosNum = tempPos.toFloat();
    pos = tempPosNum*(30) + 55;
    if (pos > 85) {
      pos = 85;
    }
    if (pos < 55) {
      pos = 55;
    }
    myservo.write(pos); 
    Serial.println(pos);
    tempPos = "";
  }
}
