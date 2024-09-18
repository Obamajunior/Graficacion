import cv2 as cv

cap = cv.VideoCapture(0)
while(True):
    ret, img = cap.read()
    if ret:
        cv.imshow('video',img)
        img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        w,h = img2.shape
        cv.imshow ('img2', img2)
        cv.imshow('hsv', hsv)
        k = cv.waitKey(1) & 0xFF
        if k == 27: 
         break   
    else:
     break

cap.release()
cv.destroyAllWindows