#include <Arduino.h>
#include <Servo.h>

Servo myServo;

int angle = 120;

void setup()
{
  myServo.attach(9);

  myServo.write(100);

  Serial.begin(9600);
}

void loop()
{

  // Check if serial data is available
  if (Serial.available() > 0)
  {
    // Read the incoming string until newline character
    String command = Serial.readStringUntil('\n');

    // Remove any whitespace/carriage returns
    command.trim();
    command.toLowerCase();

    // Compare command and set angle
    if (command == "locked")
    {
      angle = 178;
      Serial.println("Moving to locked position (180 degrees)");
    }
    else if (command == "unlocked")
    {
      angle = 10;
      Serial.println("Moving to unlocked position (30 degrees)");
    }
  }

  myServo.write(angle);
  delay(15);
}