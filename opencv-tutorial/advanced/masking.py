import cv2 as cv
import numpy as np

meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")
blank = np.zeros(meme.shape[:2], dtype = "uint8")

mask = cv.circle(blank, center = (meme.shape[1]//2, meme.shape[0]//2), radius = 100, color = 255, thickness = -1)

masked_meme = cv.bitwise_and (meme, meme, mask = mask)

cv.imshow("Masked Stonks", masked_meme)

cv.waitKey(0)