# -*- coding: cp1252 -*-

'''hashlib pertenece a la librer�a est�ndar y permite realizar
cifrados directamente desde Python con los algoritmos SHA1, SHA224,
SHA256, SHA384, SHA512 y MD5. Este �ltimo tambi�n cuenta con un m�dulo
obsoleto que permite su implementaci�n llamado md5. '''

import hashlib

''' La funci�n new() retorna un nuevo objeto de la clase hash
implementando la funci�n (hash) especificada. '''

h = hashlib.new('hash', 'cadena')

''' En donde el primer par�metro debe ser una cadena como �sha1�, �md5�,
�sha224� y el segundo cualquier tipo de cadena que querramos cifrar.

Un ejemplo para cifrar con SHA1 e imprimir el resultado en pantalla: '''

h = hashlib.new("sha1", "www.recursospython.com - Recursos Python")
print(h.digest())

'''La funci�n digest retorna la cadena cifrada en binario.
Para obtenerla en hexadecimal, existe la funci�n hexdigest(). '''

print h.hexdigest()

'''Las siguientes funciones son m�s r�pidas que new()
y realizan exactamente lo mismo:'''

# md5(), sha1(), sha224(), sha256(), sha384(), y sha512()

''' La tupla algorithms provee los nombres de los algoritmos
soportados por el m�dulo, por lo que con el siguiente c�digo
podemos probar la eficacia de cada una de las funciones: '''

for algorithm in hashlib.algorithms:
    print algorithm
    h = hashlib.new(algorithm)
    h.update("www.recursospython.com - Recursos Python")
    print h.hexdigest()

#--------------------------------------------------------

# Para cosas m�s complejas pycrypto
