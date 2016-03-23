import numpy as np

def rgb2gray(rgb):
    '''convert rgb image to gray scale, it uses formula
    gray_img = 0.299 R + 0.587 G + 0.114 B 
    
    '''
    
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
