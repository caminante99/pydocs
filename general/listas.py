# -*- coding: cp1252 -*-

frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']

frutas.count('manzana') # 2

frutas.index('banana') # 3
frutas.index('banana', 4)  # Busca la pr�xima banana empezando en posici�n 4 -> 6

frutas.reverse() # Invierte el orden de los elementos

frutas.append('uva') # A�ade un elemento al final

mas_frutas = ['mel�n', 'sand�a', 'melocoton']
frutas.extend(mas_frutas) # Extiende la lista agreg�ndole los �tems de la lista dada

frutas.sort() # Ordena alfab�ticamente

set(frutas) # Eliminar elementos repetidos (se convierte en una tupla)

frutas.pop() # Elimina el �ltimo elemento de la lista
frutas.pop(1) # Elimina el segundo elemento de la lista

''' Eliminar elementos por su valor: '''
frutas.remove('mel�n')

''' Usando listas como pilas '''
# �ltimo en entrar -> list.append()
# Primero en salir -> list.pop()

#--------------------------------------------------------------

''' Usando listas como colas '''
'''Primero en entrar, primero en salir. Las listas no son eficientes
para este prop�sito. Agregar y sacar del final de la lista es r�pido,
pero insertar o sacar del comienzo de una lista es lento
(porque todos los otros elementos tienen que ser desplazados por uno).
Para implementar una cola, us� collections.deque el cual fue dise�ado
para agregar y sacar de ambas puntas de forma r�pida.
'''

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")         # llega Terry
queue.append("Graham")        # llega Graham
queue.popleft()               # el primero en llegar ahora se va

#----------------------------------------------------------------

''' CONJUNTOS '''
''' Un conjunto es una colecci�n no ordenada y sin elementos repetidos.
Los usos b�sicos de �stos incluyen verificaci�n de pertenencia y
eliminaci�n de entradas duplicadas. Tambi�n soportan operaciones
matem�ticas como la uni�n, intersecci�n, diferencia, y diferencia sim�trica.

Las llaves o la funci�n set() pueden usarse para crear conjuntos.
Nota que para crear un conjunto vac�o ten�s que usar set(),
no {}; esto �ltimo crea un diccionario vac�o.
'''

canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana'}
# print canasta -> {'pera', 'manzana', 'banana', 'naranja'}

'naranja' in canasta         # verificaci�n de pertenencia r�pida

a = set('abracadabra')
b = set('alacazam')

a           # letras �nicas en a
a - b       # letras en a pero no en b
a | b       # letras en a o en b
a & b       # letras en a y en b
a ^ b       # letras en a o b pero no en ambos

