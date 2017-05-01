''' Capa de medio nivel con funciones específicas'''


class Utils(object):
    ''' Utilidades como abrir programas desde run o copiar y pegar '''
    def __init__(self):
        pass

    # -------------- PORTAPAPELES ----------------

    def copy(self, st):
        from pyperclip import copy
        copy(st)

    def paste(self):
        ''' Retorna lo que hay pegado en el portapapeles '''
        from pyperclip import paste
        response = paste()
        return response

    def paste_save(self, string):
        ''' Pegar algo salvando en el portapapeles lo que estaba copiado
        Para introducir con mayor velocidad que escribiendo desde teclado'''
        from core import Keyboard
        save = self.paste()
        self.copy(string)
        Keyboard().combine('ctrl', 'v')


    # ---------------- COMANDOS EN CONSOLA -------------------

    def poweroff(self):
        ''' Apagar la raspberry inmediatamente '''
        import shlex
        from subprocess import call
        command_line = 'sudo poweroff'
        args = shlex.split(command_line)
        call(args)

    def restart(self):
        ''' Reiniciar la raspberry '''
        import shlex
        from subprocess import call
        command_line = 'sudo reboot'
        args = shlex.split(command_line)
        call(args)

    def open_bash(self):
        ''' Abrir la consola del sistema en la pantalla '''
        from core import Keyboard
        Keyboard().combine('ctrl', 'alt', 't')

    # ---------------- COMANDOS EJECUTAR ---------------------
    
    def open_run(self):
        ''' Abrir la consola run '''
        from core import Keyboard
        Keyboard().combine('alt', 'f2')

    def start_run(self, command):
        ''' Abrir la consola run y ejecutar un programa pasado como arg'''
        from core import Window, Keyboard
        self.open_run()
        Window().while_active_not_name('Ejecutar')
        self.paste_save(command)
        Keyboard().enter()
        
    def ksnapshot(self):
        ''' Abrir el programa ksnapshot '''
        self.start_run('ksnapshot')

    # --------------- TESTEOS -------------------------------

    def test(self, img, win):
        ''' Asegurarnos de que hemos entrado a un contexto
        comprobando mediante una imagen en pantalla y el nombre
        de la ventana activa. Toma dos cadenas con el nombre
        de la ventana y de la imagen que esperamos.
        Devuelve True si el testeo es correcto y False si no'''
        from core import Window, Screen
        im_name = Screen().where(img)
        win_name = Window().active_name()
        if img == im_name and win == win_name:
            return True
        else:
            return False

    def test_while(self, img, win, exp=25):
        ''' Ejecuta un bucle while hasta que el nombre de
        la ventana activa y de la imagen en pantalla son las que
        hemos pasado '''
        from timeout import timeout, TimeoutError

        @timeout(exp)
        def testing(img, win):
            names = self.test(img, win)
            while names != True:
                names = self.test(img, win)
        try:
            testing(img, win)
            return True
        except TimeoutError:
            print('No se han encontrado la imagen %s y la ventana %s' % (img, win))
            return False

class Chromium(object):
    def __init__(self):
        pass

    def start(self, url='https://www.google.es'):
        ''' Abrimos el navegador con la página de inicio de google Spain '''
        import webbrowser
        webbrowser.open(url)

    def bar_directions(self):
        ''' Nos colocamos en la barra de direcciones '''
        from core import Keyboard
        Keyboard().press('f6')

    def go_to(self, url):
        ''' Vamos a la url que le pasamos como argumento '''
        from core import Keyboard
        from time import sleep
        Keyboard().press('f6')
        sleep(1.5)
        Utils().paste_save(url)
        sleep(.5)
        Keyboard().enter()
