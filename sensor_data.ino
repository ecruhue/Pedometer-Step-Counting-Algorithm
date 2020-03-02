// collect sensor data gyroscope 
#include <Wire.h>
#include <SparkFunLSM9DS1.h>
LSM9DS1 imu;
unsigned long time;


void setup() {
  Serial.begin(115200);
  Wire.begin();
  imu.begin();

}

void loop() {
  time = millis();
  if ( imu.accelAvailable() )
    imu.readAccel();
  if ( imu.gyroAvailable() )
    imu.readGyro();

  float ax = imu.calcAccel(imu.ax);
  float ay = imu.calcAccel(imu.ay);
  float az = imu.calcAccel(imu.az);

  float gx = imu.calcGyro(imu.gx);
  float gy = imu.calcGyro(imu.gy);
  float gz = imu.calcGyro(imu.gz);

//  Serial.print(ax); 
//  Serial.print("\t"); 
//  Serial.print(ay); 
//  Serial.print("\t"); 
//  Serial.print(az);
//  Serial.print("\t"); 
  Serial.print(gy); 
  Serial.print(","); 
  Serial.print(gz); 
  Serial.print(","); 
  Serial.print(gx); 
  Serial.println();
  delay(50);
}
