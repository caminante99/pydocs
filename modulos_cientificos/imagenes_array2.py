# -*- coding: cp1252 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

plt.ion()

# Creamos un array de 256 x 256 lleno de ceros
im = np.zeros((256, 256))

# Si yo le digo lo siguiente:
#im[0:10, 0:100] = 1
''' Se colorea de rojo en el programa un rectángulo:
- Desde el pixel 0 hasta el 10 en el eje y
- Desde el pixel 0 hasta el 100 en el eje x

Por lo tanto im[y, x] = 1 ¡así que cuidado! '''

# Si yo le digo lo siguiente:
im[64:-64, 64:-64] = 1
''' Se colorea un cuadrado en el medio ya que 64*4 = 256 '''

# Rotación en contra de las agujas del reloj
im = ndimage.rotate(im, 15, mode='constant')

# Desenfoque gausiano
im = ndimage.gaussian_filter(im, 8)

#plt.imshow(im) # Los 0 se ven en azul y los 1 en rojo

''' Detección de bordes '''
''' Usamos un operador gradiente Sobel para encontrar altas
variaciones de intensidad '''
sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)



plt.axis('off')
plt.pause(0.0001)
plt.show(block=True)
