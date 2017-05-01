# -*- coding: cp1252 -*-
import re

''' EXAMEN DE JUNIO '''

''' Ejercicio nº 1: '''
''' Sea la cadena de caracteres:'''
texto = "BP has agreed to sell\n it's petrochemicals unit for $5.1bn."

''' Indicar qué caracteres concretos de dicha cadena son identificados por
las siguientes expresiones:

.a..
s*l
$

'''

patron = re.compile(r'.a..')
coincidencias = patron.findall(texto)

print 'Expresión 1:' 
for c in coincidencias:
    print(c)
print

patron = re.compile(r's*l')
coincidencias = patron.findall(texto)

print 'Expresión 2:'
for c in coincidencias:
    print(c)
print

patron = re.compile(r'$')
coincidencias = patron.findall(texto)

print 'Expresión 3:'
for c in coincidencias:
    print(c)
print

''' Explicaciones:
Expresión 1: dará como resultado 'has ' (contando el espacio en blanco)
y 'cals' debido a que el . hace referencia a cualquier carácter.

Expresión 2: encontrará 3 veces la 'l' debido a que la * equivale a {0,}
es decir, la s de delante del asterisco debe encontrarse 0 ó más veces
al lado de una l. Esta expresión está realizada para confundirte
y que pongas la palabra 'sell' ó 'sel'. ¡No caer en la trampa!

Expresión 3: La $ es un etacaracter para indicar final de línea.
No encontrará nada, está hecho para que te confundas con el $ del precio.
'''

print '------------------------------------------'
print
''' Ejercicio nº 2 '''
''' Construir una expresión regular que identifique todas las ocurrencias
del artículo definido inglés 'the' en cualquier texto. '''

texto = """The pattern is very easy if you knows the method"""

patron = re.compile(r'[T|t]he')
coincidencias = patron.findall(texto)

for c in coincidencias:
    print(c)
print
print  '------------------------------------------'
print

''' Ejercicio nº 8 '''
''' Escribe código que elimine los espacios en blanco al principio
y al final de una cadena, y normalice los espacios en blanco entre
las palabras para que sólo sean de un caracter en blanco '''

'''a) Haz esta tarea usando split() y join() '''

# El método join() actúa indicandole un separador compilado:
texto = ['papel', 'botella', 'envase']
separador = ' '
print separador.join(texto) # -> papel botella envase
print

''' Sabiendo esto procedamos a resolver el ejercicio '''
texto = '   Esta     es  la cadena      que vamos  a utilizar '
lista = re.split(r'\s+', texto)
lista.pop()
lista.pop(0)
separador = ' '
resultado = separador.join(lista)
print(resultado)
print 

'''b) Haz esta tarea usando substituciones de expresiones regulares '''
''' El método re.sub() funciona así:
re.sub(pattern, repl, string, count=0, flags=0)
'''
ejemplo = 'How are you?'
print(re.sub(r'you', 'u', ejemplo)) # -> How are u?
print

''' Resolvemos '''
procesando = re.sub(r'\s{2,}', ' ', texto)
resultado = re.sub(r'^\s+|\s+$', '', procesando)
print(resultado)
