import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("rect", rectangle)
cv.imshow("circ", circle)

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise AND', bitwise_and)

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise OR", bitwise_or)

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise XOR", bitwise_xor)

bitwise_not_rec = cv.bitwise_not(rectangle)
cv.imshow("bitwise NOT rectangle", bitwise_not_rec)

bitwise_not_circ = cv.bitwise_not(circle)
cv.imshow("bitwise NOT circle", bitwise_not_circ)


cv.waitKey(0)
