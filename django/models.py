''' Página models de ejemplo '''

from django.db import models
from django.utils import timezone

    class Post(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title
        # Esta función retorna el nombre del post

# models.CharField - texto con un número limitado de caracteres
# models.TextField - textos largos sin un límite.
# models.DateTimeField - esto es fecha y hora
# modelos.ForeignKey - vínculo con otro modelo (el usuario)

''' Cada vez que se produzca un cambio en los modelos,
debemos indicárselo a django por medio de ejecutar lo siguiente: '''
# python manage.py makemigrations blog

''' Django preparará un archivo de migración que tenemos que
aplicar ahora a nuestra base de datos escribiendo: '''
# python manage.py migrate blog
