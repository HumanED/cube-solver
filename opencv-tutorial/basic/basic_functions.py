import cv2 as cv

meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")

cv.imshow("OG Stonks", meme)

# CONVERT IMAGE TO GREYSCALE

grey_meme = cv.cvtColor(meme, cv.COLOR_BGR2GRAY)
cv.imshow("Grey Stonks", grey_meme)

# BLUR IMAGE

# ksize is the size of the kernel for the gaussian blur
# sigmaX is the standard deviation of gaussian kernel in x direction
# for more blur, increase ksize or sigmaX

blur_meme = cv.GaussianBlur(meme, ksize = (3,3), sigmaX = cv.BORDER_DEFAULT)
cv.imshow("Blurred Stonks", blur_meme)

# FIND EDGES OF THE IMAGE

# canny edge detection applies blur, then uses intensity gradient approximation technique (i.e Sobel)
# then uses threshold1 to determine edges, and threshold2 to differentiate between weak and strong edges
canny_meme = cv.Canny(meme, threshold1 = 125, threshold2 = 175)
cv.imshow("Edged Stonks", canny_meme)

# increasing the thresholds will reduce the amount of edges found
canny_meme2 = cv.Canny(meme, threshold1 = 175, threshold2 = 200)
cv.imshow("Mega Edged Stonks", canny_meme2)

# DILATING IMAGE

# dilates (increases thickness) of image (edges preferably, although also works weirdly on normal image)
dilated_canny_meme = cv.dilate(canny_meme, kernel = (3,3), iterations = 3)
cv.imshow("Dilated Edged Stonks", dilated_canny_meme)

# ERODING IMAGE

# attempts to reverse the effect of dilation
eroded_canny_meme = cv.dilate(dilated_canny_meme, kernel = (3,3), iterations = 3)
cv.imshow("Eroded Edged Stonks", eroded_canny_meme)

# RESIZING IMAGE

# use INTER_AREA for resizing to smaller, and INTER_LINEAR for resizing to larger
resized_stonks = cv.resize(meme, dsize = (400,400), interpolation = cv.INTER_AREA)
cv.imshow("Smaller Stonks", resized_stonks)

# CROP IMAGE

# just use slices

cv.imshow("Cropped Stonks", meme[0:200, 200:400])


cv.waitKey(0)