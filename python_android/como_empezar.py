# -*- coding: cp1252 -*-

''' Instalar Kivy mediante pip: '''
'''
python -m pip install --upgrade pip wheel setuptools

python -m pip install docutils    
python -m pip install pygments
python -m pip install pypiwin32
python -m pip install kivy.deps.sdl2
python -m pip install kivy.deps.glew
python -m pip install kivy.deps.gstreamer

pip install cython
pip install hg+http://bitbucket.org/pygame/pygame
'''
#--------------------------------------------

''' Hello Word! en Kivy '''
import kivy
kivy.require('1.9.2') # reemplaza por tu versi�n actual de Kivy !

from kivy.app import App
from kivy.uix.label import Label # Significa etiqueta

# A�ade las 2 siguientes l�neas para solventar el bug de OpenGL 2.0
from kivy import Config
Config.set('graphics', 'multisamples', '0')

class Aplicacion(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    Aplicacion().run()

#--------------------------------------------

''' Comentando el c�digo anterior '''

from kivy.app import App
''' Es necesario que la clase base de la aplicaci�n herede de la
clase App. Est� en el directorio_de_instalaci�n_de_kivy/kivy/app.py. '''

''' Ve y abre ese archivo si deseas ahondar en lo que hace la clase
App de Kivy. Kivy se basa en Python y utiliza Sphinx para la documentaci�n,
por lo que la documentaci�n de cada clase est� en el archivo real. '''

from kivy.uix.label import Label
''' Ten en cuenta la forma en la que se establecen los paquetes.
El modulo uix es la secci�n que contiene los elementos de la interfaz
como layouts y widgets. '''

#def build(self):
''' Mira la imagen del ciclo de vida de una aplicaci�n Kivy.
Esta es la funci�n donde debes inicializar para tu widget ra�z. '''

#-------------------------------------------

''' Iniciar una aplicaci�n en Windows y en Linux '''
'''
Linux

    $ python main.py

Windows

    $ python main.py
    # or
    C:\appdir>kivy.bat main.py
'''

