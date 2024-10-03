import cv2
import numpy as np

def resaltar_color(imagen_hsv, color_bajo, color_alto):
    mascara = cv2.inRange(imagen_hsv, color_bajo, color_alto)
    return mascara

imagen = cv2.imread('estrellita.jpg', 1)
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Rango de colores en HSV ajustados
rangos_colores = {
    'rojo': [(np.array([0, 50, 50]), np.array([10, 255, 255])), (np.array([170, 50, 50]), np.array([180, 255, 255]))],
    'azul': [(np.array([90, 50, 50]), np.array([130, 255, 255]))],
    'verde': [(np.array([35, 50, 50]), np.array([85, 255, 255]))],
    'amarillo': [(np.array([20, 100, 100]), np.array([30, 255, 255]))],
    'magenta': [(np.array([145, 50, 50]), np.array([175, 255, 255]))],  
}

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imagen_gris_bgr = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)

# Resaltar cada color y abrir una ventana por cada uno
for color, rangos in rangos_colores.items():
    mascara_total = np.zeros(imagen_hsv.shape[:2], dtype=np.uint8)
    for (bajo, alto) in rangos:
        mascara = resaltar_color(imagen_hsv, bajo, alto)
        mascara_total = cv2.add(mascara_total, mascara)
    
    resultado = np.where(mascara_total[:, :, None] == 255, imagen, imagen_gris_bgr)
    cv2.imshow(f'Color {color}', resultado)

# aqui abrimos la cámara y resaltar los colores en tiempo real
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gris_bgr = cv2.cvtColor(frame_gris, cv2.COLOR_GRAY2BGR)
    
    # Crear una máscara combinada para todos los colores
    mascara_total_cam = np.zeros(frame_hsv.shape[:2], dtype=np.uint8)
    for rangos in rangos_colores.values():
        for (bajo, alto) in rangos:
            mascara = resaltar_color(frame_hsv, bajo, alto)
            mascara_total_cam = cv2.add(mascara_total_cam, mascara)
    
    resultado_cam = np.where(mascara_total_cam[:, :, None] == 255, frame, frame_gris_bgr)
    
    # Mostrar la imagen de la cámara con los colores resaltados
    cv2.imshow('Camara - Colores resaltados', resultado_cam)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
