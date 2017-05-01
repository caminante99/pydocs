# Nombres personajes

# Así es como se haría de forma pro

import re

# Abrimos el html, lo leemos y lo cerramos
with open('Caballero.html','r', encoding='utf8') as f:
    texto = f.read()

# Substituimos las tildes y los símbolos raros si los hubiera

subs = {'&Eacute;': 'É', '&ordm;': 'º'}
''' Creo un diccionario con el patrón a sustituir y la cadena
por la que lo quiero reemplazar '''

''' Itero por el diccionario con subs.items() que lo que hace
es darme por un lado el patron y por otro lado la cadena
por la que lo quiero reemplazar '''

for patron, repl in subs.items(): # Para cada par de elementos del dict
    p = re.compile(patron) # Compilamos su patrón
    texto = re.sub(p, repl, texto) # y lo substituimos

# Compilamos diciendo:
''' Coge un grupo de caracteres de 1 ó más que se encuentre
dentro de las etiquetas html y no contenga < ''' 
p = re.compile(r"<td valign=\"top\" width=\"21%\">([^<]+)</td>")

''' Hacemos un conjunto con el resultado. Lo que hace set()
es crear una tupla de elementos no repetidos. Una tupla
es muy parecido a una lista pero tiene diferentes características
y se escribe asi: tupla = (elemento_1, elemento_2) '''

''' De esa tupla volvemos a hacer una lista: '''
lista = list(set(p.findall(texto)))

print(lista)
