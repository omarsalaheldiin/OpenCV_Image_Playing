import cv2 as cv
import numpy as np

blank = np.zeros((700,1000, 3), dtype='uint8')

blank[100:200, 150:250] = 0,0,255


cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=-1)
cv.imshow("rect", blank)


cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (200, 150, 70), -1)
cv.imshow("circle", blank)

cv.line(blank, (0,100),(blank.shape[1]//2, blank.shape[0]//2),(100, 100, 100), thickness=10)
cv.imshow("line", blank)

cv.putText(blank, 'kello', (50, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,250), 2)
cv.imshow('text', blank)



cv.waitKey(0)
