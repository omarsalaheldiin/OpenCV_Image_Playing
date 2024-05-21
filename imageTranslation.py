import cv2 as cv
import numpy as np
def rescale(img, scale):
    width = int(img.shape[1]*scale)
    hight = int(img.shape[0]*scale)
    size = (width, hight)
    return cv.resize(img, size, interpolation=cv.INTER_CUBIC)

img = rescale(cv.imread("image2.jpg"), 0.5)
cv.imshow("img", img)


#translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dim = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dim)

translated = translate(img, 100, -100)
cv.imshow("translated", translated)


#rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dim = (width, height)
    
    return cv.warpAffine(img, rotMat, dim)

rotated = rotate(img, -45)
rotatedX2 = rotate(rotated, 45)
rotatedX3 = rotate(rotatedX2, -45)
cv.imshow("rotated", rotated)
cv.imshow("rotatedX2", rotatedX2)
cv.imshow("rotatedX3", rotatedX3)


#flipping

flipped = cv.flip(img, -1)
cv.imshow("flipped", flipped)


cv.waitKey(0)
