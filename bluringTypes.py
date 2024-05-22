import cv2 as cv
import numpy as np

def rescale(img, scale):
    width = int(img.shape[1]*scale)
    hight = int(img.shape[0]*scale)
    size = (width, hight)
    return cv.resize(img, size, interpolation=cv.INTER_CUBIC)

img = rescale(cv.imread("image3.jpg"), 0.25)
cv.imshow("img", img)

avg = cv.blur(img, (5,5))
cv.imshow("average", avg)

median = cv.medianBlur(img, 5)
cv.imshow("median", median)

gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow("gaussian", gauss)

bilat = cv.bilateralFilter(img, 10, 35, 30)
cv.imshow("bilateral", bilat)

cv.waitKey(0)
