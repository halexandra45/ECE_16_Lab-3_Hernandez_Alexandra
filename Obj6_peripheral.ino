#include <CurieBLE.h>
#include <CurieIMU.h>
#include "CurieTimerOne.h"

const int timerISR = 5000;
float x,y,z;
int u,v,w;
int emgread_a, emgread_b;
int a,b;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  // Initialize IMU
  CurieIMU.begin();
  Serial.println("IMU initialized...");

  // Set Accelerometer range
  CurieIMU.setAccelerometerRange(2);

  //Set gryoscope range
  CurieIMU.setGyroRange(258);

  // Initialize the CurieBLE
  BLE.begin();

  Serial.println("BLE Accelerometer Central");
  Serial.println("BLE Gyro Central");
  // Scan/look-for a Peripheral
  BLE.scanForUuid("ECE16-20");

  
}

void loop() {
  
  // See if we found the Accelerometer Peripheral
  BLEDevice peripheral=BLE.available();

  // If a peripheral has been connected to:
  if(peripheral) {
    // We found the peripheral we were looking for!
    Serial.print("Discovered ");
    Serial.print(peripheral.address());
    Serial.print(" '");
    Serial.print(peripheral.localName());
    Serial.print("' ");
    Serial.println(peripheral.advertisedServiceUuid());

    // No need to keep looking for anything else now
    BLE.stopScan();

    

    // Write Accelerometer readings to Peripheral's Accelerometer Service + Characteristics
    write_to_peripheral(peripheral);

    // If we disconnected with Peripheral, try again!
    BLE.scanForUuid("ECE16-20");
  }
}
void readSensor(){
  x=CurieIMU.readAccelerometerScaled(X_AXIS);
  y=CurieIMU.readAccelerometerScaled(Y_AXIS);
  z=CurieIMU.readAccelerometerScaled(Z_AXIS);
  u=CurieIMU.readGyroScaled(X_AXIS); 
  v=CurieIMU.readGyroScaled(Y_AXIS);
  w=CurieIMU.readGyro(Z_AXIS);
  emgread_a = analogRead(A0);
  a = ((emgread_a*3.3/1023)-1.5)/0.036;
  emgread_b = analogRead(A1);
  b = ((emgread_b*3.3/1023)-1.5)/0.036;
}


void write_to_peripheral(BLEDevice peripheral) {
  // Connect to Peripheral
    Serial.println("Connecting...");

    if(peripheral.connect()) {
      Serial.println("Connected!");
    } else {
      Serial.println("Failed to connect!");    
      return; 
    }

    // See if our Peripheral has Characteristics/Attributes
    Serial.println("Discovering Characteristics/Attributes ...");
    if (peripheral.discoverAttributes()) {
      Serial.println("Characteristics/Attributes discovered");
    } else {
      Serial.println("Characteristic/Attribute discovery failed!");
      peripheral.disconnect();      
      return;  
    }
    
  // Retrieve the Accelerometer Characteristic(s) from Peripheral
  BLECharacteristic accelerometer_characteristic_x=peripheral.characteristic("ECE16-20-01");
  BLECharacteristic accelerometer_characteristic_y=peripheral.characteristic("ECE16-20-02");
  BLECharacteristic accelerometer_characteristic_z=peripheral.characteristic("ECE16-20-03");

  BLECharacteristic gyro_characteristic_u=peripheral.characteristic("ECE16-20-04");
  BLECharacteristic gyro_characteristic_v=peripheral.characteristic("ECE16-20-05");
  BLECharacteristic gyro_characteristic_w=peripheral.characteristic("ECE16-20-06");

  BLECharacteristic EMG_characteristic_a=peripheral.characteristic("ECE16-20-07");
  BLECharacteristic EMG_characteristic_b=peripheral.characteristic("ECE16-20-08");
  
  // While we are still connected to the Peripheral, update its IMU Characteristics
  while(peripheral.connected()){
    
//    CurieIMU.readAccelerometerScaled(x,y,z);
    CurieTimerOne.start(timerISR,&readSensor);
    
    accelerometer_characteristic_x.writeFloat(x);
    accelerometer_characteristic_y.writeFloat(y);
    accelerometer_characteristic_z.writeFloat(z);
    
    gyro_characteristic_u.writeInt(u);
    gyro_characteristic_v.writeInt(v);
    gyro_characteristic_w.writeInt(w);

    EMG_characteristic_a.writeInt(a);
    EMG_characteristic_b.writeInt(b);
  }

  Serial.println("Peripheral disconnected!");
}
