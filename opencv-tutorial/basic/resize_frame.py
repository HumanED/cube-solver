import cv2 as cv
meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")

cv.imshow("Normal Stonks", meme)

def rescaleFrame(frame, scale = 0.75):
    new_width = int(frame.shape[1] * scale)
    new_height = int(frame.shape[0] * scale)
    new_dims = (new_width, new_height)

    # interpolation is the method of estimating the value of new pixels when we resize an iamge
    return cv.resize(frame, new_dims, interpolation = cv.INTER_AREA)

cv.imshow("Small  Stonks", rescaleFrame(meme))
cv.imshow("Huge Stonks", rescaleFrame(meme, 2))

cv.waitKey(0)

