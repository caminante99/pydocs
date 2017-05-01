# -*- coding: utf-8 -*-
import subprocess, time

hosts = ('8.8.8.8', 'poloniex.com', 'yahoo.com')

def ping(host):
  ret = subprocess.call(['ping', '-c', '3', '-W', '5', host],
    stdout=open('/dev/null', 'w'),
    stderr=open('/dev/null', 'w'))
  return ret == 0

def red():
  xstatus = False
  for h in hosts:
    if ping(h):
      print "[%s] Hay conexión a la red" % time.strftime("%Y-%m-%d %H:%M:%S")
      xstatus = True
      break
  if xstatus:
    print "[%s] La conexión a la red ha caído" % time.strftime("%Y-%m-%d %H:%M:%S")
  return xstatus

'''
quit(net_is_up())
'''
