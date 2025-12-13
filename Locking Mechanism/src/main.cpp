#include <Arduino.h> 
#include <Servo.h>

Servo myServo;

int angle = 120;

void setup() {
myServo.attach(9);

Serial.begin(9600);
}

void loop() {

  // Check if serial data is available
  if (Serial.available() > 0) {
    // Read the incoming string until newline character
    String command = Serial.readStringUntil('\n');
    
    // Remove any whitespace/carriage returns
    command.trim();
    
    // TODO: Next step - compare command and set angle
  }


myServo.write(angle);
delay(15);
}