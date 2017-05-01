# -*- coding: utf-8 -*-

''' Primero debemos asegurarnos que tenemos instalado django
y que tenemos la carpeta C:\Python27\Scripts en el PATH del sistema'''

''' Para comenzar un proyecto en django, activa el entorno virtual
siguiendo los pasos del archivo configurar_entorno_virtual.py'''

''' Una vez activado creamos el proyecto ejecutando lo siguiente: '''
# dajngo-admin startproject mysite
''' donde mysite es el nombre de nuestro proyecto '''

#---------------------------------------------------
'''
Ahora deberías tener una estructura de directorios parecida a esto:

djangogirls
├───manage.py
└───mysite
        settings.py
        urls.py
        wsgi.py
        __init__.py
        
manage.py es un script que ayuda con la administración del sitio.
Con ello podremos iniciar un servidor web en nuestro
ordenador sin necesidad de instalar nada más, entre otras cosas.

El archivo settings.py contiene la configuración de tu sitio web.

El archivo urls.py contiene una lista de los patrones
utilizados por urlresolver. '''

#---------------------------------------------------

''' Configurar el proyecto '''
''' Vamos a mysite/settings.py. Encuentra la línea que contiene
TIME_ZONE y modifícala para elegir tu propia zona horaria:

    TIME_ZONE = 'Europe/Madrid'

También necesitaremos agregar una ruta para los archivos estáticos.
Ve hacia abajo hasta el final del archivo, y justo por debajo
de la entrada STATIC_URL, agrega una nueva llamada STATIC_ROOT:

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


Hay una gran variedad de opciones de bases de datos para almacenar
los datos de tu sitio. Utilizaremos el que viene por defecto, sqlite3.

Esto ya está configurado en esta parte de tu archivo mysite/settings.py:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    
Para crear una base de datos para nuestro blog, ejecutemos
lo siguiente en la consola: python manage.py migrate

(necesitamos estar en el directorio del proyecto
que contiene el archivo manage.py).

Si eso va bien, deberías ver algo así:

(myvenv) ~/djangogirls$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, contenttypes, auth, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying sessions.0001_initial... OK


¡Y listo! ¡Es hora de iniciar el servidor web y ver
si nuestro sitio web está funcionando!

(myvenv) ~/djangogirls$ python manage.py runserver
Ahora todo lo que debes hacer es verificar
que tu sitio esté corriendo - abre tu navegador e ingresa la dirección:

http://127.0.0.1:8000/

El servidor web se apropiará de tu consola hasta que lo termines
manualmente: para tipear más comandos o abres una nueva terminal
(y no te olvides de activar tu virtualenv allí también),
o frena el servidor web yendo a la consola en la que está corriendo
y presionando Ctrl+C.
'''



