# -*- coding: cp1252 -*-
import re


print 'Formas de extraer información de una biblioteca:'
print 'Ejemplo 1 (EXTRAER MÓDULOS):'
print dir(re)
print
print '------------------------'
print

print 'Ejemplo 2 (EXTRAER INFORMACIÓN):'
print help(re.search)
print '--------'
print re.search.__doc__

print
print '-----------------------------------------------'
print

print 'Formas de extraer información de un dato:'
print 'Ejemplo 1 (SABER QUÉ TIPO DE DATO ES):'

print type(87)
print type('ab')
print type(3.1415)
print type(re.search)
print type((1, 2, 3))

lista = ['pepe', 'maria', 'chocolate']
print type(lista)
diccionario = {'fruta': 5.60, 'tenedor': 'de plástico'}
print

#--------------------------------------------
def sumar_cadenas(cadenas, meter_espacio=False):
    resultado = ''
    espacio = ' '
    for cadena in cadenas:
        resultado += cadena
        if meter_espacio == True:
            resultado += espacio
    return resultado
    

variable = 'sumar_cadenas(lista)'
print eval(variable)
print 

''' NOMBRES DE VARIABLES NO PERMITIDAS '''
from keyword import iskeyword, kwlist
print kwlist   # Lista parabras reservadas
print iskeyword("exec") 
print 
#---------------

'''
Función assert:
'''
def division(dividendo, divisor):
    """ Calculo de la división
    Pre: Recibe dos números, divisor debe ser distinto de 0.
    Post: Devuelve un número real, con el cociente de ambos.
    """
    assert divisor != 0, "El divisor no puede ser 0"
    return dividendo / ( divisor * 1.0 )


'''
assert está pensado para ser usado en la etapa de desarrollo.
Un programa terminado nunca debería dejar de funcionar
por este tipo de errores.
'''

#----------------

'''
Función del
'''

foo = 'hola'
del foo
#print foo # Salta un NameError: name 'foo' is not defined
'''
Deletion of a name removes the binding of that name from
the local or global namespace. Assigning None to a name
does not remove the binding of the name from the namespace.
'''


'''
# Elimina elementos de listas y diccionarios
del list_item[4]
del dictionary["alpha"]
'''

#-----------------

'''
La función exec() permite ejecutar código Python
contenido en una cadena o en un archivo.
Si el código no cumple con las reglas del lenguaje
producirá una excepción.  

En el siguiente ejemplo se ejecutan varias cadenas
que contienen instrucciones de Python.

exec('secreto = input("Introducir clave secreta: ")')
exec('if secreto == "1234": print("¡Eureka!")')
exec('print("Clave secreta:", secreto)')
'''

#------------------

'''
Funciones lambda
'''
def f(x):
    return x*2
f(3) # 6

g = lambda x: x*2
g(3) # 6

(lambda x: x*2)(3) # 6
'''
Esta es una función lambda que consigue el mismo efecto
que la función anterior. Advierta aquí la sintaxis abreviada:
la lista de argumentos no está entre paréntesis, y falta
la palabra reservada return (está implícita, ya que la función
entera debe ser una única expresión). Igualmente, la función no
tiene nombre, pero puede ser llamada mediante la variable asignada.
'''

#---------------------

'''
El uso de yield
'''
def contador(max):
    n=0
    while n < max:
            yield n
            n=n+1

mycont = contador(5)

for i in mycont:
    print(i)

print(mycont)

'''
El resultado es el mismo que si, en lugar de mycont = contador(5)
hubiéramos instanciado una lista: mycont = [0,1,2,3,4] o
mycont = range(0,5). Pero de hecho lo que ocurre es muy diferente.

El objecto mycont es un iterador, cuando se lo recorre
(en este caso en el for, o explicitamente con next())
va tirando secuencialmente sus elementos.
La diferencia con una lista es que esos elementos
no están almacenados, sino que se generan "on the fly".
'''
