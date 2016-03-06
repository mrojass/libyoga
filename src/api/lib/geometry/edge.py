import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage as ndi
from skimage import feature
from skimage import io

VAL_SIGMA = 4.5

def edge(ifile, ofile):
    img = io.imread(ifile, flatten=True)
    edges1 = feature.canny(img)
    edges2 = feature.canny(img, sigma=VAL_SIGMA)
    out = np.uint8(edges2 * 255)

    io.imsave(ofile, out)
    return ofile
