# -*- coding: cp1252 -*-
import re


print 'Formas de extraer informaci�n de una biblioteca:'
print 'Ejemplo 1 (EXTRAER M�DULOS):'
print dir(re)
print
print '------------------------'
print

print 'Ejemplo 2 (EXTRAER INFORMACI�N):'
print help(re.search)
print '--------'
print re.search.__doc__

print
print '-----------------------------------------------'
print

print 'Formas de extraer informaci�n de un dato:'
print 'Ejemplo 1 (SABER QU� TIPO DE DATO ES):'

print type(87)
print type('ab')
print type(3.1415)
print type(re.search)
print type((1, 2, 3))

lista = ['pepe', 'maria', 'chocolate']
print type(lista)
diccionario = {'fruta': 5.60, 'tenedor': 'de pl�stico'}
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
Funci�n assert:
'''
def division(dividendo, divisor):
    """ Calculo de la divisi�n
    Pre: Recibe dos n�meros, divisor debe ser distinto de 0.
    Post: Devuelve un n�mero real, con el cociente de ambos.
    """
    assert divisor != 0, "El divisor no puede ser 0"
    return dividendo / ( divisor * 1.0 )


'''
assert est� pensado para ser usado en la etapa de desarrollo.
Un programa terminado nunca deber�a dejar de funcionar
por este tipo de errores.
'''

#----------------

'''
Funci�n del
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
La funci�n exec() permite ejecutar c�digo Python
contenido en una cadena o en un archivo.
Si el c�digo no cumple con las reglas del lenguaje
producir� una excepci�n.  

En el siguiente ejemplo se ejecutan varias cadenas
que contienen instrucciones de Python.

exec('secreto = input("Introducir clave secreta: ")')
exec('if secreto == "1234": print("�Eureka!")')
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
Esta es una funci�n lambda que consigue el mismo efecto
que la funci�n anterior. Advierta aqu� la sintaxis abreviada:
la lista de argumentos no est� entre par�ntesis, y falta
la palabra reservada return (est� impl�cita, ya que la funci�n
entera debe ser una �nica expresi�n). Igualmente, la funci�n no
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
hubi�ramos instanciado una lista: mycont = [0,1,2,3,4] o
mycont = range(0,5). Pero de hecho lo que ocurre es muy diferente.

El objecto mycont es un iterador, cuando se lo recorre
(en este caso en el for, o explicitamente con next())
va tirando secuencialmente sus elementos.
La diferencia con una lista es que esos elementos
no est�n almacenados, sino que se generan "on the fly".
'''
