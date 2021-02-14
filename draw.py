import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

blank[:] = 255,0,255
cv.imshow('color', blank)

cv.circle(blank, center=(250,250), radius = 200,color=(0,255,0), thickness=cv.FILLED)
cv.imshow('Circle', blank)

cv.rectangle(blank, (blank.shape[0]//2,blank.shape[1]//2),(300,300),(0,0,255))
cv.imshow('Rectangle', blank)

cv.line(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2),(255,255,255), thickness=5)
cv.imshow('Line', blank)

cv.putText(blank, 'Yohohohohohohohoho', (0,255), cv.FONT_HERSHEY_DUPLEX, 2.0,(0,255,255),4)
cv.imshow('Fontsy', blank)
cv.waitKey(0)