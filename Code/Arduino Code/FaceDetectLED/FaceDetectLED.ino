#include <cvzone.h>

SerialData serialData(2,1); //(numOfValsRec,digitsPerValRec)
int valArr[2];
int red = 12;
int green = 13;

void setup() {
  serialData.begin();
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
}

void loop() {
  serialData.Get(valArr);
  
  digitalWrite(red, valArr[0]);
  digitalWrite(green, valArr[1]);
  delay(1000);
}
