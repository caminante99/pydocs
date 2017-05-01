import re


with open('Caballero.html','r', encoding='utf8') as f:
    texto = f.read()
    
p = re.compile(r"<td valign=\"top\" width=\"21%\">([^<]+)</td>")

nuevo_texto = p.findall(texto)

personajes = []
for p in nuevo_texto:
    # Substituimos los símbolos º
    p = re.sub(r'&ordm;', 'º', p)
    # Corregimos las tildes y las eñes
    p = re.sub(r'&aacute;', 'á', p)
    p = re.sub(r'&oacute;', 'ó', p)
    p = re.sub(r'&eacute;', 'é', p)
    p = re.sub(r'&iacute;', 'í', p)
    p = re.sub(r'&uacute;', 'ú', p)
    p = re.sub(r'&Iacute;', 'Í', p)
    p = re.sub(r'&Eacute;', 'É', p)
    p = re.sub(r'&ntilde;', 'ñ', p)
    p = re.sub(r'&Ntilde;', 'Ñ', p)
    # Añadimos a la lista el personaje en limpio. Recuerda:
    personajes.append(p) # lista_donde_quiero_meter.append(lo_que_quiero_meter)

#print(personajes)

''' Ahora tenemos que contar las veces que aparece cada personaje.
Hay varias formas de hacerlo, yo primero crearé una lista para cada
personaje. Para ello itero sobre el conjunto de personajes.
Recuerda: un conjunto es una lista de elementos no repetidos'''

''' Creo un diccionario que me facilitará guardar el nombre de cada
personaje relacionado con el número de veces que aparecerá.
Un diccionario es una lista de elementos relacionados de par en par:
contador = {34: 'TELLO', 1: 'LA VOZ', 15: 'LEONOR'}'''

''' En la carpeta docs teneis información para manejar diccionarios '''
apariciones = {}

for p in set(personajes):
    apariciones_personaje = []
    # Ahora voy a meter todas las apariciones de cada personaje en su lista
    for per in personajes:
        # Si el personaje por el que estoy iterando es el mismo al personaje
        # del cual hemos creado la lista, lo inserto en la lista
        if per == p:
            apariciones_personaje.append(per)
    # Imprimimos cada lista de cada personaje (descomentar la siguiente línea)
    #print(apariciones_personaje)
    
    # Imprimimos (descomentar las 2 siguientes líneas):
    #print(p + ' aparece:', len(apariciones_personaje), 'veces')
    #print() # con len(lista) podemos ver el número de elementos de una lista

    # Agregamos al diccionario cada personaje con el número de veces que aparece
    apariciones[len(apariciones_personaje)] = p

#print(apariciones)

''' Creamos un nueva lista donde vamos a meter los personajes
que más aparecen '''

personajes = []

''' Ahora vamos a iterar por todos los elementos del diccionario
5 veces. Por cada vez, vamos a meter en la lista el personaje
que más veces aparezca y lo vamos a quitar del diccionario. '''

# Para iterar un número de veces usamos range(num_veces)
for pasada in range(5):
    numero = 0
    # Para iterar por un diccionario usamos diccionario.items()
    for veces, per in apariciones.items():
        # Guardamos las veces en una variable 'numero'
        if veces > numero:
            # Haciendo esto nos aseguramos que el número
            # será el mayor que haya en el diccionario
            numero = veces
    # Metemos el personaje con el mayor número encontrado
    # Para ello usamos .get que nos da el valor de una clave de un diccionario
    personajes.append(apariciones.get(numero))
    # Borramos ese personaje del diccionario
    del apariciones[numero]

# Ya tenemos los 5 personajes que más veces aparecen (descomentar):
print(personajes)

for p in personajes:
    print(p)
    print()
    # INÉS hay que buscarla con &Eacute; en el texto original por la tilde
    if p == 'INÉS':
        p = 'IN&Eacute;S'
    patron = r'<td valign="top" width="21%">' + p + '(.+?)<td valign="top" width="21%">'
    exp = re.compile(patron)
    intervenciones = exp.findall(texto)
    intervenciones_limpio = []
    for i in intervenciones:
        # Eliminamos las etiquetas html, saltos de línea, tabuladores...
        i = re.sub(r'<.+?>|\t|&nbsp;', ' ', i)
        # Corregimos las tildes y las eñes
        i = re.sub(r'&aacute;', 'á', i)
        # Corregimos las interrogaciones de apertura
        i = re.sub(r'&iquest;', '¿', i)
        # Corregimos las exclamaciones de apertura
        i = re.sub(r'&iexcl;', '¡', i)
        # Eliminamos los dígitos
        i = re.sub(r'\d', '', i)
        # Corregimos tildes y eñes
        i = re.sub(r'&oacute;', 'ó', i)
        i = re.sub(r'&eacute;', 'é', i)
        i = re.sub(r'&iacute;', 'í', i)
        i = re.sub(r'&uacute;', 'ú', i)
        i = re.sub(r'&Iacute;', 'Í', i)
        i = re.sub(r'&Eacute;', 'É', i)
        i = re.sub(r'&ntilde;', 'ñ', i)
        i = re.sub(r'&Ntilde;', 'Ñ', i)
        # Corregimos los espacios que aparecen más de una vez seguida
        i = re.sub(r'\s{2,}', ' ', i)
        # Corregimos los espacios al principio de la anotación
        i = re.sub(r'^\s+', '', i)
        # Añadimos a la lista el personaje en limpio. Recuerda:
        intervenciones_limpio.append(i)
    for i in intervenciones_limpio:
        print(i)
        print()
    print('-------------------------------------------------')
        
''' OS DEJO EL RESTO PARA QUE LO HAGAIS VOSOTROS QUE SI NO NO APRENDEIS '''
