"""
Compares the angles made between two yoga pose images and calculates a score.
"""
import sys
import hough

def score2(avg1, avg2, size1, size2):
    size_penalty = abs(size1 - size2) * 0.75
    angle_penalty = abs(avg1 - avg2) * 0.05
    return 10 - size_penalty - angle_penalty

def score(avg1, avg2, size1, size2):
    ratio1 = avg1 / size1
    ratio2 = avg2 / size2
    modifier = ratio1 / ratio2
    return 10 - (modifier * (size1 - size2))


A1, A2 = hough.lines(sys.argv[1], sys.argv[2])

a1_avg = 0
a2_avg = 0

for angle in A1:
    if angle < 0:
        angle *= -1
    a1_avg += angle

for angle in A2:
    if angle < 0:
        angle *= -1
    a2_avg += angle

a1_avg = a1_avg / len(A1)
a2_avg = a2_avg / len(A2)

print "Angle 1: " + str(a1_avg), "Size: " + str(len(A1))
print "Angle 2: " + str(a2_avg), "Size: " + str(len(A2))
print "Final Score: " + str(score(a1_avg, a2_avg, len(A1), len(A2)))
