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

# Para la exclamación de apertura (¡) el html usa &iexcl;
# debido a que los caracteres españoles no los soportan todas las webs
exclamaciones = re.compile(r'&iexcl;.+?!', re.DOTALL)

texto = exclamaciones.findall(texto)

nuevo_texto = []
for personaje in texto:
    # Eliminamos las etiquetas html, saltos de línea, tabuladores...
    frase = re.sub(r'<.+?>|\n|\t|&nbsp;', '', frase)
    # Substituimos las exclamaciones de apertura
    frase = re.sub(r'&iexcl;', '¡', frase)
    # Corregimos las tildes y las eñes
    frase = re.sub(r'&aacute;', 'á', frase)
    frase = re.sub(r'&oacute;', 'ó', frase)
    frase = re.sub(r'&eacute;', 'é', frase)
    frase = re.sub(r'&iacute;', 'í', frase)
    frase = re.sub(r'&uacute;', 'ú', frase)
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

print(nuevo_texto)
