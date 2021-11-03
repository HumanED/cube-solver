from cv2 import cv2 as cv
import numpy as np

cube = cv.imread("cube_pics/cube1.jpg")

cube_grey = cv.cvtColor(cube,cv.COLOR_BGR2GRAY)
cv.imshow("Cube", cube_grey)
cv.waitKey(0)

cube_grey_blur = cv.GaussianBlur(cube_grey, (7,7), 2, 2)
cv.imshow("Cube", cube_grey_blur)
cv.waitKey(0)

cube_edge = cv.Canny(cube_grey_blur, 0, 30, 3)
cv.imshow("Cube", cube_edge)
cv.waitKey(0)

mask = cv.bitwise_and(cube_grey, cube_edge)
cv.imshow("Cube", mask)
cv.waitKey(0)

adaptive_threshold = cv.adaptiveThreshold(cube_grey, maxValue = 255, adaptiveMethod = cv.ADAPTIVE_THRESH_MEAN_C, thresholdType = cv.THRESH_BINARY_INV, blockSize = 11, C = 3)
cv.imshow("Adaptive Thresh Stonks", adaptive_threshold)
cv.waitKey(0)






