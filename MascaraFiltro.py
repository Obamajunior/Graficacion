import cv2
import numpy as np

# Cargar la máscara que deseas agregar (asegúrate de que sea PNG con transparencia)
mascara = cv2.imread('hat.PNG', cv2.IMREAD_UNCHANGED)  # Cargar PNG con transparencia

# Verificar si la imagen tiene un canal alfa
if mascara.shape[2] != 4:
    print("Error: La imagen no tiene canal alfa.")
    exit()

# Cargar el clasificador preentrenado de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# Capturar video desde la cámara
video = cv2.VideoCapture(0)

# Definir un desplazamiento para mover la máscara
desplazamiento_x = 0  # Ajustar según sea necesario
desplazamiento_y = -180  # Ajustar según sea necesario

# Factor de escala para hacer la máscara más grande (por ejemplo, 2 para el doble de tamaño)
factor_escala = 2

while True:
    # Leer cada frame del video
    ret, frame = video.read()

    if not ret:
        break

    # Convertir el frame a escala de grises
    frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar los rostros en el frame
    rostros = face_cascade.detectMultiScale(frame_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Procesar cada rostro detectado
    for (x, y, w, h) in rostros:
        # Redimensionar la máscara para que sea el doble del tamaño del rostro
        w_mascarilla = int(w * factor_escala)
        h_mascarilla = int(h * factor_escala)
        mascara_redimensionada = cv2.resize(mascara, (w_mascarilla, h_mascarilla))

        # Separar los canales de la máscara: color y alfa (transparencia)
        mascara_rgb = mascara_redimensionada[:, :, :3]
        mascara_alpha = mascara_redimensionada[:, :, 3]

        # Asegurarse de que la máscara alfa sea de tipo uint8
        mascara_alpha = cv2.convertScaleAbs(mascara_alpha)

        # Aplicar el desplazamiento y centrar la máscara sobre el rostro
        x_nuevo = x - (w_mascarilla - w) // 2 + desplazamiento_x
        y_nuevo = y - (h_mascarilla - h) // 2 + desplazamiento_y

        # Evitar que la máscara salga del borde de la imagen
        if x_nuevo < 0: x_nuevo = 0
        if y_nuevo < 0: y_nuevo = 0
        if x_nuevo + w_mascarilla > frame.shape[1]: x_nuevo = frame.shape[1] - w_mascarilla
        if y_nuevo + h_mascarilla > frame.shape[0]: y_nuevo = frame.shape[0] - h_mascarilla

        # Crear una región de interés (ROI) en el frame donde colocaremos la máscara
        roi = frame[y_nuevo:y_nuevo+h_mascarilla, x_nuevo:x_nuevo+w_mascarilla]

        # Asegurarse de que la ROI y la máscara tengan el mismo tamaño
        if roi.shape[:2] == mascara_alpha.shape[:2]:
            # Invertir la máscara alfa para obtener la parte del rostro donde se aplicará la máscara
            mascara_alpha_inv = cv2.bitwise_not(mascara_alpha)

            # Enmascarar la región del rostro en la imagen original
            fondo = cv2.bitwise_and(roi, roi, mask=mascara_alpha_inv)

            # Enmascarar la máscara RGB
            mascara_fg = cv2.bitwise_and(mascara_rgb, mascara_rgb, mask=mascara_alpha)

            # Combinar el fondo (parte del rostro sin máscara) y la parte con la máscara
            resultado = cv2.add(fondo, mascara_fg)

            # Reemplazar la región del rostro con la imagen combinada
            frame[y_nuevo:y_nuevo+h_mascarilla, x_nuevo:x_nuevo+w_mascarilla] = resultado

        else:
            print("Error: El tamaño de la ROI no coincide con la máscara.")

    # Mostrar el frame con la máscara aplicada
    cv2.imshow('Video con mascara', frame)

    # Presionar 'q' para salir del loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar las ventanas
video.release()
cv2.destroyAllWindows()
