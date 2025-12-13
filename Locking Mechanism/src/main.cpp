#include <Arduino.h> 
#include <Servo.h>

Servo myServo;

int angle = 120;

void setup() {
myServo.attach(9);

Serial.begin(9600);
}

void loop() {
myServo.write(angle);
delay(15);
}