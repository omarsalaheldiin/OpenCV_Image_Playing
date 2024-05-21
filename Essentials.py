import cv2 as cv


def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    hight = int(frame.shape[0] * scale)
    
    dimensions = (width, hight)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('image.jpg')
img_rescaled = rescale(img, 0.15)
cv.imshow("colored", img_rescaled)

#Convert to gray scale
gray = cv.cvtColor(img_rescaled, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#Blur
blur =cv.GaussianBlur(img_rescaled, (5,5), cv.BORDER_DEFAULT)
cv.imshow("colored_blur", blur)

#edge cascade
canny = cv.Canny(blur, 215, 175)
cv.imshow("canny", canny)

#Dialating image

dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("dialated", dilated)

#eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("eroded", eroded)

#croping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)



cv.waitKey(0)
