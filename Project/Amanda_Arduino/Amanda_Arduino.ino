#include <Servo.h>

Servo m1;
Servo m2;
Servo m3;
Servo m4;
Servo m5;

String valor;

void setup() {
  Serial.begin(9600);
  delay(20);  
  m1.attach(1);
  m2.attach(2);
  m3.attach(3);
  m4.attach(4);
  m5.attach(5);
  inicial();
}

void loop() {
  if (Serial.available()){
    valor = Serial.readString();
    if (valor=="UNO" or valor == "1"){
      mov_uno();
      delay(2000);
      inicial();
    }
    if (valor=="DOS" or valor == "2"){
      mov_dos();
      delay(30);
      inicial();
    }
    if (valor=="TRES" or valor == "3"){
      mov_tres();
      delay(30);
      inicial();
    }
    if (valor=="CUATRO" or valor == "4"){
      mov_cuatro();
      delay(30);
      inicial();
    }
    if (valor=="CINCO" or valor == "5"){
      mov_cero();
      delay(1000);
      mov_cinco();
      delay(30);
      inicial();
    }
    if (valor=="SEIS" or valor == "6"){
      mov_seis();
      delay(30);
      inicial();
    }
    if (valor=="SIETE" or valor == "7"){
      mov_siete();
      delay(30);
      inicial();
    }
    if (valor=="OCHO" or valor == "8"){
      mov_ocho();
      delay(30);
      inicial();
    }
    if (valor=="NUEVE" or valor == "9"){
      mov_nueve();
      delay(30);
      inicial();
    }                      
  }
}
void inicial() {
  m1.write(0);
  m2.write(0);
  m3.write(0);
  m4.write(0);
  m5.write(0);
}
void mov_cero(){
  m1.write(150);
  delay(100);
  m2.write(150);
  delay(100);
  m3.write(150);
  delay(100);
  m4.write(150);
  delay(100);
  m5.write(100);
  delay(100);
}
void mov_uno() {
  m1.write(0);
  delay(100);
  m2.write(150);
  delay(100);
  m3.write(150);
  delay(100);
  m4.write(150);
  delay(100);
  m5.write(100);
  delay(100);
}
void mov_dos() {
  m1.write(0);
  m2.write(0);
  delay(100);
  m3.write(150);
  delay(100);
  m4.write(150);
  delay(100);
  m5.write(100);
  delay(100);
}
void mov_tres() {
  m1.write(0);
  m2.write(0);
  m3.write(0);
  m4.write(0);
  delay(100);
  m5.write(100);
  delay(100);
}
void mov_cuatro() {
  m1.write(0);
  m2.write(0);
  m3.write(0);
  m4.write(0);
  delay(100);
  m5.write(100);
  delay(100);
}
void mov_cinco() {
  m1.write(0);
  m2.write(0);
  m3.write(0);
  m4.write(0);
  m5.write(0);
  delay(100);
}
void mov_seis() {
  m1.write(180);
  m2.write(180);
  m3.write(180);
  m4.write(180);
  m5.write(0);
}
void mov_siete() {
  m1.write(180);
  m2.write(180);
  m3.write(180);
  m4.write(0);
  m5.write(0);
}
void mov_ocho() {
  m1.write(180);
  m2.write(0);
  m3.write(0);
  m4.write(0);
  m5.write(0);
}
void mov_nueve() {
  m1.write(180);
  m2.write(0);
  m3.write(0);
  m4.write(0);
  m5.write(0);
}
