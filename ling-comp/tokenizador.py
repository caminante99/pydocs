# -*- encode: utf-8 -*-

text = '''El análisis automático de sentimiento es un paso más
en el intento de traducir las emociones humanas a datos.
Pero la espontaneidad y la inmediatez de la opinión en medios
sociales hacen que estos sentimientos sean más auténticos y
preserven su contenido emocional.'''

def tokenizador(texto):
    lista = [] #lista vacia
    palabra = '' #palabra vacia
    excepciones = [' ', ',', '.', '\n'] #cuando se encuentra algo de esto
    for caracter in text: #por cada caracter del texto le hacemos lo que sigue
        if caracter not in excepciones:
            palabra += caracter #palabra = palabra + caracter le va poniendo letras
        else:
            lista.append(palabra) #metemos la palabra en la lista
            palabra = '' #volvemos a poner palabra vacia cuando llega .,' ' etc

    lista.remove('') #esto es para quitar el elemento vacio

    resultado=[]
    
    for token in lista:
        sum_estad = 0 #es 0 pq el primero ya se cuenta a si mismo 
        for est in lista: #est estadistica de token
            if est == token: #para que lo cuente como minusculas
                sum_estad += 1 #para que se vaya sumando si se ve repetido

        resultado.append(token + ': ' + str(sum_estad / len(lista)))
        ''' para que lo ponga en una linea la palabra y la frec
          y str para convertir en cadena pq si no no se puede sumar '''

    resultado.sort()
    resultado = set(resultado)
    for r in resultado:
        print(r)
        
            
    
tokenizador(text)
