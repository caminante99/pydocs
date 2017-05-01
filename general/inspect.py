# -*- coding: cp1252 -*-

''' Mediante el módulo inspect podemos de una forma sencilla
obtener todos los símbolos (funciones, variables, classes, etc)
de un módulo. Para ello debemos usar la función inspect.getmembers
que nos devuelve todos los símbolos del módulo. '''

import sys
import inspect
import os.path
import os


def get_symbols_from_module(python_module, filter_func):
    members = inspect.getmembers(python_module)
    return dict([[name,symbol] for name,symbol in members 
                               if filter_func(symbol)])

def main():
    # Obtain a map whith all the classes defined in the 
    # standard os module
    print get_symbols_from_module(os, inspect.isclass)

    # Obtain a map with all the functions defined in the
    # standard sys module
    print get_symbols_from_module(sys, inspect.isfunction)

if __name__ == '__main__':
main()
