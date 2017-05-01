# -*- coding: cp1252 -*-


''' Iniciar la consola interactiva '''

python manage.py shell

''' El resultado debería ser:'''

(InteractiveConsole)
>>>

'''
Ahora estás en la consola interactiva de Django.
Es como la consola de Python, pero con un toque de magia Django.
Puedes utilizar todos los comandos Python aquí también, por supuesto.
'''

#----------------------------------------------------

''' Consultar los modelos de la base de datos '''
from blog.models import Post

Post.objects.all()
# [<Post: my post title>, <Post: another post title>]

''' Esta es una lista de las posts creadas anteriormente.
Hemos creado estos posts usando la interfaz del administrador de Django. '''

#-----------------------------------------------------

''' Crear un nuevo objeto del modelo existente '''

# Importamos el modelo User
from django.contrib.auth.models import User

# Consultamos los usuarios de la base de datos
User.objects.all() # [<User: mondeja>]

# Cogemos el usuario que necesitamos
yo = User.objects.get(username='mondeja')

# Creamos el objeto:
Post.objects.create(author=yo, title='Sample title', text='Test')

#-----------------------------------------------------

''' Filtrar objetos '''
''' Una parte importante de los QuerySets es la habilidad para filtrarlos.
Si queremos encontrar todos los posts cuyo autor es el User mondeja,
usaremos filter en vez de all en Post.objects.all().

En los paréntesis estableceremos qué condición o conduciones deben
cumplirse por un post del blog para terminar en nuestro queryset. '''

Post.objects.filter(autor=yo)
# ¡Tener en cuenta que yo no es una string, sino un objeto!
# Si no saltará un ValueError

''' ¿O tal vez querramos ver todos los posts que contengan
la palabra 'prueba' en el campo titulo? '''

Post.objects.filter(titulo__contains='prueba')

#-----------------------------------------------------

''' Ejecutando las funciones de los objetos '''
''' Vamos a publicar un post con el metodo publicar que le
creamos al modelo Post.

Primero obtén una instancia de un post que querramos publicar: ''''

post = Post.objects.get(id=1)

# Luego lanzamos su método para publicarlo
post.publicar()

''' Para comprobar que ha funcionado vamos a obtener una lista de
todos los objetos publicados. Lo hacemos filtrando los posts
que tienen el campo fecha_de_publicacion en el pasado:
'''

from django.utils import timezone
Post.objects.filter(fecha_de_publicacion__lte=timezone.now())

#-----------------------------------------------------

''' Ordenando objetos '''
''' Los QuerySets también te permiten ordenar la lista de objetos.
Intentemos ordenarlos por el campo fecha_de_creacion:'''

Post.objects.order_by('-fecha_de_creacion')

'''También podemos invertir el ordenamiento agregando - al principio:'''








