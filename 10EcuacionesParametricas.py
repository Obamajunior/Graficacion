import numpy as np
import matplotlib.pyplot as plt

# Función para graficar ecuaciones paramétricas
def graficar_parametricas(t, x_func, y_func, title, color):
    x = x_func(t)
    y = y_func(t)
    plt.plot(x, y, color=color)
    plt.title(title)
    plt.axis('equal')

# Parámetro común t
t = np.linspace(0, 2 * np.pi, 500)

# Creamos una figura grande para todas las gráficas
plt.figure(figsize=(15, 15))

# Ecuación 1: Círculo
plt.subplot(4, 3, 1)
graficar_parametricas(t, lambda t: np.cos(t), lambda t: np.sin(t), "Círculo", 'blue')

# Ecuación 2: Elipse
plt.subplot(4, 3, 2)
graficar_parametricas(t, lambda t: 2 * np.cos(t), lambda t: np.sin(t), "Elipse", 'green')

# Ecuación 3: Hipocicloide
plt.subplot(4, 3, 3)
graficar_parametricas(t, lambda t: 2 * np.cos(t) + np.cos(5 * t), lambda t: 2 * np.sin(t) + np.sin(5 * t), "Hipocicloide", 'purple')

# Ecuación 4: Espiral logarítmica
plt.subplot(4, 3, 4)
graficar_parametricas(t, lambda t: np.exp(0.1 * t) * np.cos(t), lambda t: np.exp(0.1 * t) * np.sin(t), "Espiral Logarítmica", 'orange')

# Ecuación 5: Lemniscata
plt.subplot(4, 3, 5)
graficar_parametricas(t, lambda t: np.cos(t) / (1 + np.sin(t) ** 2), lambda t: np.cos(t) * np.sin(t) / (1 + np.sin(t) ** 2), "Lemniscata", 'red')

# Ecuación 6: Roseta de 4 pétalos
plt.subplot(4, 3, 6)
graficar_parametricas(t, lambda t: np.cos(2 * t), lambda t: np.sin(2 * t), "Roseta de 4 pétalos", 'cyan')

# Ecuación 7: Cardioide
plt.subplot(4, 3, 7)
graficar_parametricas(t, lambda t: 1 - np.cos(t), lambda t: np.sin(t) * (1 - np.cos(t)), "Cardioide", 'magenta')

# Ecuación 8: Asteroide
plt.subplot(4, 3, 8)
graficar_parametricas(t, lambda t: np.cos(t) ** 3, lambda t: np.sin(t) ** 3, "Asteroide", 'brown')

# Ecuación 9: Hipérbola
plt.subplot(4, 3, 9)
graficar_parametricas(t, lambda t: np.sinh(t), lambda t: np.cosh(t), "Hipérbola", 'yellow')

# Ecuación 10: Espiral de Arquímedes
t_archimedes = np.linspace(0, 4 * np.pi, 500)
plt.subplot(4, 3, 10)
graficar_parametricas(t_archimedes, lambda t: t * np.cos(t), lambda t: t * np.sin(t), "Espiral de Arquímedes", 'black')

# Ajustar el espacio entre los gráficos
plt.tight_layout()

# Mostramos todas las gráficas
plt.show()
