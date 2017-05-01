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

    # El método run de una clase threading.Thread funciona al llamarla
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

''' Cómo usar el timeout (expirador):

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
