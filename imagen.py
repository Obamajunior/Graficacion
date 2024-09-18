import cv2 as cv
img = cv.imread('ganon.jpg') #si le pones 0 al final hara que se muestre en blanco y negro, si le pones 1 o nada se muestra a color#
cv.imshow('ejemplo',img)
cv.waitKey(0)
cv.destroyAllWindows()