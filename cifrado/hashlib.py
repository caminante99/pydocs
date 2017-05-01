# -*- coding: cp1252 -*-

'''hashlib pertenece a la librería estándar y permite realizar
cifrados directamente desde Python con los algoritmos SHA1, SHA224,
SHA256, SHA384, SHA512 y MD5. Este último también cuenta con un módulo
obsoleto que permite su implementación llamado md5. '''

import hashlib

''' La función new() retorna un nuevo objeto de la clase hash
implementando la función (hash) especificada. '''

h = hashlib.new('hash', 'cadena')

''' En donde el primer parámetro debe ser una cadena como “sha1”, “md5”,
“sha224” y el segundo cualquier tipo de cadena que querramos cifrar.

Un ejemplo para cifrar con SHA1 e imprimir el resultado en pantalla: '''

h = hashlib.new("sha1", "www.recursospython.com - Recursos Python")
print(h.digest())

'''La función digest retorna la cadena cifrada en binario.
Para obtenerla en hexadecimal, existe la función hexdigest(). '''

print h.hexdigest()

'''Las siguientes funciones son más rápidas que new()
y realizan exactamente lo mismo:'''

# md5(), sha1(), sha224(), sha256(), sha384(), y sha512()

''' La tupla algorithms provee los nombres de los algoritmos
soportados por el módulo, por lo que con el siguiente código
podemos probar la eficacia de cada una de las funciones: '''

for algorithm in hashlib.algorithms:
    print algorithm
    h = hashlib.new(algorithm)
    h.update("www.recursospython.com - Recursos Python")
    print h.hexdigest()

#--------------------------------------------------------

# Para cosas más complejas pycrypto
