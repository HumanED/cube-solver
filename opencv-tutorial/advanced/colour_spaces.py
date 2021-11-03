import cv2 as cv

meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")

cv.imshow("Stonks", meme)

# BGR to HSV (hue saturation value)

hsv = cv.cvtColor(meme, cv.COLOR_BGR2HSV)
cv.imshow("HSV Stonks", hsv)

# BGR to LAB (hue saturation value)

lab = cv.cvtColor(meme, cv.COLOR_BGR2LAB)
cv.imshow("LAB Stonks", lab)

# can also do the inverse conversions

cv.waitKey(0)