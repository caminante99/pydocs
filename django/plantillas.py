# -*- coding: utf-8 -*-

''' Configuración inicial para crear plantillas '''

'''
Las plantillas se guardan en el directorio de blog/templates/blog.
Así que primero crea un directorio llamado templates dentro
de tu directorio blog. Luego crea otro directorio llamado blog
dentro de tu directorio de templates:

blog
└───templates
    └───blog

(Tal vez te preguntes por qué necesitamos dos directorios
llamados blog - como descubrirás más adelante, esto es simplemente
una útil convención de nomenclatura que hace la vida
más fácil cuando las cosas empiezan a complicarse más.)

Y ahora crea un archivo post_list.html (déjalo en blanco por ahora)
dentro de la carpeta blog/templates/blog.
'''

#---------------------------------------------------

''' Configurando el archivo views.py '''

'''
Lo que hacemos en las views es tomar algún contenido
(modelos guardados en la base de datos) y mostrarlo adecuadamente
en nuestra plantilla.

En nuestra view post_list necesitaremos tomar los modelos
que deseamos mostrar y pasarlos a una plantilla. Así que básicamente
en una view decidimos qué (modelo) se mostrará en una plantilla.
'''

''' Para ello abrimos el archivo blog/views.py y añadimos
la última línea que vemos, y quedaría así: '''

from django.shortcuts import render
from .models import Post

''' Ahora nos interesa obtener una lista de entradas del blog
que han sido publicadas y ordenarlas por fecha_de_publicacion '''

''' Pondremos este bloque de código en el archivo blog/views.py,
agregándolo a la función def lista_de_posts(peticion) '''

from django.shortcuts import render
from django.utils import timezone
from .models import Post

def lista_de_posts(peticion):
    posts = Post.objects.filter(fecha_de_publicacion__lte=timezone.now()).order_by('fecha_de_publicacion')
    return render(peticion, 'blog/post_list.html', {'posts': posts})

''' {} es un campo en el que podemos agregar algunas cosas
para que la plantilla las use. Necesitamos nombrarlos
(los seguiremos llamando 'posts' por ahora).
Se debería ver así: {'posts': posts} '''

#---------------------------------------------------

''' Imprimir variables en las plantillas '''
'''Para imprimir una variable en una plantilla de Django,
utilizamos llaves dobles con el nombre de la variable dentro: '''

{{ posts }} # Nos lo imprime como una lista, para iterarla:

{% for post in posts %}
        {{ post }}
    {% endfor %}

''' Extender plantillas dentro de etiquetas html '''
<div>
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>

    {% for post in posts %}
        <div>
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaksbr }}</p>
        </div>
    {% endfor %}

''' Todo lo que pones entre {% for %} y {% endfor %}
se repetirá para cada objeto en la lista.

El |linebreaksbr está dirigiendo el texto de los posts a través
de un filtro para convertir saltos de línea en párrafos. '''


#---------------------------------------------------

''' Extender plantillas dentro de otras '''

''' Creamos una plantilla base. En la parte que queremos insertar otro
html agregamos lo siguiente: '''

{% block content %}
{% endblock %}

''' Acabas de crear un block, una template tag que te permite insertar
HTML en este bloque de otras plantillas que extiendan a base.html '''

''' Para que otra plantilla extienda a la plantilla base agregamos al inicio: '''

{% extends 'blog/base.html' %}

''' Y entre el bloque que queremos extender incluimos: '''

{% block content %}
        # Lo que hay aquí dentro se mostrará en la plantilla base
{% endblock content %}

''' Siguiendo el ejemplo del tutorial, la plantilla que se extendería
a la base quedaría así: '''


{% extends 'blog/base.html' %}

    {% block content %}
        {% for post in posts %}
            <div class="post">
                <div class="date">
                    {{ post.published_date }}
                </div>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaksbr }}</p>
            </div>
        {% endfor %}
    {% endblock content %}
