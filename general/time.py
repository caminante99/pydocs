# -*- coding: cp1252 -*-

''' Función para contar el tiempo que tarda una función '''
from time import time

def count_time(f):
    """
    Ejecuta una función y calcula el tiempo que tarda.
    Imprime el resultado.
    
    Es un decorador. Para usarlo coloca @count_time en la
    línea anterior de la función que necesites probar.
    """
    def wrapper():
        # Empieza a contar.
        start_time = time()
        # Toma el valor de retorno de la función original.
        ret = f()
        # Calcula el tiempo transcurrido.
        elapsed_time = time() - start_time
        print("Tiempo transcurrido: %0.10f seconds." % elapsed_time)
        return ret
    
    return wrapper

# Usar como decorador en una función

#-----------------------------------------------------------

''' Tiempo en Unix Timestamps '''
time()
