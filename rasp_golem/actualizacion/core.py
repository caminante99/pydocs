# -*- coding: utf-8 -*-

class Mouse(object):
    def __init__(self):
        pass

    def click(self, x, y):
        from pymouse import PyMouse
        PyMouse().click(x, y)

    def double_click(self, x, y):
        from time import sleep
        from pymouse import PyMouse
        PyMouse().click(x, y)
        sleep(.1)
        PyMouse().click(x, y)

    def move(self, x, y):
        from pymouse import PyMouse
        PyMouse().move(x, y)

    def pos(self):
        from pymouse import PyMouse
        self.x_pos, self.y_pos = PyMouse().position()

    def click_between(self, x, y, width, height):
        ''' Cliquea en el centro de cuatro coordenadas '''
        from math import ceil
        x_fin = ceil((x + width) / 2)
        y_fin = ceil((y + height) / 2)
        self.click(x_fin, y_fin)
    
class HumanMouse(object):
    def __init__(self):
        # Get actual coordinates
        from pymouse import PyMouse
        self.x_pos, self.y_pos = PyMouse().position()
        
    ''' Función que toma una lista de números y convierte los decimales
    a enteros redondeando hacia arriba '''
    def _round_list(self, lista):
        response = []
        from math import ceil
        for elem in lista:
            r = ceil(elem)
            response.append(r)
        return response

    ''' Función para crear parabolas aleatorias en el movimimento
    del ratón para que parezca más humano '''
    def _aleat(self, lista):
        from random import randint
        aberturas = randint(1, 3)
        largo_abertura = randint(20, 25)
        ancho_abertura = len(lista) / aberturas - len(lista) / 15
        part = largo_abertura / ancho_abertura
        '''
        print('Largo %d, ancho %d, part %f' % (largo_abertura, ancho_abertura, part))
        '''
        # Primero sorteamos donde irán los centros de las aberturas
        posiciones_aberturas = []
        for a in range(aberturas):
            ab = randint(1, len(lista))
            posiciones_aberturas.append(ab)

        principios_y_finales = []
        for pos in posiciones_aberturas:
            principios_y_finales.append(pos - ancho_abertura)
            principios_y_finales.append(pos + ancho_abertura)

        
        response = []
        for n, elem in enumerate(lista):
            # Antes de aberturas
            if n < principios_y_finales[0]:
                response.append(elem)
                # Primera abertura
            elif n >= principios_y_finales[0] and n < posiciones_aberturas[0]:
                response.append(elem + (part * (n - principios_y_finales[0])))
            elif n >= posiciones_aberturas[0] and n < principios_y_finales[1]:
                response.append(elem + (part * (principios_y_finales[1] - n)))
            # Espacio tras la primera abertura
            elif n >= principios_y_finales[1] and aberturas == 1:
                response.append(elem)
    
            if aberturas > 1:
                # Antes de la segunda abertura
                if n < principios_y_finales[2]:
                    response.append(elem)
                    # Segunda abertura
                elif n >= principios_y_finales[2] and n < posiciones_aberturas[1]:
                    response.append(elem + (part * (n - principios_y_finales[2])))
                elif n >= posiciones_aberturas[1] and n < principios_y_finales[3]:
                    response.append(elem + (part * (principios_y_finales[3] - n)))
                # Espacio tras la segunda abertura
                elif n >= principios_y_finales[3] and aberturas == 2:
                    response.append(elem)
                    
                if aberturas > 2:
                    # Antes de la tercera abertura
                    if n < principios_y_finales[4]:
                        response.append(elem)
                        # Tercera abertura
                    elif n >= principios_y_finales[4] and n < posiciones_aberturas[2]:
                        response.append(elem + (part * (n - principios_y_finales[4])))
                    elif n >= posiciones_aberturas[2] and n < principios_y_finales[5]:
                        response.append(elem + (part * (principios_y_finales[5] - n)))
                    # Espacio tras la tercera abertura
                    elif n >= principios_y_finales[5] and aberturas == 3:
                        response.append(elem)
                            
        response = self._round_list(response)
        return response

    def _movement(self, x_fin, y_fin, vel=1):
        from pymouse import PyMouse
        x_in, y_in = PyMouse().position()
        if x_fin == x_in and y_fin == y_in:
            pass
        else:
            mov_x = abs(x_fin - x_in)
            mov_y = abs(y_fin - y_in)
            '''
            print('X = Desde %d hasta %d (mov = %d)' % (x_in, x_fin, mov_x))
            print('Y = Desde %s hasta %s (mov = %d)' % (y_in, y_fin, mov_y))
            '''
            lista_x = []
            lista_y = []

            from math import ceil
            
            # Posibilidades al crear la lista de x
            try:
                part = mov_x/mov_y
            except ZeroDivisionError:
                part = 0
            count = 0
             
            
            if x_fin >= x_in and mov_x >= mov_y:
                for x_temp in range(ceil(mov_x/vel)):
                    count += vel
                    lista_x.append(count + x_in)
                    
            elif x_fin < x_in and mov_x >= mov_y:
                for x_temp in range(ceil(mov_x/vel)):
                    count += vel
                    lista_x.append(x_in - count)
                    
            elif x_fin >= x_in and mov_x < mov_y:
                for x_temp in range(ceil(mov_y/vel)):
                    count += part * vel
                    lista_x.append(count + x_in)
                lista_x = self._round_list(lista_x)
                
            elif x_fin < x_in and mov_x < mov_y:
                for x_temp in range(ceil(mov_y/vel)):
                    count -= part * vel
                    lista_x.append(count + x_in)
                lista_x = self._round_list(lista_x)

            # Posibilidades al crear la lista de y
            try:
                part = mov_y/mov_x
            except ZeroDivisionError:
                part = 0
            count = 0
            
            if y_fin >= y_in and mov_y > mov_x:
                for y_temp in range(ceil(mov_y/vel)):
                    count += vel
                    lista_y.append(count + y_in)
                    
            elif y_fin < y_in and mov_y > mov_x:
                for y_temp in range(ceil(mov_y/vel)):
                    count += vel
                    lista_y.append(y_in - count)
                    
            elif y_fin >= y_in and mov_y < mov_x:
                for y_temp in range(ceil(mov_x/vel)):
                    count += part * vel
                    lista_y.append(count + y_in)
                lista_y = self._round_list(lista_y)
                
            elif y_fin < y_in and mov_y < mov_x:
                for y_temp in range(ceil(mov_x/vel)):
                    count -= part * vel
                    lista_y.append(count + y_in)
                lista_y = self._round_list(lista_y)

            ''' Metemos aleatoriedad en las listas '''
            if len(lista_x) > 100:
                lista_x = self._aleat(lista_x)
            if len(lista_y) > 100:
                lista_y = self._aleat(lista_y)

            ''' Iteramos sobre las dos listas a la vez '''
            for mov in zip(lista_x, lista_y):
                PyMouse.move(mov[0], mov[1])

    def move(self, x_fin, y_fin, velocity=4):
        if velocity > 2:
            if abs(self.x_pos - x_fin) < 150 or abs(self.y_pos - y_fin) < 150:
                velocity = 1
        self._movement(x_fin, y_fin, vel=velocity)
        if x_fin != self.x_pos or y_fin != self.y_pos:
            self._movement(x_fin, y_fin, vel=1)
                
    def click(self, x, y):
        from pymouse import PyMouse
        self.move(x, y)
        PyMouse().click(x, y)

    def click_der(self, x, y):
        from pyautogui import rightClick
        self.move(x, y)
        gui.rightClick(x, y)  

    def pos(self):
        return (self.x_pos, self.y_pos)

