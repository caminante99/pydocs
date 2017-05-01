# -*- coding: cp1252 -*-

''' Vamos a crear un entorno virtual (también llamado un virtualenv).
Aislará la configuración Python/Django con base en cada proyecto,
lo que significa que cualquier cambio que realices en un sitio web
no afectará a otros que también estés desarrollando. '''

''' Todo lo que necesitas hacer es encontrar un directorio
en el que desees crear el virtualenv; tu directorio home.
En este caso utilizaremos esta misma carpeta como home: django'''

''' Luego ejecutar:
virtualenv venv
donde venv es el nombre del entorno virtual'''

'''
Para comenzar a utilizar el entorno virtual, necesita ser activado.
Colócate (para Windows) dentro del directorio Scripts del entorno
virtual y ejecuta:
activate.bat
'''

'''El nombre del entorno virtual aparecerá a la izquierda del prompt,
esto es para saber que está activo. A partir de ahora, cada paquete
que instalemos con pip se colocará en la carpeta venv,
aislado de la instalación general de Python. '''

''' Ahora instalamos django:
pip install django==1.8
'''


#---------------------------------------------------
'''Para borrar un entorno virtual, simplemente borramos su carpeta.'''



