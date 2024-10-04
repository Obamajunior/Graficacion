import cv2
import numpy as np

def aplicar_operadores(imagen_path):
    imagen = cv2.imread(imagen_path)

    if imagen is None:
        print("Error al cargar la imagen.")
        return

    # Operador 1: Inversión de colores (Negativo)
    imagen_negativo = cv2.bitwise_not(imagen)

    # Operador 2: Escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Operador 3: Aumentar el brillo
    matriz_brillo = np.ones(imagen.shape, dtype="uint8") * 50
    imagen_brillo = cv2.add(imagen, matriz_brillo)

    # Operador 4: Disminuir el brillo
    imagen_bajo_brillo = cv2.subtract(imagen, matriz_brillo)

    # Operador 5: Aumento de contraste usando Histogram Equalization (solo en escala de grises)
    imagen_contraste = cv2.equalizeHist(imagen_gris)

    # Mostrar todas las imágenes
    cv2.imshow("Imagen Original", imagen)
    cv2.imshow("Imagen Negativo", imagen_negativo)
    cv2.imshow("Imagen en Escala de Grises", imagen_gris)
    cv2.imshow("Imagen con Brillo Aumentado", imagen_brillo)
    cv2.imshow("Imagen con Brillo Disminuido", imagen_bajo_brillo)
    cv2.imshow("Imagen con Contraste Aumentado", imagen_contraste)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Llamar a la función con la ruta de la imagen
aplicar_operadores('ganon.jpg')