class Screen(object):
    def __init__(self):
        pass
        
    def size(self):
        from pyautogui import size
        response = size()
        return (response[0], response[1])

    def shot(self, region=None): #region es una tupla (x, y, ancho, alto)
        if region == None:
            from autopy import bitmap
            bitmap.capture_screen().save('img/screenshot.png')
        else:
            from pyautogui import screenshot
            screenshot('img/screenshot.png', region=region)

    # Busca un elemento en la pantalla y devuelve las coordenadas
    # tan sólo pon el nombre de una imagen que esté dentro de la carpeta img
    def find(self, img):
        from autopy import bitmap
        screen = bitmap.capture_screen()
        im = bitmap.Bitmap.open('img/' + img + '.png')
        pos = screen.find_bitmap(im)
        if pos:
            return pos
        else:
            return None

    def findall(self, img, reg=None):
        ''' Busca todas las imágenes pasadas como argumento en la pantalla.
        Se puede pasar una tupla como region para limitar la búsqueda a
        una region concreta y aumentar la velocidad (x, y, ancho, alto)
        El ancho y el alto son absolutos: ancho es x + ancho'''
        
        from pyautogui import locateAllOnScreen
        response = []
        if reg == None:
            for pos in locateAllOnScreen('img/' + img + '.png'):
                response.append((pos[0], pos[1], pos[0] + pos[2], pos[1] + pos[3]))
        else:
            for pos in locateAllOnScreen('img/' + img + '.png', region=(reg[0], reg[1], reg[2], reg[3])):
                response.append((pos[0], pos[1], pos[0] + pos[2], pos[1] + pos[3]))
        return response

    def while_not_found(self, img, exp=30):
        # Ejecuta un bucle hasta que encuentra el la imagen que se le pasa
        # como argumento (debe estar dentro de la carpeta img y en png.
        # Tambien necesita un tiempo de expiración
        # Retorna None si no lo encuentra y la posición en caso contrario
        from timeout import timeout, TimeoutError
        
        @timeout(exp)
        def whi(img):
            found = None
            while found == None:
                found = self.find(img)
        try:
            response = whi(img)
            return response
        except TimeoutError:
            print('La imagen %s no fue encontrada en menos de %d segundos en la funcion while_not_found()' % (img, exp))
            return None

    def find_more(self, *imgs):
        ''' Toma imágenes y retorna una lista con las posiciones de las
        imágenes en el orden que fueron recibidas. Si una imagen no la
        encuentra en su lugar de la lista retorna None '''

        responses = []
        for i in imgs:
            found = self.find(i)
            if found:
                responses.append(found)
            else:
                repsonses.append(None)
        if len(repsonses) == 1:
            return responses[0]
        else:
            return responses

    def where(self, *imgs):
        ''' Toma imágenes y devuelve el nombre de imagen la cual encuentra.
        Sirve para saber donde estamos, si ya nos hemos logueado en una
        página o no y cosas así.
        Si encuentra una imagen la devuelve en una cadena, si encuentra más
        las devuelve en una lista. '''
        
        responses = []
        for i in imgs:
            found = self.find(i)
            if found:
                responses.append(i)
        if len(responses) == 1:
            return responses[0]
        else:
            return responses

    def while_where(self, *imgs, exp=30):
        ''' Ejecuta un bucle while hasta que una de las imágenes pasadas
        como argumento aparece en pantalla, entonces devuelve su nombre'''
        from timeout import timeout, TimeoutError
        @timeout(exp)
        def whi(imgs):
            found = None
            while found == None:
                for i in imgs:
                    f = self.find(i)
                    if f != None:
                        f = i
                        break
                found = f
            return found

        try:
            response = whi(imgs)
            return response
        except TimeoutError:
            print('Han pasado más de %d segundos en la función while_where() para las imágenes: ' % exp, imgs)
            return None
            

    def click_center(self, img, human=False):
        ''' Click en el centro de una imagen.
        Por defecto cliquea con el mouse humano'''
        
        from PIL import Image
        from math import ceil
        im = Image.open('img/' + img + '.png')
        width, height = im.size
        pos_x, pos_y = self.find(img)
        x = ceil(pos_x + width / 2)
        y = ceil(pos_y + height / 2)
        if human == True:
            HumanMouse().click(x, y)
        else:
            Mouse().click(x, y)

    def when_found_click(self, img, human=False, exp=25):
        ''' Cuando encuentra la imagen hace click en el centro '''
        from timeout import timeout, TimeoutError
        from PIL import Image
        from math import ceil
        
        @timeout(exp)
        def when(img):
            found = None
            while found == None:
                found = self.find(img)
            return found    # pos
        try:
            pos_x, pos_y = when(img)
            im = Image.open('img/' + img + '.png')
            width, height = im.size
            x = ceil(pos_x + width / 2)
            y = ceil(pos_y + height / 2)
            if human == True:
                HumanMouse().click(x, y)
            else:
                Mouse().click(x, y)
        except TimeoutError:
            print('Ha caducado el tiempo de expiración en la función when_found_click() cargando la imagen %s' % img)

    # Consulta si un par de coordenadas están en pantalla
    def onScreen(self, x, y):
        from pyautogui import onScreen
        response = onScreen(x, y)
        return response

    # Retorna el color del pixel en x, y
    def pixel(self, x, y):
        from autopy import color, screen
        response = color.hex_to_rgb(screen.get_color(x, y))
        return response
    
    '''
    # Retorna las localizaciones de varias imágenes iguales
    def locateAll(self, elem):
        #gui.locateAllOnScreen
        response = ('img/' + str(elem) + '.png')
        return response
    '''

