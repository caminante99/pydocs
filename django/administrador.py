# -*- coding: cp1252 -*-

from django.contrib import admin

# Importamos el modelo
from .models import Post

''' Para hacer nuestro modelo visible en la página del administrador,
tenemos que registrar el modelo'''
admin.site.register(Post)

''' Para entrar al login del administrador ponemos la IP + /admin/ '''

''' Para poder loguearnos debemos crear un superusuario: '''
# python manage.py createsuperuser
