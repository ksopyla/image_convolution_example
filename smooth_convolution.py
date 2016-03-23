'''It uses smooth kernel for RGB image
'''

import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

import helpers as hlp


#read image
im = plt.imread('img/building.jpg').astype(float)
im =im/255.   # normalise to 0-1, it's easier to work in float space
plt.imshow(im)

#smooth kernel  - small smooth
kernel = np.ones((5,5)) 
kernel/=25.0 

# bigger kernel matrix
#t = 1 - np.abs(np.linspace(-1, 1, 21))
#kernel = t.reshape(21, 1) * t.reshape(1, 21)
#kernel /= kernel.sum()   # kernel should sum to 1!  :) 


# convolve 2d the kernel with each channel
r = scipy.signal.convolve2d(im[:,:,0], kernel, mode='same')
g = scipy.signal.convolve2d(im[:,:,1], kernel, mode='same')
b = scipy.signal.convolve2d(im[:,:,2], kernel, mode='same')

# stack the channels back into a 8-bit colour depth image and plot it
im_out = np.dstack([r, g, b])
im_out = (im_out * 255).astype(np.uint8) 

plt.subplot(2,1,1)
plt.imshow(im, interpolation='none', cmap=plt.cm.gray)
plt.subplot(2,1,2)
plt.imshow(im_out, interpolation='none', cmap=plt.cm.gray)
plt.show()