class Keyboard(object):
    def __init__(self):
        pass

    def press(self, key):
        from pyautogui import press
        press(key)

    def combine(self, *keys):
        ''' Una lista de teclas que serán pulsadas en el orden que vienen
        y soltadas en orden inverso, para hacer combinaciones como alt+f4 '''
        from pyautogui import keyDown, keyUp
        keys = list(keys)
        for k in keys:
            keyDown(k)
        keys.reverse()
        for k in keys:
            keyUp(k)

    def write(self, string, sleep=0.01):
        from pyautogui import press
        from time import sleep as s
        mayus = ['/']
        for ch in string:
            if ch in mayus or ch.isupper() == True:
                self.combine('shiftleft', ch)
            else:
                press(ch)
            s(sleep)
        

    def down(self):
        self.press('down')

    def up(self):
        self.press('up')

    def av_pag(self):
        self.press('pagedown')

    def re_pag(self):
        self.press('pageup')

    def enter(self):
        self.press('enter')

    def tab(self, num=1, sleep=0.1):
        ''' Presiona la tecla tab el número de veces
        que le pasamos como argumento num '''
        from time import sleep as s
        self.press('tab')
        s(sleep)
        
    def keys(self):
        list_keys = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
        ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
        'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
        'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
        'browserback', 'browserfavorites', 'browserforward', 'browserhome',
        'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
        'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
        'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
        'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
        'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
        'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
        'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
        'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
        'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
        'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
        'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
        'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
        'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
        'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
        'command', 'option', 'optionleft', 'optionright']
        # backspace es el botón de borrar
        return list_keys

