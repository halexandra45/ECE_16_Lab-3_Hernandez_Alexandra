from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

order = 3
data= np.loadtxt("EMG_scaled_data.txt") 
signal_in= data[0:1000,0]
sizeof = np.size(signal_in)
m=np.arange(0.,sizeof,1.0)
lowfs=0.5
highfs=0.1
y0=np.zeros(sizeof)
y1=np.zeros(sizeof)
y2=np.zeros(sizeof)
y_lowpass=np.zeros(sizeof)
y_highpass=np.zeros(sizeof)

b_low, a_low = signal.butter(order, lowfs, 'lowpass', analog=False)
y0= (b_low[0]*signal_in[0])  #b0*x[0]
y1= (b_low[0]*signal_in[1])+(b_low[1]*signal_in[0])-(a_low[1]*y0) #b0*x[n]+ b1*x[n-1] -a1[n-1]
y2= (b_low[0]*signal_in[2])+(b_low[1]*signal_in[1]) +(b_low[2]*signal_in[0]) -(a_low[1]*y1)-(a_low[2]*y0)    #b0*x[n]+b1*x[n-1]+b2*x[n-2] -a1*y1 -a2*y0   
    
def lowpass(order, lowfs, signal_in):
    b_low, a_low = signal.butter(order, lowfs, 'lowpass', analog=False)
    for i in range(sizeof):
         y_lowpass[i]= b_low[0]*signal_in[i]+b_low[1]*signal_in[i-1] +b_low[2]*signal_in[i-2] +b_low[3]*signal_in[i-3] -a_low[1]*y2 -a_low[2]*y1-a_low[3]*y0 
    return y_lowpass

def highpass(order, lowfs, signal_in):
    b_high, a_high = signal.butter(order, highfs, 'highpass', analog=False)
    for i in range(sizeof):
         y_highpass[i]= b_high[0]*signal_in[i]+b_high[1]*signal_in[i-1] +b_high[2]*signal_in[i-2] +b_high[3]*signal_in[i-3] -a_high[1]*y2 -a_high[2]*y1-a_high[3]*y0 
    return y_highpass

#original
array= np.loadtxt("EMG_scaled_data.txt") 
plt.subplot(331)
plt.plot(m, data[0:1000,0])
plt.xlabel('Samples')
plt.ylabel('Reading')
plt.title('EMG scaled')
plt.show()

#lowpass
low_in= lowpass(order, lowfs, signal_in)
plt.subplot(332)
plt.xlabel('Samples')
plt.ylabel('Reading')
plt.title('EMG scaled lowpass')
plt.plot(m,low_in)
plt.show()

#highpass
high_in= highpass(order, highfs, signal_in)
plt.subplot(333)
plt.xlabel('Samples')
plt.ylabel('Reading')
plt.title('EMG scaled highpass')
plt.plot(m,high_in)
plt.show()

