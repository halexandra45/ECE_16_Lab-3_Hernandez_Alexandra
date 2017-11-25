import scipy
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sig

order = 3
data= np.loadtxt("EMG_scaled_data.txt") 
signal_in= data[0:1000,0]
sizeof = np.size(signal_in)
m=np.arange(0.,sizeof,1.0)
lowfs=0.5
highfs=0.1

def lowpass(order, lowfs, signal_in):
    b_low, a_low = signal.butter(order, lowfs, 'lowpass', analog=False)
    signal_out = signal.lfilter(b_low, a_low, signal_in)
    return signal_out

def highpass(order,highfs, signal_in):
    b_high, a_high = signal.butter(order, highfs, 'highpass', analog=False)
    signal_out = signal.lfilter(b_high, a_high, signal_in)
    return signal_out

def both(order,highfs,lowfs,signal_in):
    b_low, a_low = signal.butter(order, lowfs, 'lowpass', analog=False)
    signal_out = signal.lfilter(b_low, a_low, signal_in)
    b_high, a_high = signal.butter(3, highfs, 'highpass', analog=False)
    signal_out = signal.lfilter(b_high, a_high, signal_out)
    return signal_out

array= np.loadtxt("EMG_scaled_data.txt") 
plt.subplot(331)
plt.plot(m, data[0:1000,0])
plt.xlabel('Samples')
plt.ylabel('Reading')
plt.title('EMG scaled')
plt.show()
plt.tight_layout(h_pad=0.001)  #creates padding

#lowpass
low_in= lowpass(order, lowfs, signal_in)
plt.subplot(332)
plt.xlabel('Samples')
plt.ylabel('Reading')
plt.title('EMG scaled lowpass')
plt.plot(m,low_in)
plt.show()
plt.tight_layout(h_pad=0.001)  #creates padding

#highpass
high_in= highpass(order, highfs, signal_in)
plt.subplot(333)
plt.xlabel('Samples')
plt.ylabel('Reading')
plt.title('EMG scaled highpass')
plt.plot(m,high_in)
plt.show()
plt.tight_layout(h_pad=0.001)  #creates padding

#bandpass
both_in= both(order,highfs,lowfs,signal_in)
plt.subplot(334)
plt.xlabel('Samples')
plt.ylabel('Reading')
plt.title('EMG scaled both(highpass & lowpass)')
plt.plot(m,both_in)
plt.show()
plt.tight_layout(h_pad=0.001)  #creates padding
 

# Rectify the signal
signal_in = abs(both_in)
plt.subplot(335)
plt.xlabel('Samples')
plt.ylabel('Reading')
plt.title('EMG signal rectified')
plt.plot(m,signal_in)
plt.show()
plt.tight_layout(h_pad=0.001)  #creates padding

# Smooth with a 100-point boxcar window
box = scipy.signal.boxcar(100)
signal_out = scipy.signal.lfilter(box, 1, signal_in)
plt.subplot(336)
plt.xlabel('Samples')
plt.ylabel('Reading')
plt.title('EMG signal smooth')
plt.plot(m,signal_out)
plt.show() 
plt.tight_layout(h_pad=0.001)  #creates padding

frequency, power = sig.welch(both_in,200)
plt.subplot(337)
plt.xlabel('Hz')
plt.ylabel('log(power/Hz')
plt.title('Power Spectral Density')
plt.plot(frequency,power)
plt.show() 
plt.tight_layout(h_pad=0.001)  #creates padding 
