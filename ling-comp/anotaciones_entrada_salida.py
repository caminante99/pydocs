# -*- encode: utf-8 -*-

import re

# Abrimos el html, lo leemos y lo cerramos
with open('Caballero.html', 'r', encoding='utf8') as f:
    texto = f.read()

''' La anterior es la forma más limpia de abrir archivos.
Con ella el archivo se cierra automáticamente después de leerlo.
Si te lía mucho puedes usar la típica, que necesita una línea más:

f = open('Caballero.html', 'r', encoding='utf8')
texto = f.read()
f.close()
'''

# Cogemos todo lo que hay dentro de las etiquetas <strong></strong>
strong = re.compile(r'<strong>(.+?)</strong>', re.DOTALL)
# DOTALL significa puntotodo, el punto en python es cualquier
# caracter excepto salto de línea, con DOTALL incluye a los saltos

texto = strong.findall(texto)

# Creamos una lista vacía donde meteremos todas las anotaciones limpias
nuevo_texto = []
for frase in texto:
    # Eliminamos las etiquetas html, saltos de línea, tabuladores...
    frase = re.sub(r'<.+?>|\n|\t|&nbsp;', '', frase)
    # Corregimos las tildes y las eñes
    frase = re.sub(r'&aacute;', 'á', frase)
    frase = re.sub(r'&oacute;', 'ó', frase)
    frase = re.sub(r'&eacute;', 'é', frase)
    frase = re.sub(r'&iacute;', 'í', frase)
    frase = re.sub(r'&Iacute;', 'Í', frase)
    frase = re.sub(r'&Eacute;', 'É', frase)
    frase = re.sub(r'&ntilde;', 'ñ', frase)
    frase = re.sub(r'&Ntilde;', 'Ñ', frase)
    # Corregimos los espacios que aparecen más de una vez seguida
    frase = re.sub(r'\s{2,}', ' ', frase)
    # Corregimos los espacios al principio de la anotación
    frase = re.sub(r'^\s+', '', frase)
    # Añadimos a la lista la frase en limpio. Recuerda:
    nuevo_texto.append(frase) # lista_donde_quiero_meter.append(lo_que_quiero_meter)

# Creamos una lista con las palabras que indican que una anotación es
# de entrada o de salida
ent_y_sal = ['Salen', 'Vanse', 'Vase', 'Sale',
             'Salgan', 'sale', 'entrar', 'salga',
             'véngase']

# Creamos una lista que contendrá el resultado final
resultado = []

# Recorremos la lista que antes hemos limpiado
for anotacion in nuevo_texto:
    # Por cada anotación, recorremos la lista de palabras
    # que indican entrada o salida:
    for palabra in ent_y_sal:
        # Si la palabra está en la anotación
        if palabra in anotacion:
            resultado.append(anotacion)
'''
En este caso en las anotaciones no hay dos palabras de entrada
salida que se repitan en la misma anotación. Si así fuera,
tendríamos frases repetidas en el resultado. Para eliminar
las repeticiones usaríamos:
resultado = list(set(resultado))
'''
print(resultado)


