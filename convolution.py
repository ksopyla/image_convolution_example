import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


im = plt.imread('building.jpg')
#im =im/255.   # normalise to 0-1, it's easier to work in float space
plt.imshow(im)

#smooth kernel
kernel = np.ones((5,5))
kernel/=25.0


#find edges

kernel= np.zeros((5,5))
kernel[:,2]=np.array([-1,-1,2,0,0])

#sobel edge detector
#smooth kernel
#kernel = np.ones((3,3))
#kernel[:,0]=np.array([1,2,1])
#kernel[:,2]=np.array([-1,-2,-1])


#kernel = np.array([[1,1,1],[1,1,0],[1,0,0]])

#sharpern
#kernel = np.zeros((5,5))
#kernel[1,2]=-1
#kernel[2,1]=-1
#kernel[2,2]=5
#kernel[2,3]=-1
#kernel[3,2]=-1

# make some kind of kernel, there are many ways to do this...
#t = 1 - np.abs(np.linspace(-1, 1, 21))
#kernel = t.reshape(21, 1) * t.reshape(1, 21)
#kernel /= kernel.sum()   # kernel should sum to 1!  :) 
#

# convolve 2d the kernel with each channel
r = scipy.signal.convolve2d(im[:,:,0], kernel, mode='same')
g = scipy.signal.convolve2d(im[:,:,1], kernel, mode='same')
b = scipy.signal.convolve2d(im[:,:,2], kernel, mode='same')

# stack the channels back into a 8-bit colour depth image and plot it
im_out = np.dstack([r, g, b])
im_out = (im_out * 255).astype(np.uint8) 

plt.subplot(2,1,1)
plt.imshow(im, interpolation='nearest',aspect='auto')
plt.subplot(2,1,2)
plt.imshow(im_out, interpolation='nearest')
plt.show()