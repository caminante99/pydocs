from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
        # Examples:
        # url(r'^$', 'mysite.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),

        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('blog.urls'))
    ]

# url(r'^admin/', include(admin.site.urls))
''' Esto significa que para cada URL que empieza con admin/
Django encontrará su correspondiente view. En este caso estamos
incluyendo en una sola línea muchas URLs de admin, así no está
todo comprimido en este pequeño archivo - es más limpio y legible. '''

# url(r'', include('blog.urls'))
''' Django ahora redirigirá todo lo que vaya hacia
'http://127.0.0.1:8000/' a blog.urls y buscará más instrucciones allí. '''

''' Ahora creamos un nuevo archivo blog/urls.py y agregamos: '''
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]

'''
Como puedes ver, ahora estamos asignando una view llamada
post_list al URL ^$. Sólo una cadena vacía coincidirá. Este patrón
mostrará a Django que views.post_list es el lugar correcto al que ir
si alguien ingresa a tu sitio web con la dirección 'http://127.0.0.1:8000/'.
'''



