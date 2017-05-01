# -*- coding: cp1252 -*-

from scipy import ndimage
import numpy as np
import Image # m�dulo PIL

''' Escribiendo un array a un archivo '''
from scipy import misc
l = misc.ascent() # Imagen de ejemplo dentro de scipy
misc.imsave('img/ascent.png', l)

ascent = misc.imread('img/ascent.png')
type(ascent) # <type 'numpy.ndarray'>
ascent.shape #(512, 512)
ascent.dtype # uint8

''' Abriendo archivos raw '''
'''El formato de im�genes raw es un formato de archivo digital
de im�genes que contiene la totalidad de los datos de la imagen
tal y como ha sido captada por el sensor digital de la c�mara. '''

l.tofile('img/ascent.raw')
ascent_from_raw = np.fromfile('img/ascent.png', dtype=np.int64)
ascent_from_raw.shape # (16601,)
ascent_from_raw = (512, 512)
#import os
#os.remove('img/ascent.raw')

''' Necesitas saber la forma y el dtype (tipo de dato)
de la imagen (de qu� forma separar los bytes de datos).

Para conjuntos de datos de gran tama�o se puede usar np.memmap,
que sirve para mapear en memoria estos datos (los datos son
le�dos desde el archivo, pero no son cargados en la memoria)'''

ascent_memmap = np.memmap('img/ascent.raw', dtype=np.int64, shape=(512, 512))

''' Trabajando en una lista de archivos de im�genes: '''
''' Crea una lista de 10 im�genes de ruido al azar '''
for i in range(10):
    im = np.random.random_integers(0, 255, 10000).reshape((100, 100))
    misc.imsave('img/random_%02d.png' % i, im)
    
from glob import glob
lista_de_archivos = glob('img/random*.png')

#--------------------------------------------------------

''' Mostrando im�genes '''
''' Se puede usar matplotlib e imshow para mostrar
una imagen dentro de una figura matplotlib: '''

l = misc.ascent()
import matplotlib.pyplot as plt
'''
plt.ion()

plt.imshow(l, cmap=plt.cm.gray, vmin=30, vmax=200)
# Podemos incrementar el contraste ajustando los valores m�nimos y m�ximos
plt.axis('off')

# Podemos dibujar las l�neas de contorno
#plt.contour(l, [60, 211])

plt.pause(0.0001)
plt.show(block=True)
'''
#-------------------------------------------------------

''' Manipulaciones b�sicas de im�genes '''
im = misc.ascent()
im[0, 40] # 86

# Mostrar recorte como array
im[10:13, 20:23]

# Pintar una l�nea horizontal blanca
im[100:120] = 255
lx, ly = im.shape
X,Y = np.ogrid[0:lx, 0:ly]
mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/4

# Enmascarar
im[mask] = 0

# L�nea diagonal desde (0, 0) a (400, 400)
im[range(400), range(400)] = 255

