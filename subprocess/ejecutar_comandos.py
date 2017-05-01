import subprocess

''' Ejecutar comandos '''
subprocess.call(['ls', '-l'], shell=True)

''' Separar comandos con shlex para una mejor visualización '''
import shlex
command_line = 'sudo apt-get install python3 -y'
args = shlex.split(command_line)
subprocess.call(args)

#------------------------------------------------

from subprocess import Popen, PIPE

process = Popen(['swfdump', '/tmp/filename.swf', '-d'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
