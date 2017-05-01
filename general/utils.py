# -*- coding: cp1252 -*-

# Funciones útiles para usar en cualquier proyecto

#-----------------------------------------
# CONTADORES DE TIEMPO DE EJECUCIÓN 

''' Función para contar el tiempo que tarda una función '''
from time import time

def count_time(f):
    """
    Ejecuta una función y calcula el tiempo que tarda.
    Imprime el resultado.
    
    Es un decorador. Para usarlo coloca @count_time en la
    línea anterior de la función que necesites probar.
    """
    def wrapper():
        # Empieza a contar.
        start_time = time()
        # Toma el valor de retorno de la función original.
        ret = f()
        # Calcula el tiempo transcurrido.
        elapsed_time = time() - start_time
        print("Tiempo transcurrido: %0.10f seconds." % elapsed_time)
        return ret
    
    return wrapper

# Usar como decorador en una función

#----------------------------------------------
# TIMEOUTS

import threading

class TimeoutError(Exception):
    ''' Traceback (most recent call last):
        ...
        timeout.TimeoutError: execution expired
        out
    '''
    pass

class InterruptableThread(threading.Thread):
    def __init__(self, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self._result = None

    # El mÃ©todo run de una clase threading. Thread funciona al llamarla
    def run(self):      
        self._result = self._func(*self._args, **self._kwargs)

    @property
    def result(self):
        return self._result


class timeout(object):
    def __init__(self, sec):
        self._sec = sec

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            it = InterruptableThread(f, *args, **kwargs)
            it.start()
            it.join(self._sec)
            if not it.is_alive():
                return it.result
            raise TimeoutError('execution expired')
        return wrapped_f

''' CÃ³mo usar el timeout (expirador):

import time
from timeout import timeout

class Test(object):
    @timeout(2)
    def test_a(self, foo, bar):
        print foo
        time.sleep(1)
        print bar
        return 'A Done'

    @timeout(2)
    def test_b(self, foo, bar):
        print foo
        time.sleep(3)
        print bar
        return 'B Done'

t = Test()
print t.test_a('python', 'rocks')
print t.test_b('timing', 'out')

'''

#--------------------------------------------



"""Stack tracer for multi-threaded applications.


Usage:

import stacktracer
stacktracer.start_trace("trace.html",interval=5,auto=True) # Set auto flag to always update file!
....
stacktracer.stop_trace()
"""



import sys
import traceback
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
 
 # Taken from http://bzimmer.ziclix.com/2008/12/17/python-thread-dumps/
 
def stacktraces():
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# ThreadID: %s" % threadId)
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename, lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
 
    return highlight("\n".join(code), PythonLexer(), HtmlFormatter(
      full=False,
      # style="native",
      noclasses=True,
    ))


# This part was made by nagylzs
import os
import time
import threading

class TraceDumper(threading.Thread):
    """Dump stack traces into a given file periodically."""
    def __init__(self,fpath,interval,auto):
        """
        @param fpath: File path to output HTML (stack trace file)
        @param auto: Set flag (True) to update trace continuously.
            Clear flag (False) to update only if file not exists.
            (Then delete the file to force update.)
        @param interval: In seconds: how often to update the trace file.
        """
        assert(interval>0.1)
        self.auto = auto
        self.interval = interval
        self.fpath = os.path.abspath(fpath)
        self.stop_requested = threading.Event()
        threading.Thread.__init__(self)
    
    def run(self):
        while not self.stop_requested.isSet():
            time.sleep(self.interval)
            if self.auto or not os.path.isfile(self.fpath):
                self.stacktraces()
    
    def stop(self):
        self.stop_requested.set()
        self.join()
        try:
            if os.path.isfile(self.fpath):
                os.unlink(self.fpath)
        except:
            pass
    
    def stacktraces(self):
        fout = file(self.fpath,"wb+")
        try:
            fout.write(stacktraces())
        finally:
            fout.close()


_tracer = None
def trace_start(fpath,interval=5,auto=True):
    """Start tracing into the given file."""
    global _tracer
    if _tracer is None:
        _tracer = TraceDumper(fpath,interval,auto)
        _tracer.setDaemon(True)
        _tracer.start()
    else:
        raise Exception("Already tracing to %s"%_tracer.fpath)

def trace_stop():
    """Stop tracing."""
    global _tracer
    if _tracer is None:
        raise Exception("Not tracing, cannot stop.")
    else:
        _trace.stop()
        _trace = None


#------------------------------------------------

# Comentarios de debugging
import logging

if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)
    
logging.debug('Esto es un comentario de debug')
