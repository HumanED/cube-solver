import cv2 as cv
import numpy as np

#meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")

#cv.imshow("Normal Stonks", meme)
#cv.waitKey(0)

blank = np.zeros((500,500), dtype = "uint8")
rgbBlank = np.zeros((500,500,3), dtype = "uint8")

# COLOURING IMAGES

def recolourGrey(img, colourCode = 0):
    new_img = img.copy()
    new_img[:] = colourCode

    return new_img

#images in openCV are BGR instead of RGB
def recolourRGB(img, rgbCode = (255,0,0)):
    new_img = img.copy()
    bgrCode = (rgbCode[2], rgbCode[1], rgbCode[0])
    new_img[:] = bgrCode

    return new_img

# draw a rectangle of rgbCode colour and height (mid - top) and width (right - mid)
def portionRGB(img, top, mid, right, rgbCode = (255,0,0)):
    new_img = img.copy()
    bgrCode = (rgbCode[2], rgbCode[1], rgbCode[0])
    new_img[top:mid, mid:right] = bgrCode

    return new_img

"""
cv.imshow("Blank (Grey)", blank)
cv.imshow("Coloured (Grey)", recolourGrey(blank, 128))
cv.imshow("Blank (RGB)", rgbBlank)
cv.imshow("Coloured (RGB)", recolourRGB(rgbBlank))
cv.imshow("Coloured Portion(RGB)", portionRGB(rgbBlank, 200, 300, 400))
"""

# DRAWING ON IMAGES

rgb_blank = rgbBlank.copy()
#pt1 is top left, pt2 is bottom right
cv.rectangle(rgb_blank, pt1 = (0,0), pt2 = (400,400), color = (0,255,0), thickness = 2)
cv.imshow("Blank", rgbBlank)
cv.imshow("Rectangle", rgb_blank)

# fill in rectangle
# instead of cv.FILLED can also use -1

#cv.rectangle(rgb_blank, pt1 = (0,0), pt2 = (400,400), color = (0,255,0), thickness = cv.FILLED)
#cv.imshow("Filled Rectangle", rgb_blank)

# draw a circle

cv.circle(rgb_blank, center = (200,200), radius = 200, color = (0,128,128), thickness = 3)
cv.imshow("Circle", rgb_blank)

# draw a line

cv.line(rgb_blank, pt1 = (400,0), pt2 = (0,400), color = (0,0,255), thickness=5)
cv.imshow("Line", rgb_blank)

# WRITING ON IMAGES

cv.putText(rgb_blank, text = "STONKS", org = (100, 450), fontFace = cv.FONT_ITALIC, fontScale = 0.5, color = (255,255,255), thickness = 2)
cv.imshow("Text", rgb_blank)

cv.waitKey(0)