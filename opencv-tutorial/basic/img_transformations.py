import cv2 as cv
import numpy as np

meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")

cv.imshow("Stonks", meme)

# TRANSLATION

# an affine transformation is any transformation that can be expressed via a matrix
# we can translate an image in the x and y direction
def translate(img, x, y):
    translation_matrix = np.array([[1,0,x], [0,1,y]], dtype = np.float32) # need 32 bit float for translaion matrix
    img_dimensions = (img.shape[1], img.shape[0]) # width x height

    return cv.warpAffine(img, M = translation_matrix, dsize = img_dimensions)

cv.imshow("Translated Stonks", translate(meme, 100, 50))

# ROTATION

# rotate rotates counterclockwise
def rotate(img, rotation_angle, rotation_point = None, scale_factor = 1):
    height = img.shape[0]
    width = img.shape[1]

    if rotation_point is None:
        # assume rotating about center pixel
        rotation_point = (width//2, height//2)

    rotation_matrix = cv.getRotationMatrix2D(center = rotation_point, angle = rotation_angle, scale = scale_factor)
    dimensions = (width, height)

    return cv.warpAffine(img, M = rotation_matrix, dsize = dimensions)

cv.imshow("Rotated Stonks", rotate(meme, 90))

# RESIZING

def resize(img, resize_factor = 1, resize_interpolation = cv.INTER_AREA):
    resized_width = img.shape[1]*resize_factor
    resized_height = img.shape[0]*resize_factor
    new_dimensions = (resized_width, resized_height)

    return cv.resize(img, dsize = new_dimensions, interpolation = resize_interpolation)

cv.imshow("Resized Stonks", resize(meme, 2))

# FLIPPING

# flipCode 0 -> x flip
# flipCode 1 -> y flip
# flipCode -1 -> x and y flip
cv.imshow("Flipped Stonks", cv.flip(meme, flipCode = -1))

cv.waitKey(0)