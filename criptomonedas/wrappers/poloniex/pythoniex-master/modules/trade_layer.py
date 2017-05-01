# -*- coding: utf-8 -*-

import llamadas, config
from core import calculos

base = llamadas.Base_datos()


# Calcula donde deben ir los checkpoints
# Admite dos valores que representan la media del soporte y la de la resistencia
# Calcula los checkpoints y devuelve una lista con todos los checkpoints
def checkpoints(soporte, resistencia):
    diferencia = float(resistencia) - float(soporte)    
    decimo_checkpoint = float(diferencia) / config.numero_checkpoints
    lista_checkpoints = []
    checkpoint = float(soporte) + float(decimo_checkpoint)
    for i in range(config.numero_checkpoints):
        lista_checkpoints.append(checkpoint)
        checkpoint += decimo_checkpoint
    return lista_checkpoints     

def guardar_checkpoints(*checkpoints):
    tupla_checkpoints = checkpoints[0]
    count = 0
    for i in tupla_checkpoints:
        base.insertar_checkpoint(count + 1, float(i))
        count += 1

def definir_checkpoints():
    soporte_min = float(base.mostrar_margen('soporte', 'minimo'))
    soporte_max = float(base.mostrar_margen('soporte', 'maximo'))
    resistencia_min = float(base.mostrar_margen('resistencia', 'minimo'))
    resistencia_max = float(base.mostrar_margen('resistencia', 'maximo'))
    media_soporte = calculos.media(soporte_min, soporte_max)                #Calcula la media del soporte
    media_resistencia = calculos.media(resistencia_min, resistencia_max)        # y la media de resistencia
    return checkpoints(media_soporte, media_resistencia)
    
    # Sube el stoploss al siguiente checkpoint:
    # ((checkpoint_nuevo - anterior / 100) * porcentaje de subida configurado) + anterior
def subir_stoploss(checkpoint_anterior, checkpoint_nuevo):
    stoploss = (((float(checkpoint_nuevo) - float(checkpoint_anterior)) / 100) * config.stop_loss_movil) + checkpoint_anterior
    return stoploss
    
