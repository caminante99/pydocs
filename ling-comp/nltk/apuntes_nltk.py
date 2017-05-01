# -*- coding: cp1252 -*-

import nltk

''' Para instalar: pip install -U nltk '''

''' Por otro lado, además de la librería también es necesario
instalar una serie de ficheros y diccionarios con patrones
para varios tipos de estructuras gramaticales llamados “corporas”,
dichos ficheros se instalan de forma independiente por medio de un
gestor de descargas que puede iniciarse utilizando el modulo nltk '''
#nltk.download()

''' Invocando a “download” se abre una ventana en la que se pueden
gestionar todos los ficheros “corpora” en diferentes categorías.
Si es la primera vez que se utiliza nltk, se realizará la descarga
de dichos ficheros. '''

''' Los corpus principales que se suelen utilizar en el procesamiento
de texto son conocidos como “gutenberg”, el cual incluye una selección
de 18 textos del proyecto Gutenberg (http://www.gutenberg.org/)
y contiene más de 1.5 millones de palabras.
Para consultar los textos de gutenberg incluidos en el corpus de NLTK,
se pueden ejecutar las siguientes instrucciones. '''

from nltk.corpus import gutenberg as gut
#print(gut.fileids())

''' Los textos de la biblioteca hay que insertarlos como unicode '''
texto = u'shakespeare-hamlet.txt'

''' Contar número de palabras en un texto '''
num_tokens = len(gut.words(texto))
''' Token: Se trata de la unidad más simple de procesamiento
y representa una palabra en el texto. '''

''' Contar número de caracteres '''
num_caracteres = len(gut.raw(texto))

''' Contar número de sentencias '''
num_sents = len(gut.sents(texto))
'''Una sentencia es de punto a punto en lenguas occidentales.
En otras lenguas es más difícil determinar qué es una sentencia.'''


''' INSERTAR UN TEXTO PROPIO '''
from nltk.corpus import PlaintextCorpusReader

#wordlists = PlaintextCorpusReader('/home/adastra/Escritorio/textos', '.*')
#wordlists.words('prueba.txt')

''' Tokenizar sentencias y palabras'''
from nltk import sent_tokenize, word_tokenize, pos_tag
text = """Machine learning is the science of getting computers to act
without being explicitly programmed. In the past decade, machine learning
has given us self-driving cars, practical speech recognition, effective
web search, and a vastly improved understanding of the human genome.
Machine learning is so pervasive today that you probably use it dozens of
times a day without knowing it. Many researchers also think it is the best
way to make progress towards human-level AI. In this class, you will learn
about the most effective machine learning techniques, and gain practice
implementing them and getting them to work for yourself."""

sents = sent_tokenize(text)
tokens = word_tokenize(text)

''' Clasificación de tokens '''
tagged_tokens = pos_tag(tokens)

''' Consultar información sobre los tags '''
#nltk.help.upenn_tagset('JJ')

''' Tokenizar en español '''
texto = """El análisis automático de sentimiento es un paso más
en el intento de traducir las emociones humanas a datos.
Pero la espontaneidad y la inmediatez de la opinión en medios
sociales hacen que estos sentimientos sean más auténticos y
preserven su contenido emocional."""

spanish_tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
spanish_tokenizer.tokenize(texto)


''' API PARA LENGUAJE NATURAL '''
# http://text-processing.com/demo/

''' Análisis de texto online '''
# http://textanalysisonline.com/nltk-pos-tagging


''' STEEMING '''
'''En la morfología lingüística y la recuperación de la información,
stemming es el proceso para reducir las palabras inflexas
(o algunas veces derivadas) a su forma de tallo, base o raíz,
generalmente una forma de palabra escrita.

El tallo no necesita ser idéntico a la raíz morfológica de la palabra;
normalmente es suficiente que las palabras relacionadas se correspondan
con el mismo tronco, incluso si este tallo no es en sí mismo una raíz válida.

Los algoritmos para stemming han sido estudiados en informática
desde la década de 1960. Muchos motores de búsqueda tratan palabras
con el mismo tallo que los sinónimos como un tipo de expansión de consulta,
un proceso llamado conflation.'''

'''NLTK proporciona varias interfaces de steemers famosos,
como Porter stemmer, Lancaster Stemmer, Snowball Stemmer y etc.
En NLTK, el uso de estos stemmers es muy simple.

Para Porter Stemmer, que se basa en The Porter Stemming Algorithm,
se puede utilizar de esta manera:'''

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
porter_stemmer.stem('maximum')        # u’maximum’
porter_stemmer.stem('presumably')     # u’presum’

''' Lancaster Stemmer '''
from nltk.stem.lancaster import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
lancaster_stemmer.stem('maximum')

''' Snowball Stemmer (¡Admite el lenguaje español!) '''
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer('spanish')
print(snowball_stemmer.stem('seguridad'))


''' LEMATIZAR '''
'''El método NLTK Lemmatization se basa en la función morphy
incorporada de WordNet. WordNet® es una gran base de datos léxica de inglés.

Los sustantivos, verbos, adjetivos y adverbios se agrupan en conjuntos
de sinónimos sintéticos (synsets), cada uno de ellos expresando
un concepto distinto. Las relaciones de síntesis están interrelacionadas
mediante relaciones conceptuales-semánticas y léxicas. La red resultante
de palabras y conceptos relacionados de forma significativa
se puede navegar con el navegador.

WordNet también está libre y públicamente disponible para su descarga.
La estructura de WordNet lo convierte en una herramienta útil
para la lingüística computacionaly el procesamiento del lenguaje natural.

WordNet se asemeja superficialmente a un tesauro, en que agrupa las palabras
en base a sus significados. Sin embargo, hay algunas distinciones importantes.
En primer lugar, WordNet enlaza no sólo formas de palabras, cadenas de letras,
sino también sentidos específicos de palabras.

Como resultado, las palabras que se encuentran en estrecha proximidad entre sí
en la red son semánticamente desambiguados. En segundo lugar, WordNet
etiqueta las relaciones semánticas entre palabras, mientras que
los agrupamientos de palabras en un tesauro no siguen ningún patrón
explícito que no sea la similitud de significado. '''

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
wordnet_lemmatizer.lemmatize('dogs')    # u'dog'
wordnet_lemmatizer.lemmatize('are')     # u'are'
wordnet_lemmatizer.lemmatize('is')      # u'is'

'''Notaría que los resultados de "are" y "is" no son "be",
es porque el argumento lemmatize por defecto es "n" (name): '''

#lemmatize(word, pos=’n’)

''' Así que hay que espicificarle que busque el verbo '''
print(wordnet_lemmatizer.lemmatize('is', pos='v'))     # u’be’



