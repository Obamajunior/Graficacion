import numpy as np
import cv2

# esto es para generar un punto en una órbita elíptica/circular
def generar_punto_orbita(a, b, t, centro):
    x = int(a * np.cos(t) + centro[0])  # Eje X de la órbita
    y = int(b * np.sin(t) + centro[1])  # Eje Y de la órbita
    return (x, y)

# Dimensiones de la imagen
img_width, img_height = 800, 800

# Esto crea una imagen en negro
imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

# Parámetros para el sistema solar
sol_pos = (400, 400)  # Esto es el Sol en el centro de la imagen
sol_radio = 30  # Tamaño del Sol

# Definimos los parámetros para los planetas (semieje mayor, semieje menor, velocidad angular)
planetas = [
    {"color": (255, 0, 0), "a": 70, "b": 70, "velocidad": 0.05, "radio": 10},   # Planeta 1
    {"color": (0, 255, 0), "a": 120, "b": 120, "velocidad": 0.03, "radio": 15},  # Planeta 2
    {"color": (0, 0, 255), "a": 180, "b": 180, "velocidad": 0.02, "radio": 20},  # Planeta 3
    {"color": (255, 255, 0), "a": 250, "b": 250, "velocidad": 0.01, "radio": 25} # Planeta 4
]

# Creamos los valores del parámetro t para cada planeta
t_planetas = [0] * len(planetas)

# El bucle de animación
while True:
    # Crear otra imagen en negro
    imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)
    
    # esto dibujara el Sol
    cv2.circle(imagen, sol_pos, sol_radio, (0, 255, 255), -1)  # Sol amarillo
    
    # esto dibujara cada planeta en su órbita
    for i, planeta in enumerate(planetas):
        # esto generara la posición del planeta en su órbita
        punto_orbita = generar_punto_orbita(planeta["a"], planeta["b"], t_planetas[i], sol_pos)
        
        # Dibujar la órbita del planeta (opcional)
        cv2.ellipse(imagen, sol_pos, (planeta["a"], planeta["b"]), 0, 0, 360, (255, 255, 255), 1)
        
        # Dibujar el planeta
        cv2.circle(imagen, punto_orbita, planeta["radio"], planeta["color"], -1)
        
        # Actualizar el ángulo t del planeta (movimiento)
        t_planetas[i] += planeta["velocidad"]
    
    cv2.imshow('Sistema Solar', imagen)
    
    # Esto controla la velocidad de los planetas/animacion (importante, en milisegundos)
    if cv2.waitKey(20) & 0xFF == 27:  # esto de aqui hace que al presionar 'Esc' se salga de la ventana
        break

cv2.destroyAllWindows()
