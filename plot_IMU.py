import numpy as np
import matplotlib.pyplot as plt  #plots shown in lab report



plt.subplot(331)
data= np.loadtxt("gyro_output.txt") 
p=np.linspace(0,1000,num = data.shape[0]) 
plt.plot(p, data[:,1])
plt.xlabel('Samples')
plt.ylabel('Reading X Gyroscope')

plt.show()

plt.subplot(332)
data= np.loadtxt("gyro_output.txt") 
p=np.linspace(0,1000,num = data.shape[0]) 
plt.plot(p, data[:,2])
plt.xlabel('Samples')
plt.ylabel('Reading Y Gyroscope')

plt.show()

plt.subplot(333)
data= np.loadtxt("gyro_output.txt") 
p=np.linspace(0,1000,num = data.shape[0]) 
plt.plot(p, data[:,3])
plt.xlabel('Samples')
plt.ylabel('Reading Z Gyroscope')

plt.show()


plt.subplot(334)
data= np.loadtxt("accel_output.txt") 
p=np.linspace(0,1000,num = data.shape[0]) 
plt.plot(p, data[:,1])
plt.xlabel('Samples')
plt.ylabel('Reading X Accelerometer')

plt.show()

plt.subplot(335)
data= np.loadtxt("accel_output.txt") 
p=np.linspace(0,1000,num = data.shape[0]) 
plt.plot(p, data[:,2])
plt.xlabel('Samples')
plt.ylabel('Reading Y Accelerometer')

plt.show()

plt.subplot(336)
data= np.loadtxt("accel_output.txt") 
p=np.linspace(0,1000,num = data.shape[0]) 
plt.plot(p, data[:,3])
plt.xlabel('Samples')
plt.ylabel('Reading Z Accelerometer')
plt.show()