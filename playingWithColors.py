import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def rescale(img, scale):
    width = int(img.shape[1]*scale)
    hight = int(img.shape[0]*scale)
    size = (width, hight)
    return cv.resize(img, size, interpolation=cv.INTER_CUBIC)

img = rescale(cv.imread("image3.jpg"), 0.25)
cv.imshow("img", img)

imgrgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("imgrgb", imgrgb)

plt.imshow(imgrgb)
plt.show()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("lab", lab)

bgrFromGray = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow("bgr from gray", bgrFromGray)

cv.waitKey(0)
