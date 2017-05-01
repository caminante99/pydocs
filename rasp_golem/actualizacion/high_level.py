

def abrir_chromium(exp=30, url='https://www.google.es', test_img='google/google', test_win='Google - Chromium'):
    ''' Abrimos Chromium con un testeo de ventana y otro por imagen '''
    from shlex import split 
    import threading as t
    from core import Window, Screen
    from medium_level import Chromium    
    from timeout import timeout
    from xdo import xdo
    from time import sleep
    
    #xdo.xdo.XdoException: Function xdo_get_active_window returned error code 1
    
    def op():
        # Este será el demonio, se terminará cuando nos hayamos
        # asegurado de que chromium está abierto con la otra función
        Chromium().start(url=url)
        
    @timeout(exp)
    def test_if_open():
        # Abrimos la ventana y comprobamos si se ha abierto el error del perfil
        Window().while_active_not_name(test_win, 'Se ha producido un error del perfil')
        ventana = Window().while_active_not_name(test_win, 'Se ha producido un error del perfil')
        if ventana == 'Se ha producido un error del perfil':
            Window().close_active()

    op = t.Thread(target=op, daemon=True, name='Abrir Chromium')
    test = t.Thread(target=test_if_open, name='Test Abrir Chromium')
    try:
        op.start()
        test.start()
        ''' Comprobamos si están abiertos los hilos '''
        alive = True
        while alive == True:
            alive = test.is_alive()
        Window().maximize()
    except timeout.TimeoutError:
        print('El tiempo de abertura de Chromium ha sido superior a %s segundos' % exp)
    except xdo.XdoException:
        print('Excepción en la biblioteca Xdo: Function xdo_get_active_window returned error code 1')
        Window().maximize()
    if test_img:
        Screen().while_not_found(test_img)
    

