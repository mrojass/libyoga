"""
Compares the angles made between two yoga pose images and calculates a score.
"""
import sys
import hough

# Calculates a "score" based on angle comparisons
A1, A2 = hough.lines(sys.argv[1], sys.argv[2])

a1_avg = 0
a2_avg = 0

for angle in A1:
    a1_avg += angle

for angle in A2:
    a2_avg += angle

a1_avg = a1_avg / len(A1)
a2_avg = a2_avg / len(A2)

print "Angle 1: " + str(a1_avg)
print "Angle 2: " + str(a2_avg)
