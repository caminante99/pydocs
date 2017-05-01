# -*- coding: cp1252 -*-

# Configuramos la IP estática en Android
# Ajustes -> WIFI -> Lista de conexiones -> Mantenemos pulsada ->
# Opciones avanzadas -> Donde dice protocolo DCHP cambiarlo por
# IP estática y rellenar los campos

# Instalamos en Android SSH Server

# Luego nos conectamos mediante la IP así
# ssh root@192.168.1.12 -p 2222

# Aparecerá una terminal ssh en la ruta principal de nuestra carpeta

# También podemos usar scp:
scp -P 2222 tareas.py root@192.168.1.12:/storage/scard1/music

# Para pasar directamente un archivo sin tener que escribir la contraseña
# podemos instalar sshpass
# sudo apt-get install sshpass

sshpass -p "" scp -P 2222 tareas.py root@192.168.1.12:/storage/scard1/music

'''
Copy the file "foobar.txt" from a remote host to the local host

    $ scp your_username@remotehost.edu:foobar.txt /some/local/directory 

Copy the file "foobar.txt" from the local host to a remote host

    $ scp foobar.txt your_username@remotehost.edu:/some/remote/directory 

Copy the directory "foo" from the local host to a remote host's directory "bar"

    $ scp -r foo your_username@remotehost.edu:/some/remote/directory/bar 

Copy the file "foobar.txt" from remote host "rh1.edu" to remote host "rh2.edu"

    $ scp your_username@rh1.edu:/some/remote/directory/foobar.txt \
    your_username@rh2.edu:/some/remote/directory/ 

Copying the files "foo.txt" and "bar.txt" from the local host to your home directory on the remote host

    $ scp foo.txt bar.txt your_username@remotehost.edu:~ 

Copy the file "foobar.txt" from the local host to a remote host using port 2264

    $ scp -P 2264 foobar.txt your_username@remotehost.edu:/some/remote/directory 

Copy multiple files from the remote host to your current directory on the local host

    $ scp your_username@remotehost.edu:/some/remote/directory/\{a,b,c\} . 

    $ scp your_username@remotehost.edu:~/\{foo.txt,bar.txt\} . 
'''
