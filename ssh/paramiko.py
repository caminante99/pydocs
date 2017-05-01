# -*- coding: cp1252 -*-

# sudo apt-get install build-essential libssl-dev libffi-dev python-dev
# wget https://pypi.python.org/packages/3c/ec/a94f8cf7274ea60b5413df054f82a8980523efd712ec55a59e7c3357cf7c/pyparsing-2.2.0.tar.gz
# gunzip pyparsing-2.2.0.tar.gz
# tar -xvf pyparsing-2.2.0.tar
# cd pyparsing-2.2.0 && sudo python3 setup.py install

# sudo apt-get install python3-appdirs
# sudo pip3 install -U appdirs


# sudo pip3 install cryptography
# sudo pip3 install paramiko

# sudo pip3 install scp

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.12', username='jesse', password='lol')

# Realizar llamadas simples
>>> ssh.connect('127.0.0.1', username='jesse', 
...    password='lol')
>>> stdin, stdout, stderr = \
...    ssh.exec_command("uptime")
>>> type(stdin)

>>> stdout.readlines()
['13:35  up 11 days,  3:13, 4 users, load averages: 0.14 0.18 0.16\n']

# DOCS -> http://docs.paramiko.org/en/2.1/api/client.html

# Conexión para SCP

from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com')

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())

scp.put('test.txt', 'test2.txt')
scp.get('test2.txt')

scp.close()


# Conexión mediante FTP
'''
This time, we make a call into ''open_sftp()'' after we perform the
connect to the host. ''open_sftp()'' returns a ''paramiko.SFTPClient''
client object that supports all of the normal sftp operations
(stat, put, get, etc.). In this example, we perform a "get" operation
to download the file ''remotefile.py'' from the remote system and write
it to to the local file, ''localfile.py''. '''

ftp = ssh.open_sftp() ftp.get('remotefile.py', 'localfile.py') ftp.close()

