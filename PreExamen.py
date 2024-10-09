import cv2
import numpy as np

imagen = cv2.imread('salida.png')

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Rangos de colores
amarilloBajo = np.array([20, 100, 100], np.uint8)
amarilloAlto = np.array([30, 255, 255], np.uint8)

verdeBajo = np.array([36, 100, 100], np.uint8)
verdeAlto = np.array([70, 255, 255], np.uint8)

rojoBajo1 = np.array([0, 100, 100], np.uint8)
rojoAlto1 = np.array([10, 255, 255], np.uint8)
rojoBajo2 = np.array([160, 100, 100], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)

azulBajo = np.array([100, 100, 100], np.uint8)
azulAlto = np.array([130, 255, 255], np.uint8)