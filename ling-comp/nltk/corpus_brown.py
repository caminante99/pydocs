# -*- coding: cp1252 -*-

'''El Corpus de Brown fue el primer corpus electr�nico de millones
de palabras del ingl�s, creado en 1961 en la Universidad de Brown.

Este corpus contiene texto de 500 fuentes, y las fuentes han sido
categorizadas por g�nero, tales como noticias, editorial, etc.
Aqu� hay un ejemplo de cada g�nero (para una lista completa,
ver http://icame.uib.no/brown/bcm-los.html). '''

'''
A16	ca16	news	        Chicago Tribune: Society Reportage
B02	cb02	editorial	Christian Science Monitor: Editorials
C17	cc17	reviews	        Time Magazine: Reviews
D12	cd12	religion	Underwood: Probing the Ethics of Realtors
E36	ce36	hobbies	        Norling: Renting a Car in Europe
F25	cf25	lore	        Boroff: Jewish Teenage Culture
G22	cg22	belles_lettres	Reiner: Coping with Runaway Technology
H15	ch15	government	US Office of Civil and Defence Mobilization: The Family Fallout Shelter
'''

''' Para importar el corpus brown en nltk, teclear lo siguiente: '''
from nltk.corpus import brown

''' Podemos acceder al corpus como una lista de palabras,
o una lista de oraciones (donde cada oraci�n es en s� misma una
lista de palabras). Opcionalmente podemos especificar categor�as
o archivos espec�ficos para leer: '''

brown.categories()

brown.words(categories='science_fiction')

brown.sents(categories=['news', 'editorial', 'reviews'])

''' El Corpus Brown es un recurso conveniente para estudiar
las diferencias sistem�ticas entre g�neros, una especie de
investigaci�n en ling��stica conocida como estil�stica.

Comparemos los g�neros en su uso de los verbos modales.
El primer paso es producir los conteos para un g�nero particular. '''

import nltk
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ':', fdist[m])
    
'''A continuaci�n, necesitamos obtener recuentos para cada g�nero
de inter�s. Utilizaremos el soporte de NLTK para las distribuciones
de frecuencia condicional. '''

cfd = nltk.ConditionalFreqDist(
            (genre, word)
            for genre in brown.categories()
            for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)
'''
                 can could  may might must will
           news   93   86   66   38   50  389
       religion   82   59   78   12   54   71
        hobbies  268   58  131   22   83  264
science_fiction   16   49    4   12    8   16
        romance   74  193   11   51   45   43
          humor   16   30    8    8    9   13
'''

''' Esta es una peque�a introducci�n al corpus brown. Para aprender a
clasificar textos con mayor profundidad en nltk ver:
http://www.nltk.org/book/ch06.html#chap-data-intensive
'''
