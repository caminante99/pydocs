# -*- coding: cp1252 -*-

sudo apt-get install python-matplotlib

# ó

sudo pip3 install cairocffi

sudo pip3 install matplotlib

# ----------------------------------

# Resolver el siguiente error
TypeError: Couldn't find foreign struct converter for 'cairo.Context'

sudo apt-get install python3-pyqt5

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
