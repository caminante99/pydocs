#!/usr/bin/env python
 
#importamos el modulo para trabajar con sockets
import socket
 
#Creamos un objeto socket para el servidor. Podemos dejarlo sin parametros pero si 
#quieren pueden pasarlos de la manera server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
 
#Nos conectamos al servidor con el metodo connect. Tiene dos parametros
#El primero es la IP del servidor y el segundo el puerto de conexion
s.connect(("localhost", 9998))
 
#Creamos un bucle para retener la conexion
while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    mensaje = raw_input("Mensaje a enviar >> ")
 
    #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
    s.send(mensaje)
 
    #Si por alguna razon el mensaje es close cerramos la conexion
    if mensaje == "close":
        break
 
#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Adios.")
 
#Cerramos la instancia del objeto servidor
s.close()
