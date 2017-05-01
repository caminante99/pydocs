# -*- coding: cp1252 -*-

import matplotlib.pyplot as plt

''' Iniciar el modo interactivo '''
''' Para mostrar im�genes primero hay que iniciar el modo interactivo '''
plt.ion()

''' Terminar el modo interactivo '''
plt.ioff()

''' Mostrar figuras '''
plt.imshow()

''' Pausar para redibujar figuras '''
''' Despu�s de dibujar algo pyplot necesita ser pausado temporalmente
para actualizarse a s� mismo, si no no funcionar� en el IDLE.

Hay que introducir esto despu�s de redibujar: '''
plt.pause(0.0001)

''' Evitar que se cuelgue al cerrar en el IDLE '''
''' Introducir esto al final: '''
plt.show(block=True)

#-------------------------------------------------------

''' Remover los ejes y los n�meros de tama�o alrededor de la imagen '''
plt.axis('off')

''' Abrir im�genes '''
#plt.imread(ruta)

#-------------------------------------------------------

''' Creaci�n de figuras '''
'''
num = numeraci�n # si num = None, las figuras se numeran autom�ticamente.
figsize = w, h # tuplas en pulgadas. Tama�o de la figura
dpi = Resoluci�n de la imagen en puntos por pulgada.
facecolor = Color del rect�ngulo de la figura.
edgecolor = Color del per�metro de la figura.
frameon = Si es falso, elimina el marco de la figura.

num = 1
figsize = (600, 600)
dpi = 8
facecolor = 'r'
edgecolor = 'k'
frameon = True
figura = plt.figure(num, figsize, dpi, facecolor, edgecolor, frameon)
'''

''' Varias gr�ficas en una figura '''
'''
subplot(numRows, numCols, plotNum)

numRows = N�mero de filas
numCols = N�mero de columnas
plotNum = N�mero de gr�fica


plot(x, y, linestyle, linewidth, marker)
x = Abcisas.
y = Ordenadas. Tanto x como y pueden ser abcisas tuplas, listas o arrays. La �nica condici�n es que el tama�o de ambas debe ser el mismo ya que en caso contrario python nos devolver� un fallo de tipo dimesi�n. Tambi�n se puede hacer una gr�fica sin especificar la coordenada x.
linestyle = color y tipo de dibujar la gr�fica. Por ejemplo �k- -�
linewidth = ancho de l�nea.
marker = Marcador.
