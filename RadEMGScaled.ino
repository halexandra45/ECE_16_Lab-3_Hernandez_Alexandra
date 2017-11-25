#include "CurieTimerOne.h"
#include "CurieIMU.h"
int Start_time=0; //variable used to set timer
int end_time;
float scale;
float bias;
int val0=0;
int i=1;
int timeISR=5000; //sampling at 200Hz
void read_emg()   //callback funstion for interrupt
{
  
   val0=analogRead(A0);
   scale= ((val0*3.3)/1023); //
   Serial.print(scale);
   Serial.print("\t");
   bias=(scale-1.5);
   Serial.print("\t");
   Serial.print(bias/3.6); //scale down gain
   Serial.print("\t");
   end_time=micros();
   Serial.println(micros()-Start_time);
   Start_time=end_time;
   }

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  while(!Serial);
  Start_time=0;
  CurieTimerOne.start(timeISR,&read_emg);
}



void loop() {}
