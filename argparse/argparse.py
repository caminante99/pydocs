# -*- coding: cp1252 -*-

''' Para leer todos los argumentos que se escriban detrás
del nombre del script: '''
import sys

print("Número de parámetros: ", len(sys.argv))
print("Lista de argumentos: ", sys.argv)

''' El resultado es algo como lo siguiente:

$ python parametros-basico.py 
Número de parámetros:  1
Lista de argumentos:  ['parametros-basico.py']
$ python parametros-basico.py -a ALL file1 file2
Número de parámetros:  5
Lista de argumentos:  ['parametros-basico.py', '-a', 'ALL', 'file1', 'file2']
'''

#------------------------------------------------
''' Procesando parámetros: '''

import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
args = parser.parse_args()
 
# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.verbose:
    print("depuración activada!!!")

'''Y el resultado es:

$ python argparse-mas-una-opcion.py  -h
usage: argparse-mas-una-opcion.py [-h] [-v]
 
optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Mostrar información de depuración
 
$ python argparse-mas-una-opcion.py  -v
depuración activada!!!
 
$ python argparse-mas-una-opcion.py  --verbose
depuración activada!!!
