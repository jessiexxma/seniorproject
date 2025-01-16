#include "Wire.h"
#include "I2Cdev.h"
#include "MPU6050.h"

MPU6050 mpu;
int16_t ax, ay, az;
int16_t gx, gy, gz;

struct MyData {
  byte aX;
  byte aY;
  byte aZ;
  byte gX;
  byte gY;
  byte gZ; 
};

MyData data;

void setup() { 
  Serial.begin(9600);
  Wire.begin();
  Wire.setClock(40000); //400Hz, sets I2C clock
  mpu.initialize();
  
}

void loop() { 
  if (Serial.available() > 0){
    mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

    data.aX = map(ax, -17000, 17000, 0, 255);
    data.aY = map(ay, -17000, 17000, 0, 255);
    data.aZ = map(az, -17000, 17000, 0, 255);

    data.gX = map(gx, -17000, 17000, 0, 255);
    data.gY = map(gy, -17000, 17000, 0, 255);
    data.gZ = map(gz, -17000, 17000, 0, 255);

    //printing the data
    //structure: ax ay az gx gy gz
    Serial.print(data.aX); Serial.print(" ");
    Serial.print(data.aY); Serial.print(" ");
    Serial.print(data.aZ); Serial.print(" ");
    Serial.print(data.gX); Serial.print(" ");
    Serial.print(data.gY); Serial.print(" ");
    Serial.print(data.gZ); Serial.print(" ");
    Serial.print("\n");

    delay(100); 
  }

  
}