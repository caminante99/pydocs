# -*- coding: cp1252 -*-

''' Para poder subir tu propio paquete a PyPi, lo primero que debes
hacer es crear una cuenta en la p�gina oficial de PyPi.'''

# Mi contrase�a en PyPi empieza con la M en may�scula

''' Una vez que hemos creado la cuenta, vamos a empezar a preparar
nuestro paquete para ser subido a PyPi. Para ello, creamos un archivo
de configuraci�n llamado .pypirc con el siguiente contenido: '''

[distutils]
    index-servers =
        pypi

    [pypi]
    repository: https://pypi.python.org/pypi
    username: {{your_username}}
    password: {{your_password}}

''' Y lo guardamos en [~/.pypirc]. Este archivo nos va a ahorrar
que tengamos que acordarnos de nuestros credenciales. '''

#----------------------------------------------------------------

'''Preparar el paquete

Una vez que hemos incluido nuestro archivo de configuraci�n,
vamos a empezar a preparar el paquete que queremos subir
al repositorio PyPi. As� pues, el esquema que tenemos que seguir
ser� el siguiente: '''

root-dir/
        setup.py
        setup.cfg
        LICENSE.txt
        README.md
        mypackage/
            __init__.py
            file1.py
            file2.py
            file3.py

''' El archivo setup.py, deber� contener el siguiente c�digo python: '''

from distutils.core import setup
setup(
  name = 'mypackage',
  packages = ['mypackage'], # this must be the same as the name above
  version = '0.1',
  description = 'my description',
  author = 'Alejandro Esquiva',
  author_email = 'alejandro@geekytheory.com',
  url = 'https://github.com/{user_name}/{repo}', # use the URL to the github repo
  download_url = 'https://github.com/{user_name}/{repo}/tarball/0.1',
  keywords = ['testing', 'logging', 'example'],
  classifiers = [],
)

''' Una vez que tenemos el archivo setup.py, debemos crear tambi�n
el archivo setup.cfg. El cual contendr� el siguiente contenido: '''

[metadata]
description-file = README.md
    
''' Por �ltimo el archivo README.md ser� usado para describir
el paquete tal como lo usamos en Git, el archivo License.txt incluir�
la licencia de uso del paquete, como por ejemplo la licencia MIT. '''

#-------------------------------------------------------

''' Subir el paquete a PyPi

Una vez que hemos realizado correctamente todos los pasos,
vamos a pasar a subir nuestro c�digo a la plataforma PyPi,
para ello vamos a instalar previamente el m�dulo llamado pypi: '''

pip install pypi

''' Una vez que tenemos instalado el m�dulo pypi, vamos a subir
nuestro paquete escribiendo el siguiente comando: '''

python setup.py register -r pypi

# Si se produce un error UnicodeDecodeError simplemente pasa la
#__version__ y las otras etiquetas de informaci�n como u''

''' Seguidamente, ejecuta: '''

python setup.py sdist upload -r pypi

''' Si todo ha ido bien, enhorabuena, acabas de registrar tu primer
paquete en pypi, ahora puedes instalar el paquete en cualquier m�quina
con el comando: '''

pip install <mipaquete>



