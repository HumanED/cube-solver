import cv2 as cv
import numpy as np

meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")
grey_meme = cv.cvtColor(meme, cv.COLOR_BGR2GRAY)

# LAPLACIAN

# edges which seem smudged
# use the laplacian to compute gradients, as gradients indicate an edge
meme_laplacian = cv.Laplacian(grey_meme, ddepth = cv.CV_64F)
meme_laplacian = np.array(np.abs(meme_laplacian), dtype = "uint8")

cv.imshow("Laplacian Stonks", meme_laplacian)

# SOBEL

meme_sobelx = cv.Sobel(grey_meme, ddepth = cv.CV_64F, dx = 1, dy = 0)
meme_sobely = cv.Sobel(grey_meme, ddepth = cv.CV_64F, dx = 0, dy = 1)

cv.imshow("Sobel X Stonks", meme_sobelx)
cv.imshow("Sobel Y Stonks", meme_sobely)

meme_sobel = cv.bitwise_or(meme_sobelx, meme_sobely)

cv.imshow("Sobel Stonks", meme_sobel)

# canny is cleaner, but uses sobel


cv.waitKey(0)
# Bavesh Here :)