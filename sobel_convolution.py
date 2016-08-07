import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

def rgb2gray(rgb):
    '''convert rgb image to gray scale, it uses formula
    gray_img = 0.299 R + 0.587 G + 0.114 B

    '''

    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


#read image
im = plt.imread('img/wikipedia_steam.png').astype(float)
#im =im/255.   # normalise to 0-1, it's easier to work in float space
plt.imshow(im)

gray = rgb2gray(im)
plt.imshow(gray, interpolation='none', cmap=plt.cm.gray)


#sobel filter


dxn = scipy.signal.convolve2d(np.array(gray), [[-1, 0, 1], [-2, 0,
2], [-1, 0, 1]])
dyn = scipy.signal.convolve2d(np.array(gray), [[-1, -2, -1], [0, 0,
0], [1, 2, 1]])
resn = dxn + dyn
a = 255. / (resn.max() - resn.min())
b = -a * resn.min()
edge= (resn*a+b).round()
plt.imshow(edge, interpolation='none', cmap=plt.cm.gray)

#compute the gradient magnitude 
mag = np.sqrt(dxn**2 + dyn**2)
#a = 255. / (resn.max() - resn.min())
#b = -a * resn.min()
plt.imshow(resn, interpolation='none', cmap=plt.cm.gray)

#compute gradient magnitude as above with numpy
mag=np.hypot(dxn,dyn)
#normalize
mag *=255.0/np.max(mag)
plt.imshow(mag, interpolation='none', cmap=plt.cm.gray)

