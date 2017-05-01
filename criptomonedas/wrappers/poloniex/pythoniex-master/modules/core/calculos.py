# -*- coding: utf-8 -*-

# ARITMÉTICA

#Admite una lista con un nº de valores arbitrario y calcula la media
def media(*valores): 
    n_valores = len(valores)
    suma = 0
    for v in valores:
        suma += v
    respuesta = float(suma) / float(n_valores)
    return respuesta


#Admite 2 valores, un porcentaje y un valor
#Devuelve la diferencia entre el número dado y el nuevo número calculado
#Ejemplo: porcentaje = 10, valor = 10 -> el 10% de 10 es 1, entonces 10 - 1 = 9
def porcentaje_resta(porcentaje, valor):
    porciento = float(valor) / 100 * float(porcentaje)
    respuesta = float(valor) - float(porciento)
    return respuesta

# Calcula el % de diferencia entre dos valores
def porcentaje_diferencia(valor_1, valor_2):
    if float(valor_1) < float(valor_2):
        resta = float(valor_2) - float(valor_1)
        porcentaje = (resta / float(valor_1)) * 100
    else:
        resta = float(valor_1) - float(valor_2)
        porcentaje = (resta / float(valor_2)) * 100
    return porcentaje   
      
# Admite un porcentaje y dos valores. Resta el valor más alto y el más bajo
# Luego calculo el porcentaje 
def porcentaje_relativo(porcentaje, valor_1, valor_2):
    if float(valor_1) < float(valor_2):
        resta = float(valor_2) - float(valor_1)
        porciento = (float(resta) / 100) * float(porcentaje)
        respuesta = valor_1 + porciento
    else:
        resta = float(valor_1) - float(valor_2)
        porciento = (float(resta) / 100) * float(porcentaje)
        respuesta = valor_2 + porciento
    return respuesta
    
#---------------------------------------------------
   
# COMPROBACIONES (Rangos...)

#A dmite 3 valores: el primero es el valor a consultar
# Los otros dos son el mínimo y el máximo del rango a consultar
#Retorna un booleano
def rango(valor, rango_min, rango_max):
    if float(valor) > float(rango_min) and float(valor) < float(rango_max):
        return True
    else:
        return False
        
        
