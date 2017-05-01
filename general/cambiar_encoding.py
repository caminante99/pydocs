# -*- coding: cp1252 -*-

''' Python 2 viene por defecto con una codificaci�n ASCII,
mientras Python 3 viene por defecto con utf-8.
Esto provoca que en Python no podamos colocar tildes ni e�es,
lo cual en Django por ejemplo nos destroza la vida. '''

''' Cambiar la codificaci�n por defecto '''
''' Dentro de la carpeta /Lib/site-packages de la instalaci�n de Python
buscamos el archivo sitecustomize.py (si no est� lo creamos sin miedo).
Dentro del archivo a�adimos estas dos l�neas: '''

import sys
sys.setdefaultencoding('utf-8')
