import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype = "uint8")

rectangle = cv.rectangle(blank.copy(), pt1 =  (30,30), pt2 = (370,360), color = 255, thickness = -1)
circle = cv.circle(blank.copy(), radius = 100, center = (200,200), color = 255, thickness = -1)

cv.imshow("Blank", blank)
cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# BITWISE AND

bitwise_and = cv.bitwise_and(rectangle, circle)

# BITWISE OR

bitwise_or = cv.bitwise_or(rectangle, circle)

# BITWISE XOR

bitwise_xor = cv.bitwise_xor(rectangle, circle)

# BITWISE NOT

bitwise_not = cv.bitwise_not(rectangle)

cv.imshow("AND", bitwise_and)
cv.imshow("OR", bitwise_or)
cv.imshow("XOR", bitwise_xor)
cv.imshow("NOT", bitwise_not)

cv.waitKey(0)