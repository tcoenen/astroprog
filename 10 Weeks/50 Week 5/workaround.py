import sys

import numpy
from PIL import Image

def imread(filename):
    '''
    Open an image and turn it into a Numpy array without scipy.ndimage.imread
    '''
    return numpy.array(Image.open(filename))


def test(filename):
    '''see whether this works'''
    print 'Attempting to open', filename
    ar = imread(filename)
    print 'array.shape', ar.shape
    print 'array.dtype', ar.dtype

if __name__ == '__main__':
    test(sys.argv[1])
