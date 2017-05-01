# -*- coding: utf-8 -*-

import sys, webbrowser
import config, llamadas, trade_layer, trade
from core import calculos

base = llamadas.Base_datos()

def saludo():
    print 'Hola, soy ' + config.nombre + ' ' + config.version + ', bot de trading en Poloniex configurable por módulos.'
    print

# Accionador del programa
def empezar():
    comienzo = raw_input('¿Quieres empezar el trading? s/n: ')
    if comienzo == 'n':
        confirmar = raw_input('¿Entonces quieres salir? s/n: ')
        if confirmar == 's':
            print 'Nos vemos otro dia'
            sys.exit(0)
        elif confirmar == 'n':
            empezar()
    elif comienzo == 's':
        print 'Puedes pausar la compra/venta en cualquier momento pulsando Ctrl+C'
        print
        pass
    
# Vemos donde irán los checkpoints y preguntamos si está seguro
def ver_checkpoints():
    base.borrar_checkpoints()                           # Borramos los checkpoints anteriores
    checkpoints = trade_layer.definir_checkpoints()            # Una lista con los checkpoints calculados
    print
    trade_layer.guardar_checkpoints(checkpoints)            # Guardamos los checkpoints en la base de datos
    soporte_min = float(base.mostrar_margen('soporte', 'minimo'))
    soporte_max = float(base.mostrar_margen('soporte', 'maximo'))
    print
    print 'Los checkpoints se colocarán de la siguiente forma:'
    count = 1
    for i in checkpoints:
        print 'Número ' + str(count) + ' = ' + str(i) + ' (al ' + str(calculos.porcentaje_diferencia(calculos.media(soporte_min, soporte_max), i)) + '%)'
        count += 1
    print
    
def ver_stoploss():
    precio_compra = calculos.media(float(base.mostrar_margen('soporte', 'minimo')), float(base.mostrar_margen('soporte', 'maximo')))
    print 'El precio de compra aproximado es ' + str(precio_compra)
    stop_loss = calculos.porcentaje_resta(float(config.stop_loss), float(precio_compra))
    if base.mostrar_stoploss() == None:
        base.insertar_stoploss(str(stop_loss))
    else:
        base.actualizar_stoploss(str(stop_loss))
    print 'El stop-loss se colocará en', stop_loss
    print
    print '(Puedes cambiar el número de checkpoints y el porcentaje de stop-loss en /modules/config.py)'
    print
    

# Configurador inicial del programa
def configuracion_inicial():
    moneda_anterior = base.mostrar_moneda()
    if base.mostrar_moneda() != None:
        print 'Vas a tradear en el mercado de:', moneda_anterior
        configurar = raw_input('¿Quieres cambiar de mercado? s/n: ')
        if configurar == 's':
            moneda = raw_input('Inserta el mercado donde quieres tradear: ').upper()
            base.actualizar_moneda(moneda)
        elif configurar == 'n':
            moneda = moneda_anterior
    else:
        moneda = raw_input('Inserta el mercado donde quieres tradear: ').upper()
        base.insertar_moneda(moneda)
    try: 
        llamadas.balance(moneda, 'available')
    except AttributeError or KeyError:
        print 'Te has equivocado escribiendo el mercado'
        moneda = raw_input('Inserta el mercado donde quieres tradear: ').upper()
        base.actualizar_moneda(moneda)
    print
    print 'Antes de empezar el trading...'
    print '...vamos a configurar los márgenes de soporte y resistencia.'
    print
    if base.mostrar_margen('soporte', 'minimo') == None:
        print 'Si quieres acceder al mercado de ' + moneda + ' en Poloniex, teclea: info'
        print
        soporte_min = raw_input('Rango mínimo de soporte: ')
        if soporte_min == 'info':
            webbrowser.open_new_tab('http://www.poloniex.com/exchange#btc_' + base.mostrar_moneda().lower())
            print
            print 'Abriendo el mercado en Poloniex...'
            print
            configuracion_inicial()
        soporte_max = input('Rango máximo de soporte: ')
        resistencia_min = input('Rango mínimo de resistencia: ')
        resistencia_max = input('Rango máximo de resistencia: ')
        base.insertar_margen('resistencia', resistencia_min, resistencia_max)
        base.insertar_margen('soporte', soporte_min, soporte_max)
    else:
        print 'Estos son los antiguos rangos (fueron configurados para ' + str(moneda_anterior) +'): '
        print
        print base.mostrar_margenes()
        print
        actualizar_rangos = raw_input('¿Deseas actualizarlos? s/n: ')
        if actualizar_rangos == 'n':
            pass
        elif actualizar_rangos == 's':
            print
            print 'Si quieres acceder al mercado de ' + moneda + ' en Poloniex, teclea: info'
            print
            soporte_min = raw_input('Rango mínimo de soporte: ')
            if soporte_min == 'info':    
                webbrowser.open_new_tab('http://www.poloniex.com/exchange#btc_' + base.mostrar_moneda().lower())
                print
                print 'Abriendo el mercado en Poloniex...'
                print
                configuracion_inicial()
            soporte_max = input('Rango máximo de soporte: ')
            resistencia_min = input('Rango mínimo de resistencia: ')
            resistencia_max = input('Rango máximo de resistencia: ')
            base.actualizar_margenes('soporte', soporte_min, soporte_max)
            base.actualizar_margenes('resistencia', resistencia_min, resistencia_max)

#-----------------------------------------------------------

# Estas funciones se lanzan si el usuario pulsa Ctrl+C en el trade de compra o de venta
def pausar_trade_venta():
    pausa = raw_input('¿Quieres detener el trading? s/n: ')
    if pausa == 's':
        print
        print 'Vas a detener la venta, se abrirá poloniex automáticamente para dejarlo todo amarrado'
        print
        print '¡Hasta la próxima!'
        webbrowser.open_new_tab('http://www.poloniex.com/exchange#btc_' + base.mostrar_moneda().lower())
        base.cerrar()   # Cerramos la base de datos
        sys.exit(0)
    elif pausa == 'n':
        reanudar = raw_input('¿Entonces quieres reanudarlo? s/n: ')
        if reanudar == 's':
            print 'Volviendo al punto donde estaba realizándose el trading...'
            trade.organizador()
        if reanudar == 'n':
            pausar_trade_venta()
            
def pausar_trade_compra():
    pausa = raw_input('¿Quieres detener el trading? s/n: ')
    if pausa == 's':
        print
        print 'Vas a detener la compra, asegúrate de no dejar compras abiertas sin sentido'
        print 
        print '¡Hasta la próxima!'
        base.cerrar()   # Cerramos la base de datos
        sys.exit(0)
    elif pausa == 'n':
        reanudar = raw_input('¿Entonces quieres reanudarlo? s/n: ')
        if reanudar == 's':
            print 'Volviendo al punto donde estaba realizándose el trading...'
            trade.organizador()
        if reanudar == 'n':
            pausar_trade_venta()
