import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np 

def rescale(img, scale):
    width = int(img.shape[1]*scale)
    hight = int(img.shape[0]*scale)
    size = (width, hight)
    return cv.resize(img, size, interpolation=cv.INTER_CUBIC)

img = rescale(cv.imread("image.jpg"), 0.15)
cv.imshow("img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

#sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("sobelx",sobelx)
cv.imshow("sobely",sobely)
cv.imshow("sobel combinde",sobel)

#canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('cany',canny)
cv.waitKey(0)
