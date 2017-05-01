# -*- coding: cp1252 -*-

import matplotlib.pyplot as plt

''' Las representaciones en matplotlib se distinguen fundamentalmente
entre figura y sistema de ejes: '''

fig, axes = plt.subplots() # Si ejecutamos esta funcion tendremos una
                           # figura en blanco

''' El sistema de ejes es donde se cambian las representaciones: de
donde a donde van los parámetros, qué aspecto tiene a gráfica...
y la figura es el contenedor del sistema de ejes. '''

''' Todas las llamadas que antes estábamos haciendo a través del
comando plt ahora las haremos a través del comando axes, que es el
segundo objeto que nos han devuelto arriba. '''

# La ventaja de esto es que puedo separar la lógica de la representación
# del trabajo con la figura:
axes.plot(x, f(x), 'green', label='Funcion f(x)') # Representamos
fig.savefig('grafica1.png') # Guardamos la figura en .png

#---------------------------------------------------

''' Trabajar con varias figuras '''
fig, axes = plt.subplots(1, 2) # Una fila y dos columnas

''' Si otorgamos a subplots parámetros para espeficiar el número de filas
y columnas obtendremos más de una gráfica. Ahora, si llamamos a la función
axes, esta no devolverá un objecto axes, si no un array numpy de axes: '''

axes   # array([<matplotlib.axes._subplots.AxesSubplot object at 0x6ad17710>,
# <matplotlib.axes._subplots.AxesSubplot object at 0x6acc1830>], dtype=object)

# Si quiero pintar en la gráfica de la izquierda:
axes[0].plot(x, f(x), color='green', label='Funcion f(x)')

# Para hacer que ambas figuras compartan uno de los ejes:
fig, axes = plt.subplots(1, 2, sharey=True)


