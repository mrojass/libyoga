"""
Module for applying straight line Hough transformations to processed images (
specifically ones that have been processed with a Canny edge detection
algorithm) of yoga poses.
"""
from math import degrees
import numpy as np
from skimage.transform import (hough_line, hough_line_peaks)
from skimage.io import imread


def lines(base, test):
    image1 = imread(base, flatten=True)
    image2 = imread(test, flatten=True)

    # Angles
    a1 = []
    a2 = []

    group1_a1 = []
    group2_a1 = []
    group3_a1 = []

    # # Plot 1 -> Base Case (original)
    # print "Plot 1"
    h, theta, d = hough_line(image1)
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
        elif degree > -45 and degree < 0:
            if degree > -40 and degree < -25:
                group2_a1.append(degree)
        elif degree > 0 and degree < 45:
            if degree > 15 and degree < 40:
                group3_a1.append(degree)

    if len(pos_horizontal) == 0:
        avg_horizontal = reduce(lambda x, y: x + y, neg_horizontal) / float(len(neg_horizontal))
    elif len(neg_horizontal) == 0:
        avg_horizontal = reduce(lambda x, y: x + y, pos_horizontal) / float(len(pos_horizontal))
    else:
        avg_neg = reduce(lambda x, y: x + y, neg_horizontal) / float(len(neg_horizontal))
        avg_pos = reduce(lambda x, y: x + y, pos_horizontal) / float(len(pos_horizontal))
        avg_horizontal = (avg_pos + avg_neg)/2

    print "BASE HORIZONTAL: " + str(avg_horizontal)

    h1, theta1, d1 = hough_line(image2)
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
        elif degree > -45 and degree < 0:
            if degree > -40 and degree < -25:
                group2_a2.append(degree)
        elif degree > 0 and degree < 45:
            if degree > 15 and degree < 40:
                group3_a2.append(degree)
        a2.append(degrees(angle))

    if len(pos_horizontal_user) == 0:
        avg_horizontal_user = reduce(lambda x, y: x + y, neg_horizontal_user) / float(len(neg_horizontal_user))
    elif len(neg_horizontal_user) == 0:
        avg_horizontal_user = reduce(lambda x, y: x + y, pos_horizontal_user) / float(len(pos_horizontal_user))
    else:
        avg_neg = reduce(lambda x, y: x + y, neg_horizontal_user) / float(len(neg_horizontal_user))
        avg_pos = reduce(lambda x, y: x + y, pos_horizontal_user) / float(len(pos_horizontal_user))
        avg_horizontal_user = (avg_pos + avg_neg)/2

    avg_down = -1
    avg_up =-1

    base_down = reduce(lambda x, y: x + y, group2_a1) / float(len(group2_a1))
    if len(group2_a2) > 0:
        avg_down = reduce(lambda x, y: x + y, group2_a2) / float(len(group2_a2))
    base_up = reduce(lambda x, y: x + y, group3_a1) / float(len(group3_a1))
    if len(group3_a2) > 0:
        avg_up = reduce(lambda x, y: x + y, group3_a2) / float(len(group3_a2))

    print "USER HORIZONTAL: " + str(avg_horizontal_user)

    print "BASE DOWN: " + str(base_down)
    print "USER DOWN: " + str(avg_down)

    print "BASE UP: " + str(base_up)
    print "USER UP: " + str(avg_up)

    base_down = float(base_down)
    base_up = float(base_up)
    user_down = float(avg_down)
    user_up = float(avg_up)

    # Calculate score
    score = 10

    lost_down = abs(base_down - avg_down)
    lost_up = abs(base_up - avg_up)
    lost_horizontal = abs(avg_horizontal - avg_horizontal_user)

    SCORE_FACTOR = 3             # equals max angle of error / 10
    score1 = lost_down / SCORE_FACTOR
    score2 = lost_up / SCORE_FACTOR
    score3 = lost_horizontal / SCORE_FACTOR

    neg_points = (score1 + score2 + score3) / 3.0
    score -= neg_points
    print "SCORE: " + str(score)
    return score
