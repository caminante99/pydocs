# -*- coding: cp1252 -*-

''' Vamos a crear un entorno virtual (tambi�n llamado un virtualenv).
Aislar� la configuraci�n Python/Django con base en cada proyecto,
lo que significa que cualquier cambio que realices en un sitio web
no afectar� a otros que tambi�n est�s desarrollando. '''

''' Todo lo que necesitas hacer es encontrar un directorio
en el que desees crear el virtualenv; tu directorio home.
En este caso utilizaremos esta misma carpeta como home: django'''

''' Luego ejecutar:
virtualenv venv
donde venv es el nombre del entorno virtual'''

'''
Para comenzar a utilizar el entorno virtual, necesita ser activado.
Col�cate (para Windows) dentro del directorio Scripts del entorno
virtual y ejecuta:
activate.bat
'''

'''El nombre del entorno virtual aparecer� a la izquierda del prompt,
esto es para saber que est� activo. A partir de ahora, cada paquete
que instalemos con pip se colocar� en la carpeta venv,
aislado de la instalaci�n general de Python. '''

''' Ahora instalamos django:
pip install django==1.8
'''


#---------------------------------------------------
'''Para borrar un entorno virtual, simplemente borramos su carpeta.'''



