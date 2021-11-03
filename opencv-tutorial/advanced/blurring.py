import cv2 as cv

meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")

cv.imshow("Stonks", meme)

# Blurring uses kernels to change a certain pixel based on its surroundings

# AVERAGING
# the value of a pixel is given by the average of the intensities of the surrounding pixels

average_meme = cv.blur(meme, ksize = (3,3))
cv.imshow("Average Stonks", average_meme)

# GAUSSIAN
# use a gaussian distributioin to give pixels weights, from which we calculate the center pixel value
# less blurring than averaging, but more natural

gauss_meme = cv.GaussianBlur(meme, ksize = (3,3), sigmaX = 0)
cv.imshow("Gaussian Stonks", gauss_meme)

# MEDIAN BLUR
# like averaging, but using median
# good when removing noise

median_meme = cv.medianBlur(meme, ksize = 3)
cv.imshow("Median Stonks", median_meme)

# BILATERAL BLUR
# blurs, but retains edges
# sigmaColor gives differences in colour to consider when blurring
# sigmaSpace gives the distance between a pixel and other pixels which influence this pixel

bilateral_meme = cv.bilateralFilter(meme, d = 10, sigmaColor = 35, sigmaSpace = 40)
cv.imshow("Bilateral Stonks", bilateral_meme)

cv.waitKey(0)