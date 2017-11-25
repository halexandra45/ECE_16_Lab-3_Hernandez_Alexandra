import serial #import serial library
import time
ser= serial.Serial('/dev/cu.usbmodem1421', baudrate=115200, timeout=1) #open serial port
i=1;
                       
f1 = open('EMG_scaled_data.txt', 'w')  #create file

time_start = time.time()
time_end =time.time()

while (time_end-time_start < 5):     #read 5 seconds of data 
     time_end=time.time()
     
     arduinoData=ser.readline()       #read arduino data
     print(arduinoData.decode())      #print to console
     f1.write(arduinoData.decode())
     if not arduinoData:
         break
     
f1.close()
                              
    
       
    

    





        
    
   
        
        
        
        

    
    





