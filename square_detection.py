from cv2 import cv2 as cv
import numpy as np

# Read the image
img = cv.imread("cube_pics/cube1.jpg")
cv.imshow('image', img)
cv.waitKey()

# Convert to grayscale
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray", img_gray)
cv.waitKey(0)

# Blur the image
blur = cv.GaussianBlur(img_gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey(0)

# Extract the edges
canny = cv.Canny(blur, 10, 10, 4, L2gradient = True)
cv.imshow('Canny Edges', canny)
cv.waitKey(0)

# Find the contours
contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

squares = []
for cnt in contours:
    area = cv.contourArea(cnt)
    print(area)
    if area > 100: 
        approx = cv.approxPolyDP(cnt, 0.009 * cv.arcLength(cnt, True), True)
        squares.append(cnt)

cv.drawContours(img, squares, -1, (0, 255, 0), 3 )
cv.imshow('squares', img)
cv.waitKey(0)


    