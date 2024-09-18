import cv2 as cv 

img = cv.imread('ganon.jpg',0 )
cv.imshow('salida', img)
x,y=img.shape
for i in range(x):
    for j in range (y):
        if(img[i,j]>150):
            img[i,j]=255
        else:
            img[i,j]=0

        if(img[i,j]>200):
            img[i,j]=100
        else:
            img[i,j]=10


cv.imshow('negativo', img)
print(img.shape)
cv.waitKey(0)
cv.destroyAllWindows()

#operador puntual
#operador de ventana o caja