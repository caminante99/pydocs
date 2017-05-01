# -*- coding: cp1252 -*-

import os

''' Saber en qu� directorio estamos '''
print os.getcwd()

''' Cambiar de directorio '''
os.chdir('..')

''' Saber si se puede acceder a un archivo o directorio '''
#os.access(path, modo_de_acceso)
''' El modo de acceso es os.F_OK si queremos ver si accedemos'''

''' Saber en que path est� el archivo del script que ejecutamos '''
os.path.dirname(os.path.abspath(__file__))

''' Saber con que versi�n de python estamos ejecutando '''
sys.version[0]
# Tambi�n se puede usar:
sys.version_info[0]

''' A�adir temporalmente ruta al path para solucionar problemas de import '''
sys.path.insert(1, path)
# C�digo import + ejecuciones
sys.path.remove(path)

''' Cambiar de directorio de trabajo ra�z '''
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

''' El m�dulo glob '''
''' Provee una funci�n para hacer listas de archivos
a partir de b�squedas con comodines en directorios (*): '''

import glob
glob.glob('*.py')

#-----------------------------------------------

''' El m�dulo subprocess '''
'''Entre los m�todos m�s comunes de subprocess, podemos encontrar
subprocess.call(). Este m�todo, suele ser �til, para ejecutar
�rdenes sencillas, como por ejemplo, limpiar la pantalla:'''

from subprocess import call
#call('clear')

'''El m�todo call, esperar� recibir como primer argumento,
el comando a ser ejecutado, como se mostr� en el ejemplo anterior.
Sin embargo, si el comando requiere argumentos, como primer par�metro,
call necesitar� recibir una lista donde el primer elemento
ser� el comando y el segundo, sus argumentos.

Un ejemplo de ello, es el siguiente c�digo encargado de hacer
un listado de archivos y directorios:'''

comando_y_argumentos = ['ls', '-lha']
#call(comando_y_argumentos)

'''El m�dulo subprocess tambi�n nos provee del subm�dulo Popen,
el cu�l nos permite, no solo ejecutar �rdenes al igual que call,
sino mantener un mejor control sobre las salidas.'''

'''A diferencia de call, Popen no es un m�todo de subprocess,
sino, un objeto. C�mo tal, la forma correcta de iniciar
un proceso con Popen, ser� entonces, crear un objeto Popen
para poder acceder a sus m�todos, y as� evitar, que el proceso
quede abierto en ejecuci�n.

De esta forma, creamos el objeto y luego, llamamos al m�todo
wait() de Popen, el cual espera a que el proceso finalice.'''

from subprocess import Popen

proceso = Popen(['ls', '-lha'])
proceso.wait()

''' Utilizando tuber�as para para capturar la salida '''
''' Popen nos permite capturar tanto la entrada como la salida
est�ndar o su error. Para efectuar dicha captura, tanto stdout
como stdin y/o stderr se pasan como argumentos clave a Popen.
El valor de dichos argumentos, deber� ser un archivo o una tuber�a
que funcione como tal. Y para esto, Popen, tambi�n nos provee de
una tuber�a para capturar dichas entradas y salidas,llamada PIPE.

De esta forma, si quisi�ramos capturar la salida est�ndar
o error de nuestro c�digo, debemos pasarle a Popen, stdout
y stderr como argumentos claves, con PIPE como valor de cada
uno de ellos, para lo cual, tambi�n debemos importar PIPE: '''

from subprocess import PIPE
proceso = Popen(['ls', '-lha'], stdout=PIPE, stderr=PIPE) # Dar� error
error_econtrado = proceso.stderr.read()
proceso.stderr.close()
listado = proceso.stdout.read()
proceso.stdout.close()

'''Capturando la salida, como bien se puede ver en el ejemplo,
stdout y stderr, son tratados como archivos (de hecho, lo son
ya que hemos utilizado una tuber�a). Por lo tanto,
deben ser cerrados una vez le�dos.

Luego, podremos manipular dichas lecturas, como cualquier string: '''

if not error_encontrado: 
    print listado 
else: 
    print "Se produjo el siguiente error:\n%s" % error_encontrado

#---------------------------------------------

''' Rutas de archivos y directorios. El subm�dulo os.path() '''
'''
Ruta absoluta                   	    os.path.abspath(path)
Directorio base	                            os.path.basename(path)
Saber si un directorio existe	            os.path.exists(path)
Conocer �ltimo acceso a un directorio	    os.path.getatime(path)
Conocer tama�o del directorio	            os.path.getsize(path)
Saber si una ruta es absoluta	            os.path.isabs(path)
Saber si una ruta es un archivo	            os.path.isfile(path)
Saber si una ruta es un directorio	    os.path.isdir(path)
Saber si una ruta es un enlace simb�lico    os.path.islink(path)
Saber si una ruta es un punto de montaje    os.path.ismount(path)
'''

