# -*- coding: utf-8 -*-

''' Creamos una carpeta llamada static dentro de la aplicación blog.
Django encontrará automáticamente cualquier carpeta que se llame
"static" dentro de las carpetas de tus aplicaciones y podrá utilizar
su contenido como ficheros estáticos. '''

''' Crea un nuevo directorio llamado css dentro de tu directorio static.
Para añadir tu propio estilo a tu página web, crea un nuevo fichero
llamado blog.css dentro de este directorio css. '''

web
└─── blog
     └─── static
          └─── css
               └─── blog.css

''' Incluir css en html '''
# Añadimos esto al principio de la página html:
{% load staticfiles %}

''' Aquí sólo estamos cargando ficheros estáticos. Luego, entre
el <head> y </head>, después de los enlaces a los ficheros
CSS de Bootstrap (el navegador lee los ficheros en el orden
en que están, así que nuestro fichero podría sobrescribir partes
del código de Bootstrap), añade la siguiente línea: '''

<link rel="stylesheet" href="{% static 'css/blog.css' %}">
