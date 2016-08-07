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
gray = rgb2gray(im)
gray /= 255
plt.imshow(gray, interpolation='none', cmap=plt.cm.gray)


#emmboss filter
kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])

em_img = scipy.signal.convolve2d(gray, kernel)
em_img*=255

plt.subplot(1,3,1)
plt.imshow(im, interpolation='none', cmap=plt.cm.gray)
plt.subplot(1,3,2)
plt.imshow(gray, interpolation='none', cmap=plt.cm.gray)
plt.subplot(1,3,3)
plt.imshow(em_img, interpolation='none', cmap=plt.cm.gray)
plt.show()