# -*- coding: cp1252 -*-

''' Para leer todos los argumentos que se escriban detr�s
del nombre del script: '''
import sys

print("N�mero de par�metros: ", len(sys.argv))
print("Lista de argumentos: ", sys.argv)

''' El resultado es algo como lo siguiente:

$ python parametros-basico.py 
N�mero de par�metros:  1
Lista de argumentos:  ['parametros-basico.py']
$ python parametros-basico.py -a ALL file1 file2
N�mero de par�metros:  5
Lista de argumentos:  ['parametros-basico.py', '-a', 'ALL', 'file1', 'file2']
'''

#------------------------------------------------
''' Procesando par�metros: '''

import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Mostrar informaci�n de depuraci�n", action="store_true")
args = parser.parse_args()
 
# Aqu� procesamos lo que se tiene que hacer con cada argumento
if args.verbose:
    print("depuraci�n activada!!!")

'''Y el resultado es:

$ python argparse-mas-una-opcion.py  -h
usage: argparse-mas-una-opcion.py [-h] [-v]
 
optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Mostrar informaci�n de depuraci�n
 
$ python argparse-mas-una-opcion.py  -v
depuraci�n activada!!!
 
$ python argparse-mas-una-opcion.py  --verbose
depuraci�n activada!!!
