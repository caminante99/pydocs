# -*- coding: cp1252 -*-

''' Funci�n para contar el tiempo que tarda una funci�n '''
from time import time

def count_time(f):
    """
    Ejecuta una funci�n y calcula el tiempo que tarda.
    Imprime el resultado.
    
    Es un decorador. Para usarlo coloca @count_time en la
    l�nea anterior de la funci�n que necesites probar.
    """
    def wrapper():
        # Empieza a contar.
        start_time = time()
        # Toma el valor de retorno de la funci�n original.
        ret = f()
        # Calcula el tiempo transcurrido.
        elapsed_time = time() - start_time
        print("Tiempo transcurrido: %0.10f seconds." % elapsed_time)
        return ret
    
    return wrapper

# Usar como decorador en una funci�n

#-----------------------------------------------------------

''' Tiempo en Unix Timestamps '''
time()
