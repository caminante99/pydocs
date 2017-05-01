# -*- coding: cp1252 -*-

frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']

frutas.count('manzana') # 2

frutas.index('banana') # 3
frutas.index('banana', 4)  # Busca la próxima banana empezando en posición 4 -> 6

frutas.reverse() # Invierte el orden de los elementos

frutas.append('uva') # Añade un elemento al final

mas_frutas = ['melón', 'sandía', 'melocoton']
frutas.extend(mas_frutas) # Extiende la lista agregándole los ítems de la lista dada

frutas.sort() # Ordena alfabéticamente

set(frutas) # Eliminar elementos repetidos (se convierte en una tupla)

frutas.pop() # Elimina el último elemento de la lista
frutas.pop(1) # Elimina el segundo elemento de la lista

''' Eliminar elementos por su valor: '''
frutas.remove('melón')

''' Usando listas como pilas '''
# Último en entrar -> list.append()
# Primero en salir -> list.pop()

#--------------------------------------------------------------

''' Usando listas como colas '''
'''Primero en entrar, primero en salir. Las listas no son eficientes
para este propósito. Agregar y sacar del final de la lista es rápido,
pero insertar o sacar del comienzo de una lista es lento
(porque todos los otros elementos tienen que ser desplazados por uno).
Para implementar una cola, usá collections.deque el cual fue diseñado
para agregar y sacar de ambas puntas de forma rápida.
'''

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")         # llega Terry
queue.append("Graham")        # llega Graham
queue.popleft()               # el primero en llegar ahora se va

#----------------------------------------------------------------

''' CONJUNTOS '''
''' Un conjunto es una colección no ordenada y sin elementos repetidos.
Los usos básicos de éstos incluyen verificación de pertenencia y
eliminación de entradas duplicadas. También soportan operaciones
matemáticas como la unión, intersección, diferencia, y diferencia simétrica.

Las llaves o la función set() pueden usarse para crear conjuntos.
Nota que para crear un conjunto vacío tenés que usar set(),
no {}; esto último crea un diccionario vacío.
'''

canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana'}
# print canasta -> {'pera', 'manzana', 'banana', 'naranja'}

'naranja' in canasta         # verificación de pertenencia rápida

a = set('abracadabra')
b = set('alacazam')

a           # letras únicas en a
a - b       # letras en a pero no en b
a | b       # letras en a o en b
a & b       # letras en a y en b
a ^ b       # letras en a o b pero no en ambos

