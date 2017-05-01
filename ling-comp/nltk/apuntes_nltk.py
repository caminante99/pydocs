# -*- coding: cp1252 -*-

import nltk

''' Para instalar: pip install -U nltk '''

''' Por otro lado, adem�s de la librer�a tambi�n es necesario
instalar una serie de ficheros y diccionarios con patrones
para varios tipos de estructuras gramaticales llamados �corporas�,
dichos ficheros se instalan de forma independiente por medio de un
gestor de descargas que puede iniciarse utilizando el modulo nltk '''
#nltk.download()

''' Invocando a �download� se abre una ventana en la que se pueden
gestionar todos los ficheros �corpora� en diferentes categor�as.
Si es la primera vez que se utiliza nltk, se realizar� la descarga
de dichos ficheros. '''

''' Los corpus principales que se suelen utilizar en el procesamiento
de texto son conocidos como �gutenberg�, el cual incluye una selecci�n
de 18 textos del proyecto Gutenberg (http://www.gutenberg.org/)
y contiene m�s de 1.5 millones de palabras.
Para consultar los textos de gutenberg incluidos en el corpus de NLTK,
se pueden ejecutar las siguientes instrucciones. '''

from nltk.corpus import gutenberg as gut
#print(gut.fileids())

''' Los textos de la biblioteca hay que insertarlos como unicode '''
texto = u'shakespeare-hamlet.txt'

''' Contar n�mero de palabras en un texto '''
num_tokens = len(gut.words(texto))
''' Token: Se trata de la unidad m�s simple de procesamiento
y representa una palabra en el texto. '''

''' Contar n�mero de caracteres '''
num_caracteres = len(gut.raw(texto))

''' Contar n�mero de sentencias '''
num_sents = len(gut.sents(texto))
'''Una sentencia es de punto a punto en lenguas occidentales.
En otras lenguas es m�s dif�cil determinar qu� es una sentencia.'''


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

''' Clasificaci�n de tokens '''
tagged_tokens = pos_tag(tokens)

''' Consultar informaci�n sobre los tags '''
#nltk.help.upenn_tagset('JJ')

''' Tokenizar en espa�ol '''
texto = """El an�lisis autom�tico de sentimiento es un paso m�s
en el intento de traducir las emociones humanas a datos.
Pero la espontaneidad y la inmediatez de la opini�n en medios
sociales hacen que estos sentimientos sean m�s aut�nticos y
preserven su contenido emocional."""

spanish_tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
spanish_tokenizer.tokenize(texto)


''' API PARA LENGUAJE NATURAL '''
# http://text-processing.com/demo/

''' An�lisis de texto online '''
# http://textanalysisonline.com/nltk-pos-tagging


''' STEEMING '''
'''En la morfolog�a ling��stica y la recuperaci�n de la informaci�n,
stemming es el proceso para reducir las palabras inflexas
(o algunas veces derivadas) a su forma de tallo, base o ra�z,
generalmente una forma de palabra escrita.

El tallo no necesita ser id�ntico a la ra�z morfol�gica de la palabra;
normalmente es suficiente que las palabras relacionadas se correspondan
con el mismo tronco, incluso si este tallo no es en s� mismo una ra�z v�lida.

Los algoritmos para stemming han sido estudiados en inform�tica
desde la d�cada de 1960. Muchos motores de b�squeda tratan palabras
con el mismo tallo que los sin�nimos como un tipo de expansi�n de consulta,
un proceso llamado conflation.'''

'''NLTK proporciona varias interfaces de steemers famosos,
como Porter stemmer, Lancaster Stemmer, Snowball Stemmer y etc.
En NLTK, el uso de estos stemmers es muy simple.

Para Porter Stemmer, que se basa en The Porter Stemming Algorithm,
se puede utilizar de esta manera:'''

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
porter_stemmer.stem('maximum')        # u�maximum�
porter_stemmer.stem('presumably')     # u�presum�

''' Lancaster Stemmer '''
from nltk.stem.lancaster import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
lancaster_stemmer.stem('maximum')

''' Snowball Stemmer (�Admite el lenguaje espa�ol!) '''
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer('spanish')
print(snowball_stemmer.stem('seguridad'))


''' LEMATIZAR '''
'''El m�todo NLTK Lemmatization se basa en la funci�n morphy
incorporada de WordNet. WordNet� es una gran base de datos l�xica de ingl�s.

Los sustantivos, verbos, adjetivos y adverbios se agrupan en conjuntos
de sin�nimos sint�ticos (synsets), cada uno de ellos expresando
un concepto distinto. Las relaciones de s�ntesis est�n interrelacionadas
mediante relaciones conceptuales-sem�nticas y l�xicas. La red resultante
de palabras y conceptos relacionados de forma significativa
se puede navegar con el navegador.

WordNet tambi�n est� libre y p�blicamente disponible para su descarga.
La estructura de WordNet lo convierte en una herramienta �til
para la ling��stica computacionaly el procesamiento del lenguaje natural.

WordNet se asemeja superficialmente a un tesauro, en que agrupa las palabras
en base a sus significados. Sin embargo, hay algunas distinciones importantes.
En primer lugar, WordNet enlaza no s�lo formas de palabras, cadenas de letras,
sino tambi�n sentidos espec�ficos de palabras.

Como resultado, las palabras que se encuentran en estrecha proximidad entre s�
en la red son sem�nticamente desambiguados. En segundo lugar, WordNet
etiqueta las relaciones sem�nticas entre palabras, mientras que
los agrupamientos de palabras en un tesauro no siguen ning�n patr�n
expl�cito que no sea la similitud de significado. '''

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
wordnet_lemmatizer.lemmatize('dogs')    # u'dog'
wordnet_lemmatizer.lemmatize('are')     # u'are'
wordnet_lemmatizer.lemmatize('is')      # u'is'

'''Notar�a que los resultados de "are" y "is" no son "be",
es porque el argumento lemmatize por defecto es "n" (name): '''

#lemmatize(word, pos=�n�)

''' As� que hay que espicificarle que busque el verbo '''
print(wordnet_lemmatizer.lemmatize('is', pos='v'))     # u�be�



