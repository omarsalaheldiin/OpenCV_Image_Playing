import cv2 as cv
import numpy as np

def rescale(img, scale):
    width = int(img.shape[1]*scale)
    hight = int(img.shape[0]*scale)
    size = (width, hight)
    return cv.resize(img, size, interpolation=cv.INTER_CUBIC)

img = rescale(cv.imread("image3.jpg"), 0.35)
cv.imshow("img", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank", blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1 )
cv.imshow("mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked", masked)

cv.waitKey(0)
