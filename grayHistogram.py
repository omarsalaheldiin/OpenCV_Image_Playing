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

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title("grayscale histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)
