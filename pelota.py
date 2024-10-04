import cv2
import numpy as np

# Tamaño de la ventana
ancho, alto = 300, 250

# Crear una ventana negra
fondo = np.zeros((alto, ancho, 3), dtype=np.uint8)

# Parámetros de la pelota
radio = 20
posicion_x = np.random.randint(radio, ancho - radio)  # Posición inicial aleatoria en X
posicion_y = np.random.randint(radio, alto - radio)   # Posición inicial aleatoria en Y
velocidad_x = 5  # Velocidad en X
velocidad_y = 5  # Velocidad en Y
color_pelota = (90, 200, 210)  # Color

while True:
    # Crear un fondo negro para que la pelota se "mueva"
    fondo = np.zeros((alto, ancho, 3), dtype=np.uint8)

    # Dibujar la pelota en la nueva posición
    cv2.circle(fondo, (posicion_x, posicion_y), radio, color_pelota, -1)

    # Actualizar la posición de la pelota
    posicion_x += velocidad_x
    posicion_y += velocidad_y

    # Verificar colisiones con las paredes
    if posicion_x - radio <= 0 or posicion_x + radio >= ancho:
        velocidad_x = -velocidad_x  # Cambiar la dirección en X
    if posicion_y - radio <= 0 or posicion_y + radio >= alto:
        velocidad_y = -velocidad_y  # Cambiar la dirección en Y

    # Mostrar la imagen
    cv2.imshow('Pelota rebotando', fondo)

    # Salir con la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Cerrar la ventana
cv2.destroyAllWindows()
