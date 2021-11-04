from cv2 import cv2 as cv
import numpy as np
from scipy.spatial import distance as dist

# Read the image
img = cv.imread("cube_pics/cube2.jpg")
cv.imshow('image', img)

# Convert to grayscale
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray", img_gray)

# Median Filtering
img_med = cv.medianBlur(img_gray,25)
cv.imshow("median", img_med)

# Sharpen the image
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
img_sharp = cv.filter2D(img_med, -1, sharpen_kernel)
cv.imshow("sharp", img_sharp)

# Threshold the image
img_thresh = cv.adaptiveThreshold(img_sharp,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,175,1)
cv.imshow("thresh", img_thresh)
    
# Perform morphological operations
kernel = cv.getStructuringElement(cv.MORPH_RECT, (7,7))
img_morph = cv.morphologyEx(img_thresh, cv.MORPH_CLOSE, kernel, iterations=1)
cv.imshow("morph", img_morph)

def get_color(image, contour):
    colours = ["red", "green", "blue", "yellow", "white", "orange"]
    bgr_codes = [(0, 0, 255),(0, 255, 0),(255, 0, 0),(0,204,204),(255,255,255),(0, 128, 255)]

    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv.drawContours(mask, [contour], -1, 255, -1)
    mask = cv.erode(mask, None, iterations=6)
    mean = cv.mean(image, mask=mask)[:3]

    min_dist_color = np.argmin(np.array([dist.euclidean(bgr, mean) for bgr in bgr_codes]))

    return colours[min_dist_color]

# Find contours
cnts = cv.findContours(img_morph, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
min_area = 1e4
max_area = 1e5
stickers = []
for c in cnts:
    area = cv.contourArea(c)
    if area > min_area and area < max_area:
        stickers.append(c)
        x,y,w,h = cv.boundingRect(c)
        colour = get_color(img, c)
        cv.putText(img,colour, (int(x + w/2), int(y + h/2)), cv.FONT_HERSHEY_TRIPLEX, 1, (255,255,255), 2)
        
cv.drawContours(img, stickers, -1, (80,255,15), 3)
cv.imshow("contours", img)

cv.waitKey(0)
cv.destroyAllWindows()
