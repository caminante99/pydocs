import numpy as np
import matplotlib.pyplot as plt

# Definimos la función (esta eleva al cuadrado la inversa de un array)
def f(x):
    return np.exp(-x ** 2)

# Creamos el eje X
x = np.linspace(-1, 5, num=1000) # Cuanto más números más calidad tendrá la línea

# La graficamos en verde con su leyenda
plt.plot(x, f(x), 'green', label='Función f(x)') # En lugar de 'green' también acepta 'g'

# Si queremos que pinte cada uno de los puntos representados, en lugar de una línea:
plt.plot(x, f(x), 'o', label='Función f(x)')
# Ahora en rojo
plt.plot(x, f(x), 'or', label='Función f(x)')

plt.xlabel('Eje X') # Añadimos un nombre al eje X
plt.ylabel('f(x)') # Añadimos un nombre al eje Y
plt.legend() # Activamos la leyenda

# Activar o desactivar la rejilla:
plt.grid(True) # ó False

# Cambiar los l�mites de los ejes
plt.set_xlin(-2, 6)
plt.set_ylin(-2, 2)

#-------------------------------------------------------

''' Distribuci�n de puntos (an�lisis estad�stico) '''
x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y)
