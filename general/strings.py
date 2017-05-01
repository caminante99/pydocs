# -*- coding: cp1252 -*-

cadena = 'hola esto es una cadena'

''' Primera letra en may�scula '''
print cadena.capitalize()

''' Convertir cadena a min�sculas '''
print cadena.lower()

''' Convertir cadena a may�sculas '''
print cadena.upper()

''' Convertir may�sculas a min�sculas y viceversa '''
cadena = 'Hola Mundo'
print cadena.swapcase()
print

#---------------------------------------------------

''' M�TODOS DE VALIDACI�N '''

''' Saber si una cadena es may�scula, min�scula o espacio '''
print cadena.upper().isupper()
print cadena.lower().islower()
print cadena.isspace()

''' Saber si una cadena es alfanum�rica '''
# (Si tiene un espacio retorna False)
print cadena.isalnum()

''' Saber si una cadena es alfab�tica '''
# (Si tiene un n�mero retorna False)
print cadena.isalpha()

''' Saber si una cadena es num�rica '''
# (Si tiene un punto retorna False)
print cadena.isdigit()

''' Extraer los n�meros de una cadena sin regex '''
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

'''M�TODOS DE B�SQUEDA '''
cadena = 'Esta es la cadena'

''' Contar cantidad de apariciones de una subcadena '''
print cadena.count("a") # 4

''' Buscar una subcadena dentro de una cadena '''
'''Retorna: un entero representando la posici�n donde inicia
la subcadena dentro de cadena. Si no la encuentra, retorna -1.'''
print cadena.find('de')
print cadena.find('de', 0, 10)
print

#----------------------------------------------------

''' M�TODOS DE SUSTITUCI�N '''

''' Dar formato a una cadena '''
cadena = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}"
print cadena.format(100, 21, 121)

cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}" 
print cadena.format(bruto=100, iva=21, neto=121) 

''' Reemplazar texto '''
buscar = "nombre apellido" 
reemplazar_por = "Juan P�rez" 
print "Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por)

''' Eliminar caracteres a la derecha y a la izquierda '''
cadena = "   www.siglo25.com   " 
print cadena.strip() # www.siglo25.com

cadena = "www.siglo25.com" 
print cadena.lstrip("w." ) # siglo25.com
print cadena.rstrip("m." ) # siglo25.co
print

#-----------------------------------------------------

''' M�TODOS DE UNI�N Y DIVISI�N '''

''' Unir una cadena de forma iterativa '''
formato_numero_factura = ("N� 0000-0", "-0000 (ID: ", ")") 
numero = "275" 
numero_factura = numero.join(formato_numero_factura) 
print numero_factura # N� 0000-0275-0000 (ID: 275)

''' Partir una cadena en tres partes, utilizando un separador '''
tupla = "http://www.siglo25.com".partition("www.") 
print tupla # ('http://', 'www.', 'siglo25.com')

''' Partir una cadena en varias partes, utilizando un separador '''
keywords = "python, guia, curso, tutorial".split(", ") 
print keywords # ['python', 'guia', 'curso', 'tutorial']

''' Partir una cadena en l�neas '''
texto = "Linea 1\nLinea 2\nLinea 3" 
print texto.splitlines() # ['Linea 1', 'Linea 2', 'Linea 3']
