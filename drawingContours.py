import cv2 as cv
import numpy as np
def rescale(img, scale):
    width = int(img.shape[1]*scale)
    hight = int(img.shape[0]*scale)
    size = (width, hight)
    return cv.resize(img, size, interpolation=cv.INTER_CUBIC)

img = rescale(cv.imread("image3.jpg"), 0.25)
cv.imshow("img", img)


blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

ret, thresh = cv.threshold(canny, 125,255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST ,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')


cv.drawContours(blank, contours, -1,(0,0,255), 2)
cv.imshow("contours", blank)






cv.waitKey(0)
