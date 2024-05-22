import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np 

def rescale(img, scale):
    width = int(img.shape[1]*scale)
    hight = int(img.shape[0]*scale)
    size = (width, hight)
    return cv.resize(img, size, interpolation=cv.INTER_CUBIC)

img = rescale(cv.imread("image3.jpg"), 0.35)
cv.imshow("img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

threshold, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
cv.imshow("simple threshold", thresh)

threshold, thresh_inverse = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple threshold inverse", thresh_inverse)


cv.waitKey(0)
