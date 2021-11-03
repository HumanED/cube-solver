import cv2 as cv
import matplotlib.pyplot as plt

meme = cv.imread("/Users/antonioleonvillares/Desktop/stonks.jpg")

grey_meme = cv.cvtColor(meme, cv.COLOR_BGR2GRAY)

# GRAYSCALE HISTOGRAM

grey_hist = cv.calcHist([grey_meme], channels = [0], mask = None, histSize = [256], ranges = [0,256])

fig, ax = plt.subplots(1,2, sharey = "row")
ax[0].plot(grey_hist, c = "k")
ax[0].set_title("Greyscale Pixel intensity Distribution")

# can also calculate hist using a mask

# RGB HISTOGRAM

channels = ("b", "g", "r")

for i, channel in enumerate(channels):
    hist = cv.calcHist([meme], channels = [i], mask = None, histSize = [256], ranges = [0,256])
    ax[1].plot(hist, c = channel, label = channel)

ax[1].legend()
ax[1].set_title("RGB Pixel intensity Distribution")
plt.setp(ax, xlabel = "Pixel Intensity", ylabel = "Count")
plt.show()


