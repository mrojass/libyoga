from math import degrees
from matplotlib import cm
from skimage.transform import (hough_line, hough_line_peaks,
                               probabilistic_hough_line)
from skimage.feature import canny
from skimage import data
from skimage.io import imread
import numpy as np
import matplotlib.pyplot as plt

#
image1 = imread("../../img/gs-blur-dd-male.jpg", flatten=True)
image2 = imread("../../img/gs-blur-dd-male2.jpg", flatten=True)
image3 = imread("../../img/gs-edge-male2.jpg", flatten=True)

h, theta, d = hough_line(image1)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8,4))

print "Plot 1"
ax1.imshow(image1, cmap=plt.cm.gray)
rows, cols = image1.shape
for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
    print degrees(angle)
    ax1.plot((0, cols), (y0, y1), '-r')
ax1.axis((0, cols, rows, 0))
ax1.set_title('Detected lines')
ax1.set_axis_off()

h1, theta1, d1 = hough_line(image2)

print "\nPlot 2"
ax2.imshow(image2, cmap=plt.cm.gray)
rows, cols = image2.shape
for _, angle, dist in zip(*hough_line_peaks(h1, theta1, d1)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
    print degrees(angle)
    ax2.plot((0, cols), (y0, y1), '-r')
ax2.axis((0, cols, rows, 0))
ax2.set_title('Detected lines')
ax2.set_axis_off()

h2, theta2, d2 = hough_line(image3)

print "\nPlot 3"
ax3.imshow(image3, cmap=plt.cm.gray)
rows, cols = image3.shape
for _, angle, dist in zip(*hough_line_peaks(h2, theta2, d2)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
    print degrees(angle)
    ax3.plot((0, cols), (y0, y1), '-r')
ax3.axis((0, cols, rows, 0))
ax3.set_title('Detected lines')
ax3.set_axis_off()

plt.show()
