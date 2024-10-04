import cv2
import numpy as np
#esta bugeado el npc
# Tamaño de la ventana
ancho, alto = 250, 200

# Crear una ventana negra
fondo = np.zeros((alto, ancho, 3), dtype=np.uint8)

# Parámetros de la pelota
radio_pelota = 20
posicion_x_pelota = np.random.randint(radio_pelota, ancho - radio_pelota)
posicion_y_pelota = np.random.randint(radio_pelota, alto - radio_pelota)
velocidad_x_pelota = 2
velocidad_y_pelota = 2
color_pelota = (0, 255, 0)  # Color verde

# Parámetros del personaje (cubo)
ancho_personaje, alto_personaje = 30, 30
posicion_x_personaje = np.random.randint(ancho_personaje, ancho - ancho_personaje)
posicion_y_personaje = np.random.randint(alto_personaje, alto - alto_personaje)
velocidad_x_personaje = np.random.choice([-5, 5])  # Velocidades aleatorias iniciales
velocidad_y_personaje = np.random.choice([-5, 5])
color_personaje = (255, 0, 0)  # Color rojo

# Función para cambiar la dirección del cubo cuando se detecta colisión
def cambiar_direccion_si_colision(pos_x_pelota, pos_y_pelota, pos_x_personaje, pos_y_personaje, vx_personaje, vy_personaje):
    distancia_x = pos_x_pelota - pos_x_personaje
    distancia_y = pos_y_pelota - pos_y_personaje
    distancia = np.sqrt(distancia_x**2 + distancia_y**2)

    # Si están demasiado cerca (por ejemplo, dentro de 50 píxeles), cambia de dirección
    if distancia < 50:
        # Invertir la dirección del cubo aleatoriamente
        vx_personaje = np.random.choice([-5, 5])
        vy_personaje = np.random.choice([-5, 5])

    return vx_personaje, vy_personaje

while True:
    # Crear un fondo negro
    fondo = np.zeros((alto, ancho, 3), dtype=np.uint8)

    # Dibujar la pelota
    cv2.circle(fondo, (posicion_x_pelota, posicion_y_pelota), radio_pelota, color_pelota, -1)

    # Dibujar el personaje (cubo)
    cv2.rectangle(fondo, (posicion_x_personaje, posicion_y_personaje),
                  (posicion_x_personaje + ancho_personaje, posicion_y_personaje + alto_personaje), color_personaje, -1)

    # Actualizar la posición de la pelota
    posicion_x_pelota += velocidad_x_pelota
    posicion_y_pelota += velocidad_y_pelota

    # Verificar colisiones de la pelota con las paredes
    if posicion_x_pelota - radio_pelota <= 0 or posicion_x_pelota + radio_pelota >= ancho:
        velocidad_x_pelota = -velocidad_x_pelota
    if posicion_y_pelota - radio_pelota <= 0 or posicion_y_pelota + radio_pelota >= alto:
        velocidad_y_pelota = -velocidad_y_pelota

    # Actualizar la posición del personaje (cubo)
    posicion_x_personaje += velocidad_x_personaje
    posicion_y_personaje += velocidad_y_personaje

    # Verificar colisiones del personaje con las paredes
    if posicion_x_personaje <= 0 or posicion_x_personaje + ancho_personaje >= ancho:
        velocidad_x_personaje = -velocidad_x_personaje
    if posicion_y_personaje <= 0 or posicion_y_personaje + alto_personaje >= alto:
        velocidad_y_personaje = -velocidad_y_personaje

    # Cambiar la dirección del personaje si está cerca de la pelota
    velocidad_x_personaje, velocidad_y_personaje = cambiar_direccion_si_colision(posicion_x_pelota, posicion_y_pelota,
                                                                                 posicion_x_personaje, posicion_y_personaje,
                                                                                 velocidad_x_personaje, velocidad_y_personaje)

    # Mostrar la imagen
    cv2.imshow('Pelota y personaje', fondo)

    # Salir con la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Cerrar la ventana
cv2.destroyAllWindows()
