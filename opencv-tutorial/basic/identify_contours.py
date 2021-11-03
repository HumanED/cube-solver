import cv2 as cv
import numpy as np

meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")

cv.imshow("Stonks", meme)

# the contour of an image is composed of all the edges which enclose an iamge
# an edge is less high-level, and might consider only differences in intensity

grey_meme = cv.cvtColor(meme, cv.COLOR_BGR2GRAY)

cv.imshow("Grey Meme", grey_meme)

# CONTOURING VIA EDGE DETECTION

canny_meme = cv.Canny(grey_meme, threshold1 = 125, threshold2 = 175)

cv.imshow("Edged Meme", canny_meme)

# for contours
# 1) get edges of image
# 2) give how hierarchy should be displayed
# 3) give how contour should be found

contours, hierarchy = cv.findContours(canny_meme, mode = cv.RETR_LIST, method = cv.CHAIN_APPROX_NONE)

# contours is python list of all the contours of the image
# cv.RETR_LIST returns all contours find (can also have cv.RETR_EXTERNAL for only external contours, or cv.RETR_TREE for hierarchical contours)
# cv.CHAIN_APPROX_NONE (how we approximate the contour): in this case, will return ALL possible points in the contour
# cv.CHAIN_APPROX_SIMPLE simplies (i.e instead of giving all points in a line, just gives the endpoints)

print(f"{len(contours)} Contours Found in Image via Canny and CHAIN_APPROX_NONE")

contours_simple, hierarchy_simple = cv.findContours(canny_meme, mode = cv.RETR_LIST, method = cv.CHAIN_APPROX_SIMPLE)

print(f"{len(contours_simple)} Contours Found in Image via Canny and CHAIN_APPROX_SIMPLE")

# We can reduce the contours if we apply blur

blurred_grey_meme = cv.GaussianBlur(grey_meme, ksize = (5,5), sigmaX = cv.BORDER_DEFAULT)
blurred_canny_meme = cv.Canny(blurred_grey_meme, threshold1 = 125, threshold2 = 175)
contours_blurred, hierarchy_blurred = cv.findContours(blurred_canny_meme, mode = cv.RETR_LIST, method = cv.CHAIN_APPROX_NONE)

cv.imshow("Blurred Stonks", blurred_grey_meme)
cv.imshow("Blurred Edged Stonks", blurred_canny_meme)

print(f"{len(contours_blurred)} Contours Found in Image via Blurred Canny and CHAIN_APPROX_NONE")

# CONTOURING VIA THRESHOLDING

# When thresholding, we essentially turn each pixel in the image into either black or white

ret, thresh = cv.threshold(grey_meme, thresh = 125, maxval = 255, type = cv.THRESH_BINARY)

# any pixel with brightness less than 125 turns black, otherwise white

cv.imshow("Thresholded Stonks", thresh)

contours_thresh, hierarchy_thresh = cv.findContours(thresh, mode = cv.RETR_LIST, method = cv.CHAIN_APPROX_NONE)

print(f"{len(contours_thresh)} Contours Found in Image via Thresholding and CHAIN_APPROX_NONE")

# VISUALISING THE CONTOURS

def vis_contours(contours, dimensions, colour = (0,0,255), thickness = 1):
    blank = np.zeros(dimensions, dtype="uint8")
    cv.drawContours(blank, contours = contours, contourIdx = -1, color = colour, thickness = thickness)

    return blank

cv.imshow("Contour Stonks", vis_contours(contours, meme.shape))
cv.imshow("Contour Threshold Stonks", vis_contours(contours_thresh, meme.shape))
cv.imshow("Contour Blurred Stonks", vis_contours(contours_blurred, meme.shape))

cv.waitKey(0)