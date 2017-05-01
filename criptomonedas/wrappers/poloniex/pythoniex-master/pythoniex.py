# -*- coding: utf-8 -*-
from modules import funcionamiento, trade


# Aquí hay funciones puras que se encuentran en funcionamiento
# Este archivo organiza el programa, haciendo que sea fácil ver
# cómo está estructurado

def organizador():
        funcionamiento.saludo()
        funcionamiento.configuracion_inicial() # Configuración inicial
        funcionamiento.ver_checkpoints() # Muestra donde irán los checkpoints
        funcionamiento.ver_stoploss() # Muestra donde irá el stop-loss
        funcionamiento.empezar() # Pregunta de comienzo del programa
        trade.trade()
         # Trading
         # Interrupción
         # Guardar datos
         # Cierre
