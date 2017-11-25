
#include "CurieTimerOne.h"
#include "CurieIMU.h"
int Start_time=0; //variable used to set timer
int end_time;
char my_input;
int val0=0;
int timeISR=5000; //sampling at 200Hz
void printData()   //callback funstion for interrupt


{
  //Get raw EMG value
  val0=analogRead(A0);
  Serial.print(val0);
  Serial.print("\t");
  end_time=micros();
  Serial.println(micros()-Start_time);
  Start_time=end_time;
  Serial.println();
  
  
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  while(!Serial);
    Start_time=0;
    CurieTimerOne.start(timeISR,&printData);
}

void loop() {}
