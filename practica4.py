import cv2 as cv
import numpy as np 

img = cv.imread('ganon.jpg',0)
x,y = img.shape
img2 = np.zeros((x,y), dtype=np.uint8)
for i in range(x):
    for j in range(y):
        img2[int(i*0.5),int(j+0.5)]=img[i,j]

cv.imshow('img', img)
cv.imshow('img2', img2)

cv.waitKey
cv.destroyAllWindows