import cv2 as cv
import numpy as np

def rescale(img, scale):
    width = int(img.shape[1]*scale)
    hight = int(img.shape[0]*scale)
    size = (width, hight)
    return cv.resize(img, size, interpolation=cv.INTER_CUBIC)

img = rescale(cv.imread("image3.jpg"), 0.25)
cv.imshow("img", img)

b,g,r = cv.split(img)

cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

blank = np.zeros(shape=img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("blue2", blue)
cv.imshow("green2", green)
cv.imshow("red2", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

cv.waitKey(0)
