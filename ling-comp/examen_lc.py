# -*- coding: cp1252 -*-

import re

'''
Ejercicio nº 1:
'''
texto = 'hola alas tengo alup alaa ala8 ALAA ALA8 ALAH aLUp a[]p alu['

patron = re.compile(r"""
        \b 
        [aeiou]{1}
        [a-z]{2}
        [^aeiou \d]{1}
        \b
        """, re.VERBOSE)

patron = re.compile(r'\b[aeiou]{1}[a-z]{2}[^aeiou\d]{1}\b')

# \b Comienzo de palabra
# [aeiou]{1} Una vocal
# [a-z]{2} Dos letras minúsculas
# [^aeiou 0-9]{1} No puede acabar ni en número ni en vocal
# # \b Final de palabra

coincidencias = patron.findall(texto)
for c in coincidencias:
    print(c)
    
print 

'''
Ejercicio nº 2:
'''

arch = open('fichero.txt', 'r')
texto = arch.read()
'''
texto1 = """Identifica todas las líneas de un fichero\n
que empiecen y acaben con la misma palabra\n
\n
argos tendre ser bola palabras al azar argos\n
\n
expulsar seeora corriente esta no acaba en la misma\n
\n
esta si acabara en la misma la en acabara si esta\n ya\n"""
'''

#patron = re.compile(r'^(\b\w+).*\b\1$', re.MULTILINE)
patron = re.compile(r'^(?=([A-Za-z]+)).*\1$', re.MULTILINE)

coincidencias = patron.findall(texto)
for c in coincidencias:
    print(c)
print 

'''
Ejercicio nº 3: Palabras repetidas dos o más veces
'''

palabras = 'hola adios adios quetal quetal quetal'

p = re.compile(r'(\b\w+\b)\s+\1')

coincidencias = patron.findall(palabras)
for c in coincidencias:
    print(c)

'''
Ejercicio nº 4: Palabras repetidas dos o más veces
'''

texto = 'Paris in the the the the spring'

#print(p.match(texto).group()) # None
print(p.search(texto).group()) # the the
print(p.search(texto).span())


