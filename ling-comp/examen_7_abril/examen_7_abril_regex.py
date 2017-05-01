# -*- encode: utf-8 -*-

import re

''' 1. Escribir una expresión regular para seleccionar las consonantes
(todas las consonantes y sólo las consonantes) que aparecen antes de una
vocal en un rexto '''

texto = """Este es un texto de prueba con el que vamos a comprobar\n
si hemos hecho bien el ejercicio. Son complicadillos, pero\n
vamos al lío..."""

# Esta expresión es incompleta
exp = re.compile(r'([^aeiou\s\.,])[aeiou]', re.IGNORECASE | re.MULTILINE)
'''Explicación:
Agrupamos para que sólo nos coja la consonante. Para determinar que
es una consonante hay que ser muy explícitos, le decimos que no puede
ser ni una vocal, ni un espacio, ni un punto ni una coma
(podríamos seguir diciéndole que no fuera ni un símbolo de exclamación,
ni una ni un símbolo de paréntesis, las vocales con tildes... y es
un no acabar, así que podemos ser creativos y especificar
sólo las consonantes, como he hecho a continuación.

Luego detrás del grupo ponemos vocal, agregamos IGNORECASE (para que
nos valide sea mayúscula o minúscula y MULTILINE. Para agregar las
dos hay que poner un símbolo | de por medio, está mal si ponemos una coma.
¡Tened mucho cuidado en agregar estos atributos!
'''
# Así está perfecta ¡Sed explícitos y simples!
exp = re.compile(r'([b-df-hj-np-tv-z])[aeiou]', re.IGNORECASE | re.MULTILINE)

print('Ejercicio 1:')
print(exp.findall(texto))
print()

#-----------------------------------------------------

''' 2. Escribir una expresión regular que identifique fechas en formato día,
mes y año, separados por '/' o por '-'. '''

# Debe darnos la primera y las dos últimas
fechas = '22/2-2222, 2-/04-1000, 2-04/1000, 9-4-33'

exp = re.compile(r'\d{1,2}[/|-]\d{1,2}[/|-]\d{1,4}')

print('Ejercicio 2:')
print(exp.findall(fechas))
print()

''' La explicación creo que es bastante explícita:
1 ó 2 dígitos, separador / o -, 1 ó 2 dígitos, separador / o -, de 1 a 4 dígitos
'''

#----------------------------------------------
''' 3. Sea la expresión regular ([def])+=\1 ¿Qué identifica en las cadenas... '''

a = 'def=def'
b = 'def=fed'

exp = re.compile(r'([def])+=\1')

print('Ejercicio 3:')
print(exp.findall(a)) # En la cadena a identifica None
print(exp.findall(b)) # En la cadema b identifica 'f'
print()

''' Explicación:
Aquí seguramente os han fundido. Hay que leer muy bien la expresión y ver
por donde nos la quiere colar. La expresión significa lo siguiente:

def esta entre [] lo que significa que es un grupo de caracteres, no la cadena 'def',
lo que quiere decir que pueden encontrarse d, e, f cualquiera de los tres
También está entre paréntesis, lo que quiere decir que encontrará uno sólo de esos
caracteres, ya que el + (1 ó más veces) está fuera del paréntesis. Esto indica
que el grupo (calquiera de los 3 caracteres) lo encontrará una o más veces.

Y ahora viene la gran trampa... Después del + viene un = que indica que después del
caracter agrupado vendrá el signo igual. Esto nos da la pista: sólo puede ser el
carácter f. Y ahora nos viene el \1 justo después del =, lo que indica que
tiene que volver a encontrarlo JUSTO DESPUÉS del signo =
'''

#----------------------------------------------------

''' 4. Escribir una expresión regular que identifique todas las líneas de un fichero
que contengan una palabra con dos o más ocurrencias consecutivas de la letra 'a',
o bien dos o más ocurrencias consecutivas de la letra 'u'. '''

print('Ejercicio 4:')
texto = """Este es un texto de pruebaa con el que vamos a comprobar\n
si hemos hecho bien el uuultimo ejercicio.\n
Vamos al lío..."""


exp = re.compile('.*u{2,}.*|.*a{2,}.*', re.MULTILINE)

print(exp.findall(texto))
''' Explicación:
Recordad que siempre que tengamos un texto debemos meter re.MULTILINE y tener
en cuenta que irá línea por línea tomando cada línea como una cadena.

Le indicamos al programa que coja todo lo que valla desde el principio hasta
dos veces o más 'u' y lo que vaya detrás. Luego ponemos un | para indicarle
que también coja todo lo que vaya delante y detrás de dos 'a'.

Como no agrupamos nada lo coge todo, incluidas las a y las u.'''


