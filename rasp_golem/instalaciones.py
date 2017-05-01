# -*- coding: cp1252 -*-

sudo apt-get install xsel
sudo apt-get install xclip
sudo pip3 install gtk
sudo pip3 install PyQt4
sudo pip3 install pyperclip

sudo pip3 install pyuserinput
sudo pip3 install pytesseract
sudo pip3 install python-libxdo

sudo pip3 install python-xlib
sudo apt-get install scrot
sudo apt-get install python-tk
sudo apt-get install python-dev -y
sudo pip3 install pyautogui

sudo apt-get install libx11-dev -y
sudo apt-get install libpng-dev; sudo apt-get install libpng12-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libxtst-dev
sudo apt-get install xorg openbox

''' Instalar libxdo '''
sudo apt-get install xdotool
pip3 install https://github.com/rshk/python-libxdo/tarball/master

# instalar autopy desde source
''' Si da un error 'no module named autopy.alert' '''
sudo nano /usr/local/lib/python3.4/dist-packages/autopy/__init__.py
# comentar la línea autopy.alert

''' Instalar un capturador de pantalla (K-SnapShot): '''
sudo apt-get install ksnapshot -y

#---------------------------------------------------
# OPCIONAL

''' Instalar librería para Steemit '''
sudo pip3 install pyyaml
sudo pip3 install funcy
sudo pip3 install websocket
sudo pip3 install websocket-client
sudo pip3 install scrypt
sudo pip3 install ecdsa
sudo apt-get install libffi-dev libssl-dev python-dev python3-pip -y
sudo pip3 install steem

# Para usar:
from piston.steem import Steem
s = Steem(node='wss://node.steem.ws')

# Documentation here: http://lib.piston.rocks/en/develop/
