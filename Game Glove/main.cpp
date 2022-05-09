#include <Arduino.h>
int buttons[]={2,3,4,5};
int states[]={};

void setup() {
  // put your setup code here, to run once:
  for(int i=0;i<4;i++){
    pinMode(buttons[i],INPUT_PULLUP);
  }
  Serial.begin(9600); 
}

void loop() {
  // put your main code here, to run repeatedly:
  String total;
  for(int i=0;i<4;i++){
    states[i]=digitalRead(buttons[i]);
    if(states[i]==LOW){
      total+='1';
    }
    else{
      total+='0';
    }
  }
  // for(int i=0;i<4;i++){
  //   Serial.println(total[i]);
  delay(50);
  Serial.println(total);
}