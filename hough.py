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
image1 = imread("gs-blur-dd-male2.jpg", flatten=True)
image2 = imread("gs-blur-dd-male.jpg", flatten=True)
image3 = imread("gs-blur-dd-female.jpg", flatten=True)
# print(image)

# Constructing test image.
# image = np.zeros((100, 100))
# idx = np.arange(25, 75)
# image[idx[::-1], idx] = 255
# image[idx, idx] = 255

h, theta, d = hough_line(image1)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8,4))

# ax1.imshow(image, cmap=plt.cm.gray)
# ax1.set_title('Input image')
# ax1.set_axis_off()

# ax2.imshow(np.log(1 + h),
#              extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]),
#                      d[-1], d[0]],
#              cmap=plt.cm.gray, aspect=1/1.5)
# ax2.set_title('Hough transform')
# ax2.set_xlabel('Angles (degrees)')
# ax2.set_ylabel('Distance (pixels)')
# ax2.axis('image')

ax1.imshow(image1, cmap=plt.cm.gray)
rows, cols = image1.shape
for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
    ax1.plot((0, cols), (y0, y1), '-r')
ax1.axis((0, cols, rows, 0))
ax1.set_title('Detected lines')
ax1.set_axis_off()
print h

h1, theta1, d1 = hough_line(image2)

ax2.imshow(image2, cmap=plt.cm.gray)
rows, cols = image2.shape
for _, angle, dist in zip(*hough_line_peaks(h1, theta1, d1)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
    ax2.plot((0, cols), (y0, y1), '-r')
ax2.axis((0, cols, rows, 0))
ax2.set_title('Detected lines')
ax2.set_axis_off()

h2, theta2, d2 = hough_line(image3)

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




# # # Line finding using the Probabilistic Hough Transform.
# # image = data.camera()
# edges = canny(image, 2, 1, 25)
# lines = probabilistic_hough_line(edges, threshold=10, line_length=100,
#                                  line_gap=100)

# # Generating figure 2.
# fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(16, 6), sharex=True,
#                                     sharey=True)
# plt.tight_layout()

# ax0.imshow(image, cmap=cm.gray)
# ax0.set_title('Input image')
# ax0.set_axis_off()
# ax0.set_adjustable('box-forced')

# ax1.imshow(edges, cmap=cm.gray)
# ax1.set_title('Canny edges')
# ax1.set_axis_off()
# ax1.set_adjustable('box-forced')


# ax2.imshow(edges * 0)
# for line in lines:
#     p0, p1 = line
#     ax2.plot((p0[0], p1[0]), (p0[1], p1[1]))

# row2, col2 = image.shape
# ax2.axis((0, col2, row2, 0))

# ax2.set_title('Probabilistic Hough')
# ax2.set_axis_off()
# ax2.set_adjustable('box-forced')

plt.show()