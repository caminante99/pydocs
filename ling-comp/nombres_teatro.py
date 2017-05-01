import re, os

'''á'''
directorio_actual = os.getcwd()
f = open(directorio_actual + '\\' + 'Caballero.html','r', encoding='utf8')
texto = f.read()
f.close()

td = re.compile(r'<td valign="top">.+?</td>', re.DOTALL)

lista = td.findall(texto)
string = ''.join(lista)

html = re.compile(r"<.*?>") 

texto = re.sub(html, '', string)
limpiar = re.compile(r'\s{2,}|\.$')
texto = re.sub(limpiar, '', texto)

enies = re.compile(r'&Ntilde;')
texto = re.sub(enies, 'Ñ', texto)
tabs = re.compile(r'&nbsp;&nbsp;')
texto = re.sub(tabs, ' ', texto)
tilde = re.compile(r'&Eacute;')
texto = re.sub(tilde, 'É', texto)
bruto = texto.split('.')

espacio = re.compile(r'^\s')
lista_final = []
for personaje in bruto:
    personaje = re.sub(espacio, '', personaje)
    lista_final.append(personaje)

print(lista_final)

