"""
Module for applying straight line Hough transformations to processed images (
specifically ones that have been processed with a Canny edge detection
algorithm) of yoga poses.
"""
from math import degrees
import numpy as np
from skimage.transform import (hough_line, hough_line_peaks)
from skimage.io import imread
import matplotlib.pyplot as plt


def lines(base, test):
    """
    Reads two images of yoga poses and compares them.
    """
    image1 = imread(base, flatten=True)
    image2 = imread(test, flatten=True)

    # Angles
    a1 = []
    a2 = []

    # Generate figure and 2 axes from matplotlib
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

    # Plot 1 -> Base Case (original)
    print "Plot 1"
    h, theta, d = hough_line(image1)
    ax1.imshow(image1, cmap=plt.cm.get_cmap('gray'))
    rows, cols = image1.shape

    for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
        y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
        y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
        print degrees(angle)
        a1.append(degrees(angle))
        ax1.plot((0, cols), (y0, y1), '-r')

    ax1.axis((0, cols, rows, 0))
    ax1.set_title('Detected lines')
    ax1.set_axis_off()


    # Plot 2 -> Test Case (submission)
    print "\nPlot 2"
    h1, theta1, d1 = hough_line(image2)
    ax2.imshow(image2, cmap=plt.cm.gray)
    rows, cols = image2.shape

    for _, angle, dist in zip(*hough_line_peaks(h1, theta1, d1)):
        y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
        y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
        print degrees(angle)
        a2.append(degrees(angle))
        ax2.plot((0, cols), (y0, y1), '-r')

    ax2.axis((0, cols, rows, 0))
    ax2.set_title('Detected lines')
    ax2.set_axis_off()

    plt.show()
    return a1, a2
