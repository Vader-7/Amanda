#include <Servo.h>

// Define constants for the servo pin numbers
const int SERVO_1_PIN = 1;
const int SERVO_2_PIN = 2;
const int SERVO_3_PIN = 3;
const int SERVO_4_PIN = 4;
const int SERVO_5_PIN = 5;

// Create servo objects
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

String valor;

void setup() {
  Serial.begin(9600);
  delay(20);
  servo1.attach(SERVO_1_PIN);
  servo2.attach(SERVO_2_PIN);
  servo3.attach(SERVO_3_PIN);
  servo4.attach(SERVO_4_PIN);
  servo5.attach(SERVO_5_PIN);
  moveToInitialPosition();
}

void loop() {
  if (Serial.available()){
    valor = Serial.readString();
    // Handle the different commands
    switch (valor) {
      case "UNO":
      case "1":
        moveOne();
        delay(2000);
        moveToInitialPosition();
        break;
      case "DOS":
      case "2":
        moveTwo();
        delay(30);
        moveToInitialPosition();
        break;
      case "TRES":
      case "3":
        moveThree();
        delay(30);
        moveToInitialPosition();
        break;
      case "CUATRO":
      case "4":
        moveFour();
        delay(30);
        moveToInitialPosition();
        break;
      case "CINCO":
      case "5":
        moveToInitialPosition();
        delay(1000);
        moveFive();
        delay(30);
        moveToInitialPosition();
        break;
      case "SEIS":
      case "6":
        moveSix();
        delay(30);
        moveToInitialPosition();
        break;
      case "SIETE":
      case "7":
        moveSeven();
        delay(30);
        moveToInitialPosition();
        break;
      case "OCHO":
      case "8":
        moveEight();
        delay(30);
        moveToInitialPosition();
        break;
      case "NUEVE":
      case "9":
        moveNine();
        delay(30);
        moveToInitialPosition();
        break;
      default:
        // Handle unrecognized input
        break;
    }
  }
}

// Define functions for each movement
void moveToInitialPosition() {
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  servo5.write(0);
}

void moveOne() {
  servo1.write(0);
  delay(100);
  servo2.write(150);
  delay(100);
  servo3.write(150);
  delay(100);
  servo4.write(150);
  delay(100);
  servo5.write(100);
  delay(100);
}

void moveTwo() {
  servo1.write(0);
  servo2.write(0);
  delay(100);
  servo3.write(150);
  delay(100);
  servo4.write(150);
  delay(100);
  servo5.write(100);
  delay(100);
}

void moveThree() {
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  delay(100);
  servo5.write(100);
  delay(100);
}

void moveFour() {
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  delay(100);
  servo5.write(100);
  delay(100);
}

void moveFive() {
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  delay(100);
  servo5.write(100);
  delay(100);
}

void moveSix() {
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  delay(100);
  servo5.write(100);
  delay(100);
}

void moveSeven() {
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  delay(100);
  servo5.write(100);
  delay(100);
}

void moveEight() {
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  delay(100);
  servo5.write(100);
  delay(100);
}

void moveNine() {
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  delay(100);
  servo5.write(100);
  delay(100);
}

// Define functions for each movement
void moveToInitialPosition() {
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  servo5.write(0);
}

