# -*- coding: cp1252 -*-

cadena = 'hola esto es una cadena'

''' Primera letra en mayúscula '''
print cadena.capitalize()

''' Convertir cadena a minúsculas '''
print cadena.lower()

''' Convertir cadena a mayúsculas '''
print cadena.upper()

''' Convertir mayúsculas a minúsculas y viceversa '''
cadena = 'Hola Mundo'
print cadena.swapcase()
print

#---------------------------------------------------

''' MÉTODOS DE VALIDACIÓN '''

''' Saber si una cadena es mayúscula, minúscula o espacio '''
print cadena.upper().isupper()
print cadena.lower().islower()
print cadena.isspace()

''' Saber si una cadena es alfanumérica '''
# (Si tiene un espacio retorna False)
print cadena.isalnum()

''' Saber si una cadena es alfabética '''
# (Si tiene un número retorna False)
print cadena.isalpha()

''' Saber si una cadena es numérica '''
# (Si tiene un punto retorna False)
print cadena.isdigit()

''' Extraer los números de una cadena sin regex '''
print "".join([x for x in "123jajaja345" if x.isdigit()]) 

print

#----------------------------------------------------

''' Centrar una cadena '''
print cadena.center(50, "=")

''' Alinear a la izquierda y a la derecha '''
print cadena.ljust(50, '-')
print cadena.rjust(50, '-')
print

#----------------------------------------------------

'''MÉTODOS DE BÚSQUEDA '''
cadena = 'Esta es la cadena'

''' Contar cantidad de apariciones de una subcadena '''
print cadena.count("a") # 4

''' Buscar una subcadena dentro de una cadena '''
'''Retorna: un entero representando la posición donde inicia
la subcadena dentro de cadena. Si no la encuentra, retorna -1.'''
print cadena.find('de')
print cadena.find('de', 0, 10)
print

#----------------------------------------------------

''' MÉTODOS DE SUSTITUCIÓN '''

''' Dar formato a una cadena '''
cadena = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}"
print cadena.format(100, 21, 121)

cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}" 
print cadena.format(bruto=100, iva=21, neto=121) 

''' Reemplazar texto '''
buscar = "nombre apellido" 
reemplazar_por = "Juan Pérez" 
print "Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por)

''' Eliminar caracteres a la derecha y a la izquierda '''
cadena = "   www.siglo25.com   " 
print cadena.strip() # www.siglo25.com

cadena = "www.siglo25.com" 
print cadena.lstrip("w." ) # siglo25.com
print cadena.rstrip("m." ) # siglo25.co
print

#-----------------------------------------------------

''' MÉTODOS DE UNIÓN Y DIVISIÓN '''

''' Unir una cadena de forma iterativa '''
formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")") 
numero = "275" 
numero_factura = numero.join(formato_numero_factura) 
print numero_factura # Nº 0000-0275-0000 (ID: 275)

''' Partir una cadena en tres partes, utilizando un separador '''
tupla = "http://www.siglo25.com".partition("www.") 
print tupla # ('http://', 'www.', 'siglo25.com')

''' Partir una cadena en varias partes, utilizando un separador '''
keywords = "python, guia, curso, tutorial".split(", ") 
print keywords # ['python', 'guia', 'curso', 'tutorial']

''' Partir una cadena en líneas '''
texto = "Linea 1\nLinea 2\nLinea 3" 
print texto.splitlines() # ['Linea 1', 'Linea 2', 'Linea 3']
