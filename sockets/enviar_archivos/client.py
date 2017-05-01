#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      client.py
#
#      Copyright 2014 Recursos Python - www.recursospython.com
#
#

from socket import socket


def main():
    s = socket()
    s.connect(("192.168.1.11", 8000))
    
    while True:
        f = open("C:\Documents and Settings\Administrador\Escritorio\pydocs\sockets\enviar_archivos\pytesser.zip", "rb")
        content = f.read(1024)
        
        while content:
            # Enviar contenido.
            s.send(content)
            content = f.read(1024)
        
        break
    
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        s.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        s.send(bytes(chr(1), "utf-8"))
    
    # Cerrar conexión y archivo.
    s.close()
    f.close()
    print("El archivo ha sido enviado correctamente.")


if __name__ == "__main__":
    main()
