import cv2 as cv
import numpy as np

meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")

cv.imshow("Stonks", meme)

# SPLIT (GREYSCALE)

blue, green, red = cv.split(meme)

cv.imshow("Blue Grey Stonks", blue)
cv.imshow("Green Grey Stonks", green)
cv.imshow("Red Grey Stonks", red)

# MERGE

full_meme = cv.merge([blue, green, red])
cv.imshow("Merged Stonks", full_meme)

# SPLIT (RGB)

def colour_split(img, colour = "red"):
    blank = np.zeros(img.shape[:2], dtype = "uint8")
    blue, green, red = cv.split(img)

    if (colour == "red"):
        return cv.merge([blank, blank, red])
    elif (colour == "green"):
        return cv.merge([blank, green, blank])
    else:
        return cv.merge([blue, blank, blank])

cv.imshow("Red Stonks", colour_split(meme))
cv.imshow("Green Stonks", colour_split(meme, "green"))
cv.imshow("Blue Stonks", colour_split(meme, "blue"))

cv.waitKey(0)