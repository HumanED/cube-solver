import cv2 as cv

videoPath = "/Users/antonioleonvillares/Desktop/Blender/HoleInHole/HoleInHoleVideo0001-0250.avi"

# arg 0 => webcame
capture = cv.VideoCapture(videoPath)

# Videos are read as images frame by frame
# will break when no more framesa re left

stillVideo = True

while (stillVideo):
    stillVideo, frame = capture.read()

    videoFrame = cv.imshow("Hole", frame)

    keyPress = cv.waitKey(20)

    if keyPress == 32: #if press spacebar
        stillVideo = False

capture.release()
cv.destroyAllWindows()