class HumanKeyboard(object):
    def __init__(self):
        pass

    def _random_decimal(self, i, d):
        from random import randint
        return float('0.%00d' % randint(0,d))
    
    def write(self, string):
        ''' Escribir por teclado emulando al ser humano.
        Incluye equivocaciones de letras que se borran
        y se vuelven a escribir. Hay que mejorarlo para
        incluir equivocaciones de más teclas'''
        from pyautogui import press
        from time import sleep as s
        from random import randint
        from pyperclip import copy
        from medium_level import Utils
        
        letters = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z']
        
        mayus = ['/']
        excepciones = ['á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í',
                       'Ó', 'Ú', '@']
        for ch in string:
            # Equivocaciones de una letra
            wrong_letter = False
            prob = randint(0, 25)
            if prob == 25:
                if ch in letters:
                    letters.remove(ch)
                ch_save = ch
                ch = letters[randint(0, len(letters) - 1)]
                letters.append(ch)
                wrong_letter = True

            # Pulsación de tecla
            if ch in mayus or ch.isupper() == True:
                Keyboard().combine('shiftleft', ch)
            elif ch in excepciones:
                Utils().paste_save(ch)
            else:
                press(ch)
            if wrong_letter == True:
                sleep = self._random_decimal(0, 65)
                s(sleep)
                press('backspace')
                if ch_save in mayus or ch.isupper() == True:
                    Keyboard().combine('shiftleft', ch)
                elif ch_save in excepciones:
                    Utils().paste_save(ch_save)
                else:
                    press(ch_save)
                
            # Mayor profundidad de azar en los tiempos de espera
            # entre letras
            maxim = 1
            prob = randint(0, 6)
            if prob > 4:
                maxim = 2
            sleep = self._random_decimal(0, maxim)
            s(sleep)  

class Window(object):
    def __init__(self):
        pass
    
    def active(self):
        ''' Retorna la id de la ventana activa '''
        from xdo import Xdo
        response = Xdo().get_active_window()
        return response

    def get_name(self, win_id):
        ''' Retorna el nombre de la ventana que recibe como id '''
        from xdo import Xdo
        from re import sub
        from json import loads
        name = Xdo().get_window_name(win_id)
        name = sub(r"^b'|'*$", '', str(name))
        substituciones = {r'\\xc3\\xb1': 'ñ', r'\\xc3\\xad': 'í'}
        for pat, repl in substituciones.items():
            name = sub(pat, repl, name)
        return name

    def active_name(self):
        ''' Retorna el nombre de la ventana activa '''
        window = self.active()
        response = self.get_name(window)
        return response
    
    def while_active_not_name(self, *names, exp=25):
        ''' Ejecuta un bucle while que se rompe cuando
        la ventana activa es una de las ventanas pasadas como args.
        Se le puede pasar un número indefinido de ventanas
        Se le puede pasar un tiempo de expiración
        Devuelve el nombre de la ventana si la encuentra y None si no'''
        from timeout import timeout, TimeoutError
        
        @timeout(exp)
        def whi(names):
            string = self.active_name()
            while string not in names:
                string = self.active_name()
            return string
        try:
            response = whi(names)
            return response
        except TimeoutError:
            if len(names) == 1:
                print('La ventana %s no ha sido hallada como activa en %d segundos' % (names, exp))
            else:
                print('Ninguna de las ventanas han sido halladas como activa en %d segundos' % exp)
            return None
        
    def minimize(self):
        ''' Solo funciona en la ventana activa '''
        from time import sleep
        Keyboard().combine('alt', 'space')
        for d in range(6):
            Keyboard().down()
            sleep(.01)
        Keyboard().enter()

    def maximize(self):
        ''' Solo funciona en la ventana activa '''
        from time import sleep
        Keyboard().combine('alt', 'space')
        for d in range(7):
            Keyboard().down()
            sleep(.01)
        Keyboard().enter()
        sleep(0.01)
        Keyboard().press('esc')

    def close_active(self):
        Keyboard().combine('alt', 'f4')
        
