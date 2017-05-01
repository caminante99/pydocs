# -*- coding: cp1252 -*-

class FetchUrls(threading.Thread):
    """
    Thread checking URLs.
    """

    def __init__(self, urls, output):
        """
        Constructor.

        @param urls list of urls to check
        @param output file to write urls output
        """
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
    
    def run(self):
        """
        Thread run method. Check URLs one by one.
        """
        while self.urls:
            url = self.urls.pop()
            req = urllib2.Request(url)
            try:
                d = urllib2.urlopen(req)
            except urllib2.URLError, e:
                print 'URL %s failed: %s' % (url, e.reason)
            self.output.write(d.read())
            print 'write done by %s' % self.name
            print 'URL %s fetched by %s' % (url, self.name)

# The main function starts the 2 threads and then wait for them to finish.

def main():
    # list 1 of urls to fetch
    urls1 = ['http://www.google.com', 'http://www.facebook.com']
    # list 2 of urls to fetch
    urls2 = ['http://www.yahoo.com', 'http://www.youtube.com']
    f = open('output.txt', 'w+')
    t1 = FetchUrls(urls1, f)
    t2 = FetchUrls(urls2, f)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()

if __name__ == '__main__':
    main()
    
'''
The issue is that both threads are going to write to the file at the same
time, resulting in a big mess. We need to find a way to only have
1 thread writing to the file at a given time. To do that, one way
is to use synchronization mechanisms like locks.'''


# Lock

''' Locks have 2 states: locked and unlocked. 2 methods are
used to manipulate them: acquire() and release(). Those are the rules:

    if the state is unlocked: a call to acquire() changes the state to locked.
    if the state is locked: a call to acquire() blocks until another thread calls release().
    if the state is unlocked: a call to release() raises a RuntimeError exception.
    if the state is locked: a call to release() changes the state to unlocked().

To solve our issue of 2 threads writing to the same file at the same time,
we pass a lock to the FetchUrls constructor and we use it to protect
the file write operation. I am just going to highlight the modifications
relevant to locks. The source code can be found in threads/lock.py.
'''
class FetchUrls(threading.Thread):
    ...

    def __init__(self, urls, output, lock):
        ...
        self.lock = lock
    
    def run(self):
        ...
        while self.urls:
            ...
            self.lock.acquire()
            print 'lock acquired by %s' % self.name
            self.output.write(d.read())
            print 'write done by %s' % self.name
            print 'lock released by %s' % self.name
            self.lock.release()
            ...

def main():
    ...
    lock = threading.Lock()
    ...
    t1 = FetchUrls(urls1, f, lock)
    t2 = FetchUrls(urls2, f, lock)
    ...


''' Let’s look at the program output when we run it: '''
$ python locks.py
lock acquired by Thread-2
write done by Thread-2
lock released by Thread-2
URL http://www.youtube.com fetched by Thread-2
lock acquired by Thread-1
write done by Thread-1
lock released by Thread-1
URL http://www.facebook.com fetched by Thread-1
lock acquired by Thread-2
write done by Thread-2
lock released by Thread-2
URL http://www.yahoo.com fetched by Thread-2
lock acquired by Thread-1
write done by Thread-1
lock released by Thread-1
URL http://www.google.com fetched by Thread-1

''' You can also use the “with” statement. The Lock object can be used
as a context manager. The advantage of using “with” is that the acquire()
method will be called when the “with” block is entered and release()
will be called when the block is exited. Let’s rewrite the class
FetchUrls using the “with” statement. '''

#---------------------------------------------------------

# RLock

'''
RLock is a reentrant lock. acquire() can be called multiple times
by the same thread without blocking. Keep in mind that release()
needs to be called the same number of times to unlock the resource.

Using Lock, the second call to acquire() by the same thread will block: '''
lock = threading.Lock()
lock.acquire()
lock.acquire()

'''
If you use RLock, the second call to acquire() won’t block. '''

rlock = threading.RLock()
rlock.acquire()
rlock.acquire()
