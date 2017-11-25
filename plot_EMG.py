import numpy as np
import matplotlib.pyplot as plt

data= np.loadtxt("EMG_raw_data.txt")  #load the file
p=np.linspace(0,5,num = data.shape[0]) #0 to 5 seconds then take the first column from data 
plt.figure(1)    
plt.plot(p, data[:,0])  #plot data 
plt.xlabel('Time')      #title axis
plt.ylabel('Reading')
plt.title('EMG raw')
plt.show()

data=np.loadtxt("EMG_scaled_data.txt")  #load file
p=np.linspace(0,5,num = data.shape[0])
plt.figure(2)
plt.plot(p, data[:,0])
plt.xlabel('Time')
plt.ylabel('Reading')
plt.title('EMG scaled')
plt.show()





