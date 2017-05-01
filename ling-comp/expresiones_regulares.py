# -*- coding: cp1252 -*-
import re


cadena1 = 'casa'
cadena2 = 'casas'
cadena3 = 'pasa'


print 'Ejemplo 1 (COINCIDENCIAS):'
if re.match(cadena1, cadena2): # Significa que no es None
    print('cadena1 y cadena2 son coincidentes')
else:
    print('cadena1 y cadena2 no son coincidentes')

if re.match(cadena1, cadena3) != None:
    print('cadena1 y cadena3 son coincidentes')
else:
    print('cadena1 y cadena3 no son coincidentes')

print
print '--------------------------------------'
print
print 'Ejemplo 2 (CAR�CTER COMOD�N):'
if re.match('.asa', cadena2):
    print('cadena2 contiene "asa" y un car�cter comod�n delante')
else:
    print('cadena2 no contiene "asa" y un car�cter comod�n delante')

if re.match('.asa', cadena3):
    print('cadena3 contiene "asa" y un car�cter comod�n delante')
else:
    print('cadena3 no contiene "asa" y un car�cter comod�n delante')

print
print '--------------------------------------'
print
print 'Ejemplo 3 (CAR�CTER ESPECIAL):'

extension = '\.jpg'
if re.match(extension, '.jpg'):
    print('El archivo es una imagen jpg')


print
print '--------------------------------------'
print
print('Ejemplo 3 (DISTINTAS ALTERNATIVAS):')

extensiones = ['jpg', 'png', 'gif', 'mp3', 'doc']

for tipoarchivo in extensiones:
    if re.match('jpg|png|gif|bmp', tipoarchivo):
        print('La extensi�n ', tipoarchivo, 'se corresponde con una imagen')
    else:
        print('La extensi�n ', tipoarchivo, 'no se corresponde con una imagen')

print
print '--------------------------------------'
print
print 'Ejemplo 4 (GRUPOS AISLADOS):'

palabras = ['careta', 'carpeta', 'colita', 'cateta', 'cocreta', 'caleta', 'caseta']
for termino in palabras:
    if re.match('ca(..|...)ta', termino):
        print(termino)  # careta , carpeta, cateta, caleta, caseta
print
maspalabras = ['masa', 'mata', 'mar', 'mana','cama', 'marea']
for termino in maspalabras:
    if re.match('ma(s|m|n)a', termino):
        print(termino)  # masa, mana


print
print '--------------------------------------'
print
print 'Ejemplo 5 (RANGOS):'
codigos = ['se1', 'se9', 'ma2', 'se:','se.', 
           'se2', 'hu2', 'se3', 'sea', 'sec']

for elemento in codigos:
    if re.match('se[0-5]', elemento):  # el 3er car�cter puede ser n� de 0-5
        print(elemento)
print
for elemento in codigos:
    if re.match('se[0-5a-z]', elemento):  # n� de 0 a 5 y letra de a a z
        print(elemento)
print
for elemento in codigos:
    if re.match('se[.:]', elemento):  # el tercer car�cter puede ser . � :
        print(elemento)
print
for elemento in codigos:
    if re.match('se[^0-2]', elemento):  # debe comenzar por n� de 0 a 2 
        print(elemento)
print

print 'Caracteres predefinidos:'
'''
\d  Cualquier car�cter que sea d�gito
\D  Cualquier car�cter que no sea d�gito
\w  Cualquier car�cter alfanum�rico
\W  Cualquier car�cter no alfanum�rico
\s  Espacio en blanco
\S  Cualquier car�cter que no sea espacio
'''
for elemento in codigos:
    if re.match('se\d', elemento):  # el 3er car�cter debe ser n�mero
        print(elemento)

print
print 'Caracteres que permiten repeticiones:'
'''
+  El car�cter de la izquierda aparecer� una o varias veces
*  El car�cter de la izquierda aparecer� cero o m�s veces
?  El car�cter de la izquierda aparecer� cero o una vez
{}  Indica el n�mero de veces que debe aparecer el car�cter de la izquierda:

{3} 3 veces; {1,4} de 1 a 4; {,3} de 0 a 3; {2,} dos o m�s veces
'''
codigos = ['aaa111', 'aab11', 'aaa1111', 'aaz1', 'aaa'] 

for elemento in codigos:
    if re.match('aa[a-z]1{2,}', elemento):
        print(elemento)  # aaa111 , aab11, aaa1111
print
for elemento in codigos:
    if re.match('a+1+', elemento):
        print(elemento)  # aaa111 , aaa1111 


print
print '--------------------------------------'
print
print 'Ejemplo 6 (M�TODO group()):'
'''
El m�todo group del objeto mo devuelve la cadena encontrada o produce excepci�n
'''

mo = re.match('ftp://.+\com', 'ftp://ovh.com')
print(mo.group())  # ftp://ovh.com 

print
'''
Con los par�ntesis acotamos los grupos:
'''
mo = re.match('ftp://(.+)\com', 'ftp://ovh.com')
print(mo.group(0))  # ftp://ovh.com 
print(mo.group(1))  # ovh. 
print(mo.groups())  # ('ovh.',). 

print
print '--------------------------------------'
print
print 'Ejemplo 7 (FUNCI�N search()):'
'''
La funci�n search es como match pero busca coincidencias de un patr�n
en una cadena de textoy dichas coincidencias pueden aparecer en cualquier lugar.
Su formato es: search(patr�n, cadena, [flag]) 
'''

palabras = ['paniaguado', 'ag�ita', 'aguador', 
            'paraguas', 'agua'] 

