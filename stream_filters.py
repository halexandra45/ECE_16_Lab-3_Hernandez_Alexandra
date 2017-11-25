import numpy as np
import matplotlib.pyplot as plt
import time
import serial #import serial library
import scipy.signal
import matplotlib.animation as animation

#read from serial port
ser= serial.Serial('/dev/cu.usbmodem1421', baudrate=115200,timeout=1)

sample_rate= 200


def play(t, time_step, samples, sample_rate):
    plt.ion #interactive plotting
    plt.plot(ser)
    plt.xlabel('Time(s)')
    plt.ylabel('mV')
    #more formatting need here
    
    
    while True:
        line=ser.readline()
        #split it up
        #add value to the end of my time and data arrays
        
        #read data from serial
        ser.read()
        #make time array(time from Serial)
        #make data array
        x=np.array(data1)
        y=np.array(data2)
        
        plt.pause(0.01)
        plt.plot()
        
        
#array t holds the times to plot at time step
samples=100 *0.1*200
t=np.arange(0.0,samples)/200
play(t,0.1,100,200)
















