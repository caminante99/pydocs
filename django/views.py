# -*- coding: cp1252 -*-

from django.shortcuts import render
from django.utils import timezone
from .models import Post

def lista_de_posts(peticion):
    posts = Post.objects.filter(fecha_de_publicacion__lte=timezone.now()).order_by('fecha_de_publicacion')
    return render(peticion, 'blog/post_list.html', {})


''' Este es el m�dulo que sirve las plantillas y las html.

Para m�s informaci�n consulta el archivo plantillas.py'''
