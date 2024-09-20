import cv2 as cv
import numpy as np

img = np.ones((600, 900, 3), dtype=np.uint8) * 50

# Personaje 1 (héroe) - usando formas simples
cv.circle(img, (250, 300), 40, (0, 255, 0), -1)
cv.line(img, (250, 340), (250, 440), (0, 255, 0), 8)
cv.line(img, (250, 360), (320, 370), (0, 255, 0), 6)
cv.rectangle(img, (320, 360), (350, 370), (255, 255, 255), -1) 
cv.line(img, (250, 360), (200, 400), (0, 255, 0), 6)
cv.line(img, (250, 440), (270, 510), (0, 255, 0), 6)
cv.line(img, (250, 440), (230, 510), (0, 255, 0), 6)

# Personaje 2
cv.circle(img, (650, 300), 40, (0, 0, 255), -1)  
cv.line(img, (650, 340), (650, 440), (0, 0, 255), 8)
cv.line(img, (650, 360), (580, 370), (0, 0, 255), 6)
cv.rectangle(img, (550, 360), (580, 370), (100, 100, 100), -1) 
cv.line(img, (650, 360), (700, 400), (0, 0, 255), 6)
cv.line(img, (650, 440), (670, 510), (0, 0, 255), 6)
cv.line(img, (650, 440), (630, 510), (0, 0, 255), 6)

#ambiente
cv.rectangle(img, (0, 500), (900, 600), (30, 30, 30), -1)  
cv.circle(img, (450, 200), 100, (80, 80, 80), -1) 

#rayos de luz
pts = np.array([[900, 0], [600, 0], [900, 300]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], (120, 120, 120))  

#mostrar la imagen
cv.imshow('Resident Evil 4 segun', img)
cv.waitKey(0)
cv.destroyAllWindows()
