# -*- coding: cp1252 -*-

''' Python 2 viene por defecto con una codificación ASCII,
mientras Python 3 viene por defecto con utf-8.
Esto provoca que en Python no podamos colocar tildes ni eñes,
lo cual en Django por ejemplo nos destroza la vida. '''

''' Cambiar la codificación por defecto '''
''' Dentro de la carpeta /Lib/site-packages de la instalación de Python
buscamos el archivo sitecustomize.py (si no está lo creamos sin miedo).
Dentro del archivo añadimos estas dos líneas: '''

import sys
sys.setdefaultencoding('utf-8')
