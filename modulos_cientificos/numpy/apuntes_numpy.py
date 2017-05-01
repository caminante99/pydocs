# -*- coding: cp1252 -*-

import numpy as np

array = np.arange(10)
#print array

''' Consulta de informaci�n '''
#print type(array)
print array.ndim # Consultamos el n�mero de dimensiones -> 1
print array.shape  # Consultamos la dimensi�n -> (10,)
print array.size   # Consultamos la dimensi�n -> 10
print array.dtype   # Tipo de elementos del array -> dtype('int64')
print array.itemsize   # tama�o en bytes -> 8
print

''' Creaci�n de arrays '''
print np.array([1, 2, 3]) # De forma manual
print np.zeros((3,4))      # Creamos un array nulo de 3 filas y 4 columnas
print np.ones(9)     #  Creamos un array unitario de 1 fila y 9 columnas
print np.empty((2,3))     # Creamos un array sin entradas de  2x3.
print np.arange( 10, 30, 5 )  # Array con inicio en 10 final en 30 y paso de 5
print np.linspace( 0, 2, 9 )       # Array de 9 elementos de 0 a 2
X, Y = np.meshgrid([1,2,3], [4,5,6,7]) # Generamos una matriz de coordenadas

# Si construimos un array con diferentes tipos de datos:
np.array([1, 2, 3.0])
# numpy convierte todos los datos en el tipo de datos con m�s informaci�n,
# en este caso crear�a una array float64

# Si queremos forzar el tipo del array
a = np.array([1, 2, 3], dtype=float)

# Convertir array de un tipo a otro:
a.astype(int)

# ----------------------------------------------------------

''' Indexaci�n de arrays '''

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
    ])


a[0] # [1, 2, 3] -> Obtener la primera fila

a[0][0] # 1 -> Obtener el primer elemento de la primera fila
a[0, 0] # 1 -> as� tambien se puede

a[0:2, 1:3] # Obtener elementos por filas, columnas

a[0, 1:3:2] # Coger s�lo los elementos de las columnas pares
a[0, ::2]   # Coger s�lo los elementos de las columnas pares ([:] significa todos)

#-----------------------------------------------
''' Vectores '''

np.linspace(0, 1, num=10) # Vector con rango del 0 al 1 con 10 elementos

np.logspace(0, 3)   # Saldr�a un vector de 50 elementos del 1 al 1000
# el 3 en este caso es 10**3. Podemos a�adir otra base a�adiendo base=5
