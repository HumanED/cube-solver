import cv2 as cv

meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")

cv.imshow("Stonks", meme)

grey_meme = cv.cvtColor(meme, cv.COLOR_BGR2GRAY)

# SIMPLE THRESHOLDING

# thresholded image is thresh

threshold, thresh = cv.threshold(grey_meme, thresh = 130 , maxval = 255, type = cv.THRESH_BINARY)

cv.imshow("Thresh Stonks", thresh)

threshold_inv, thresh_inv = cv.threshold(grey_meme, thresh = 130 , maxval = 255, type = cv.THRESH_BINARY_INV)

cv.imshow("Thresh Inverse Stonks", thresh_inv)

# ADAPTIVE THRESHOLDING

# previously, we had to provide threshold values; adaptive thresholding allows us to do this automaticlaly

# with cv.ADAPTIVE_THRESH_MEAN_C, we adapt based on mean, although other options are available
adaptive_threshold = cv.adaptiveThreshold(grey_meme, maxValue = 255, adaptiveMethod = cv.ADAPTIVE_THRESH_MEAN_C, thresholdType = cv.THRESH_BINARY, blockSize = 11, C = 3)

cv.imshow("Adaptive Thresh Stonks", adaptive_threshold)

cv.waitKey(0)