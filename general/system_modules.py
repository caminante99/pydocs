# -*- coding: cp1252 -*-

import os

''' Saber en qué directorio estamos '''
print os.getcwd()

''' Cambiar de directorio '''
os.chdir('..')

''' Saber si se puede acceder a un archivo o directorio '''
#os.access(path, modo_de_acceso)
''' El modo de acceso es os.F_OK si queremos ver si accedemos'''

''' Saber en que path está el archivo del script que ejecutamos '''
os.path.dirname(os.path.abspath(__file__))

''' Saber con que versión de python estamos ejecutando '''
sys.version[0]
# También se puede usar:
sys.version_info[0]

''' Añadir temporalmente ruta al path para solucionar problemas de import '''
sys.path.insert(1, path)
# Código import + ejecuciones
sys.path.remove(path)

''' Cambiar de directorio de trabajo raíz '''
#os.chroot()

''' Crear un directorio '''
#os.mkdir(path)

''' Eliminar un directorio '''
#os.rmdir(path)

''' Eliminar un archivo '''
#os.remove()

''' Renombrar un archivo '''
#os.rename(actual, nuevo)

''' Acceder a las variables de entorno '''
for variable, valor in os.environ.iteritems(): 
    print "%s: %s" % (variable, valor)

''' Ejecutar comandos del sistema operativo '''
#os.system('comando_1 comando_2')

''' Terminar un programa '''
import sys
#sys.exit()

#----------------------------------------------

''' El módulo glob '''
''' Provee una función para hacer listas de archivos
a partir de búsquedas con comodines en directorios (*): '''

import glob
glob.glob('*.py')

#-----------------------------------------------

''' El módulo subprocess '''
'''Entre los métodos más comunes de subprocess, podemos encontrar
subprocess.call(). Este método, suele ser útil, para ejecutar
órdenes sencillas, como por ejemplo, limpiar la pantalla:'''

from subprocess import call
#call('clear')

'''El método call, esperará recibir como primer argumento,
el comando a ser ejecutado, como se mostró en el ejemplo anterior.
Sin embargo, si el comando requiere argumentos, como primer parámetro,
call necesitará recibir una lista donde el primer elemento
será el comando y el segundo, sus argumentos.

Un ejemplo de ello, es el siguiente código encargado de hacer
un listado de archivos y directorios:'''

comando_y_argumentos = ['ls', '-lha']
#call(comando_y_argumentos)

'''El módulo subprocess también nos provee del submódulo Popen,
el cuál nos permite, no solo ejecutar órdenes al igual que call,
sino mantener un mejor control sobre las salidas.'''

'''A diferencia de call, Popen no es un método de subprocess,
sino, un objeto. Cómo tal, la forma correcta de iniciar
un proceso con Popen, será entonces, crear un objeto Popen
para poder acceder a sus métodos, y así evitar, que el proceso
quede abierto en ejecución.

De esta forma, creamos el objeto y luego, llamamos al método
wait() de Popen, el cual espera a que el proceso finalice.'''

from subprocess import Popen

proceso = Popen(['ls', '-lha'])
proceso.wait()

''' Utilizando tuberías para para capturar la salida '''
''' Popen nos permite capturar tanto la entrada como la salida
estándar o su error. Para efectuar dicha captura, tanto stdout
como stdin y/o stderr se pasan como argumentos clave a Popen.
El valor de dichos argumentos, deberá ser un archivo o una tubería
que funcione como tal. Y para esto, Popen, también nos provee de
una tubería para capturar dichas entradas y salidas,llamada PIPE.

De esta forma, si quisiéramos capturar la salida estándar
o error de nuestro código, debemos pasarle a Popen, stdout
y stderr como argumentos claves, con PIPE como valor de cada
uno de ellos, para lo cual, también debemos importar PIPE: '''

from subprocess import PIPE
proceso = Popen(['ls', '-lha'], stdout=PIPE, stderr=PIPE) # Dará error
error_econtrado = proceso.stderr.read()
proceso.stderr.close()
listado = proceso.stdout.read()
proceso.stdout.close()

'''Capturando la salida, como bien se puede ver en el ejemplo,
stdout y stderr, son tratados como archivos (de hecho, lo son
ya que hemos utilizado una tubería). Por lo tanto,
deben ser cerrados una vez leídos.

Luego, podremos manipular dichas lecturas, como cualquier string: '''

if not error_encontrado: 
    print listado 
else: 
    print "Se produjo el siguiente error:\n%s" % error_encontrado

#---------------------------------------------

''' Rutas de archivos y directorios. El submódulo os.path() '''
'''
Ruta absoluta                   	    os.path.abspath(path)
Directorio base	                            os.path.basename(path)
Saber si un directorio existe	            os.path.exists(path)
Conocer último acceso a un directorio	    os.path.getatime(path)
Conocer tamaño del directorio	            os.path.getsize(path)
Saber si una ruta es absoluta	            os.path.isabs(path)
Saber si una ruta es un archivo	            os.path.isfile(path)
Saber si una ruta es un directorio	    os.path.isdir(path)
Saber si una ruta es un enlace simbólico    os.path.islink(path)
Saber si una ruta es un punto de montaje    os.path.ismount(path)
'''

