import numpy as np
import cv2

# Función para cargar y pixelar una imagen
def pixelar_imagen(imagen_path, tamaño_pixel):
    # sec carga la imagen
    imagen = cv2.imread(imagen_path)

    if imagen is None:
        print("Error al cargar la imagen. Verifica la ruta del archivo.")
        return

    # Obtenemos las dimensiones de la imagen original
    original_h, original_w = imagen.shape[:2]

    # Reducimos la imagen para crear el efecto pixelado
    nueva_h = original_h // tamaño_pixel
    nueva_w = original_w // tamaño_pixel
    
    # Redimensionamos la imagen a un tamaño pequeño (pixel art)
    imagen_pequeña = cv2.resize(imagen, (nueva_w, nueva_h), interpolation=cv2.INTER_LINEAR)

    # Escalamos nuevamente la imagen al tamaño original, pero pixelada
    imagen_pixelada = cv2.resize(imagen_pequeña, (original_w, original_h), interpolation=cv2.INTER_NEAREST)

    # Mostramos la imagen original y la pixelada
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Pixelada', imagen_pixelada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Guardamos la imagen pixelada
    cv2.imwrite('imagen_pixelada.png', imagen_pixelada)

# Tamaño de píxel para el efecto (cuanto más grande, más pixelada se vera la imagen)
tamaño_pixel = 12

# Llamamos a la función con la ruta de la imagen subida
pixelar_imagen('ganon.jpg', tamaño_pixel)
