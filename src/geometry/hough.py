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

    group1_a1 = []
    group2_a1 = []
    group3_a1 = []
    # Generate figure and 2 axes from matplotlib
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

    # # Plot 1 -> Base Case (original)
    # print "Plot 1"
    h, theta, d = hough_line(image1)
    ax1.imshow(image1, cmap=plt.cm.get_cmap('gray'))
    rows, cols = image1.shape

    for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
        y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
        y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
        degree = degrees(angle)
        a1.append(degree)
        if degree < -45 or degree > 45:
            if degree < -85 or degree > 85:
                pos_horizontal = []
                neg_horizontal = []
                if degree > 0:
                    pos_horizontal.append(90 - degree)
                elif degree <= 0:
                    neg_horizontal.append(-(degree + 90))
                ax1.plot((0, cols), (y0, y1), '-r')
        elif degree > -45 and degree < 0:
            if degree > -40 and degree < -25:
                group2_a1.append(degree)
                ax1.plot((0, cols), (y0, y1), '-r')
        elif degree > 0 and degree < 45:
            if degree > 15 and degree < 40:
                group3_a1.append(degree)
                ax1.plot((0, cols), (y0, y1), '-r')

    ax1.axis((0, cols, rows, 0))
    ax1.set_title('Detected lines')
    ax1.set_axis_off()
    if len(pos_horizontal) == 0:
        avg_horizontal = reduce(lambda x, y: x + y, neg_horizontal) / float(len(neg_horizontal))
    elif len(neg_horizontal) == 0:
        avg_horizontal = reduce(lambda x, y: x + y, pos_horizontal) / float(len(pos_horizontal))
    else:
        avg_neg = reduce(lambda x, y: x + y, neg_horizontal) / float(len(neg_horizontal))
        avg_pos = reduce(lambda x, y: x + y, pos_horizontal) / float(len(pos_horizontal))
        avg_horizontal = (avg_pos + avg_neg)/2

    print "BASE HORIZONTAL: " + str(avg_horizontal)
    # print group2_a1
    # print group3_a1

    # Plot 2 -> Test Case (submission)
    # print "\nPlot 2"
    h1, theta1, d1 = hough_line(image2)
    ax2.imshow(image2, cmap=plt.cm.gray)
    rows, cols = image2.shape

    group1_a2 = []
    group2_a2 = []
    group3_a2 = []
    for _, angle, dist in zip(*hough_line_peaks(h1, theta1, d1)):
        y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
        y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
        degree = degrees(angle)
        a2.append(degree)
        if degree < -45 or degree > 45:
            if degree < -85 or degree > 85:
                pos_horizontal_user = []
                neg_horizontal_user = []
                if degree > 0:
                    pos_horizontal_user.append(90 - degree)
                elif degree <= 0:
                    neg_horizontal_user.append(-(degree + 90))
                ax2.plot((0, cols), (y0, y1), '-r')
        elif degree > -45 and degree < 0:
            if degree > -40 and degree < -25:
                group2_a2.append(degree)
                ax2.plot((0, cols), (y0, y1), '-r')
        elif degree > 0 and degree < 45:
            if degree > 15 and degree < 40:
                group3_a2.append(degree)
                ax2.plot((0, cols), (y0, y1), '-r')
        a2.append(degrees(angle))
        # ax2.plot((0, cols), (y0, y1), '-r')

    if len(pos_horizontal_user) == 0:
        avg_horizontal_user = reduce(lambda x, y: x + y, neg_horizontal_user) / float(len(neg_horizontal_user))
    elif len(neg_horizontal_user) == 0:
        avg_horizontal_user = reduce(lambda x, y: x + y, pos_horizontal_user) / float(len(pos_horizontal_user))
    else:
        avg_neg = reduce(lambda x, y: x + y, neg_horizontal_user) / float(len(neg_horizontal_user))
        avg_pos = reduce(lambda x, y: x + y, pos_horizontal_user) / float(len(pos_horizontal_user))
        avg_horizontal_user = (avg_pos + avg_neg)/2

    print "USER HORIZONTAL: " + str(avg_horizontal_user)
    # print sorted(a2, key=float)
    # print group2_a2
    # print group3_a2

    print "BASE DOWN: " + str(reduce(lambda x, y: x + y, group2_a1) / float(len(group2_a1)))
    print "USER DOWN: " + str(reduce(lambda x, y: x + y, group2_a2) / float(len(group2_a2)))

    print "BASE UP: " + str(reduce(lambda x, y: x + y, group3_a1) / float(len(group3_a1)))
    print "USER UP: " + str(reduce(lambda x, y: x + y, group3_a2) / float(len(group3_a2)))

    ax2.axis((0, cols, rows, 0))
    ax2.set_title('Detected lines')
    ax2.set_axis_off()

    plt.show()
    return a1, a2