for elemento in palabras:
    if re.search('agua', elemento):
        print(elemento) # paniaguado, aguador, paraguas, agua
print
print 'Coincidencias al comienzo y al final:'

'''
Busca una subcadena al ^ COMIENZO o al $ FINAL de una cadena:
'''
lista_url = ['http://www.aaa.es',
             'ftp://www.aaa.es',
             'http://www.bbb.es']
for elemento in lista_url:
    if re.search('^ftp://', elemento):
        print(elemento)  # ftp://www.aaa.es
        
lista_dom = ['.com', '.es']
for elemento in lista_dom:
    if re.search('es$', elemento):
        print(elemento)  # .es

print
print '--------------------------------------'
print
print 'Ejemplo 8 (M�TODOS start() y end()):'
'''
El m�todo start() devuelve la posici�n inicial
y el m�todo end() la final, si la subcadena est� en la cadena.
'''

mo1 = re.search('agua', 'paraguas')
print(mo1.start())  # devuelve 3
print(mo1.end())  # devuelve 7

print
print '--------------------------------------'
print
print 'Ejemplo 9 (FUNCI�N findall()):'
'''
La funci�n findall() devuelve una lista con las subcadenas
que cumplen el patr�n en una cadena.
El formato que utiliza es: findall(patr�n, cadena, [flag])
'''
cadena = 'tengo una yama que yama se llama'
lista = re.findall('..ama', cadena)
print(lista)  # [' yama', ' yama', 'llama']

print
print '--------------------------------------'
print
print 'Ejemplo 10 (FUNCI�N finditer()):'
'''
La funci�n finditer() permite usar un iterador
para recorrer las subcadenas que cumplen el patr�n.
El resultado son tuplas con las posiciones de las subcadenas.

span() Return a tuple containing the (start, end) positions of the match
'''
cadena = 'tengo una yama que yama se llama'
iterador = re.finditer('ama', cadena)
for encontrado in iterador:
    print(encontrado.span())  # (11, 14) , (20, 23) , (29, 32)


print
print '--------------------------------------'
print
print 'Ejemplo 11 (FUNCI�N compile()):'
'''
La funci�n compile() se utiliza para compilar una expresi�n regular,
devolviendo un objeto especial llamado RegexObject.
La compilaci�n es un paso previo que conlleva la evaluaci�n
del patr�n que indiquemos en la funci�n; que despu�s utilizaremos con
las funciones split(), sub(), subn() y otras.  
'''

print('La funci�n sub() con compilaci�n:')

clave = "asdb92z$"

# \D se refiere a cualquier car�cter que no es n�mero 
patron = re.compile("\D")   

# Se sustituyen los caracteres encontrados por "0"
nueva_clave = patron.sub("0", clave)

print(nueva_clave)  # 00009200

# Para motrar el tipo de objeto de "patron":
print(type(patron))

# Otra forma de expresarlo:
nueva_clave = re.compile("\D").sub("0", clave)

# Otros ejemplos:
oracion = 'la norma es la norma'
patron = re.compile('norma') 
print(patron.sub('ley', oracion))  # la ley es la ley

patron = re.compile('la') 
print(patron.sub('LA', oracion, count=1))
# LA norma es la norma

print
print('La funci�n subn() con compilaci�n:')
'''
La funci�n subn() es como sub() pero devuelve una tupla con dos valores:
el primero contiene la cadena resultado despu�s de aplicar las sustituciones
y en el segundo el n�mero de sustituciones realizadas.

En el siguiente ejemplo en vez de utilizar el patr�n "\D" se emplea "\d"
que se refiere a todos los caracteres num�ricos. Dicho patr�n se
utilizar� para sustituir todos los caracteres num�ricospor el caracter "x".
'''
clave = "asdb92z$"
patron = re.compile("\d")
tupla_resultado = patron.subn("x", clave)
print(tupla_resultado[0])   # asdbxxz$
print(tupla_resultado[1])  # 2
print

print 'La funci�n split() con compilaci�n:'
'''
La funci�n split() divide una cadena en subcadenas:
split(cadena, [maxsplit=0]) 
'''
meses = 'ene+feb+mar+abr+may+jun'

patron = re.compile('\+')
print(patron.split(meses))
# ['ene', 'feb', 'mar', 'abr', 'may', 'jun']

patron = re.compile('\+')
print(patron.split(meses, maxsplit=1))  
# ['ene', 'feb+mar+abr+may+jun']


print
print
print('--------------------------------------')
print('--------------------------------------')
print 
print('Bonus track (CLASE DE REEMPLAZO DE CADENAS):')

def my_strtr(cadena, reemplazo):   # reemplazo es un diccionario 
    """Reemplazo m�ltiple de cadenas en Python."""
    import re
    regex = re.compile("(%s)" % "|".join(map(re.escape, reemplazo.keys())))
    return regex.sub(lambda x: str(reemplazo[x.string[x.start() :x.end()]]), cadena)


reemplazo = {'rojo': 'verde', 'sangre': 'esperanza'}
print(my_strtr('El rojo es el color de la sangre', reemplazo))
print

class MyStr(str):
    def strtr(self, reemplazo):
        """Reemplazo m�ltiple de cadenas en Python."""
        import re
        regex = re.compile("(%s)" % "|".join(map(re.escape, reemplazo.keys())))
        return regex.sub(lambda x: str(reemplazo[x.string[x.start() :x.end()]]), self)

c = "El verde es el color de la esperanza"
cadena = MyStr(c)
print(cadena.strtr({'verde' : 'rojo', 'esperanza' : 'sangre'}))
