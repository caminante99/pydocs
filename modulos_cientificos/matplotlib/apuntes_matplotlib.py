# -*- coding: cp1252 -*-

import matplotlib.pyplot as plt

''' Iniciar el modo interactivo '''
''' Para mostrar imágenes primero hay que iniciar el modo interactivo '''
plt.ion()

''' Terminar el modo interactivo '''
plt.ioff()

''' Mostrar figuras '''
plt.imshow()

''' Pausar para redibujar figuras '''
''' Después de dibujar algo pyplot necesita ser pausado temporalmente
para actualizarse a sí mismo, si no no funcionará en el IDLE.

Hay que introducir esto después de redibujar: '''
plt.pause(0.0001)

''' Evitar que se cuelgue al cerrar en el IDLE '''
''' Introducir esto al final: '''
plt.show(block=True)

#-------------------------------------------------------

''' Remover los ejes y los números de tamaño alrededor de la imagen '''
plt.axis('off')

''' Abrir imágenes '''
#plt.imread(ruta)

#-------------------------------------------------------

''' Creación de figuras '''
'''
num = numeración # si num = None, las figuras se numeran automáticamente.
figsize = w, h # tuplas en pulgadas. Tamaño de la figura
dpi = Resolución de la imagen en puntos por pulgada.
facecolor = Color del rectángulo de la figura.
edgecolor = Color del perímetro de la figura.
frameon = Si es falso, elimina el marco de la figura.

num = 1
figsize = (600, 600)
dpi = 8
facecolor = 'r'
edgecolor = 'k'
frameon = True
figura = plt.figure(num, figsize, dpi, facecolor, edgecolor, frameon)
'''

''' Varias gráficas en una figura '''
'''
subplot(numRows, numCols, plotNum)

numRows = Número de filas
numCols = Número de columnas
plotNum = Número de gráfica


plot(x, y, linestyle, linewidth, marker)
x = Abcisas.
y = Ordenadas. Tanto x como y pueden ser abcisas tuplas, listas o arrays. La única condición es que el tamaño de ambas debe ser el mismo ya que en caso contrario python nos devolverá un fallo de tipo dimesión. También se puede hacer una gráfica sin especificar la coordenada x.
linestyle = color y tipo de dibujar la gráfica. Por ejemplo ‘k- -‘
linewidth = ancho de línea.
marker = Marcador.
