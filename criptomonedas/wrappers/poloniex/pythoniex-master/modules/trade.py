# -*- coding: utf-8 -*-

import time, sys
import urllib2
from core import calculos
from wrappers import poloniex
import llamadas, trade_layer, avisos, config, funcionamiento, wifi_conexion

base = llamadas.Base_datos()
api = poloniex.poloniex(config.keypublic, config.keysecret)

def venta():
    moneda = str(base.mostrar_moneda())
    soporte_min = float(base.mostrar_margen('soporte', 'minimo'))
    soporte_max = float(base.mostrar_margen('soporte', 'maximo'))
    soporte_inicial = calculos.media(soporte_min, soporte_max)     # Calcula el soporte inicial para actualizar la primera subida de stoploss
    total_compra = api.returnTradeHistory('BTC_' + moneda)[0]['total'] # Cogemos el precio al que compramos
    cantidad_compra = api.returnTradeHistory('BTC_' + moneda)[0]['amount']
    precio_compra = api.returnTradeHistory('BTC_' + moneda)[0]['rate']
    precio = llamadas.precio(base.mostrar_moneda(), 'bids')['precio']
    print 'DEP: Obtenemos las constantes de venta'    
    if base.mostrar_check_actual() == None:
        base.insertar_check_actual('1')       # Inserta en la base el checkpoint donde estamos (1)
    else:                            # a no ser que ya exista un check_actual
        base.actualizar_check_actual('1')     # en ese caso actualízalo por (1)
        print 'DEP: Insertamos en la base el primer check_actual y entramos al bucle de venta'
    while float(base.mostrar_stoploss()) < float(precio):  # Mientras no salte el stop loss (movil o de protección)
        try:        
            precio_mercado = llamadas.precio(moneda, config.vender)['precio']             # Cogemos el precio de compras
            print 'Precio de mercado: ' + str(precio_mercado) + ',(compraste a ' + str(precio_compra) + ')'
            if float(precio_mercado) > float(base.mostrar_checkpoint(str(base.mostrar_check_actual()))): # Si el precio de mercado es mayor que el checkpoint actual
                if base.mostrar_check_actual() == '1':
                    base.actualizar_stoploss(str(trade_layer.subir_stoploss(soporte_inicial, str(base.mostrar_checkpoint(1))))) #Subimos el stoploss
                    stop_loss = base.mostrar_stoploss()
                    print 'DEP: El check_actual == 1, subimos el stop_loss a ' + str(stop_loss)
                else:
                    base.actualizar_stoploss(str(trade_layer.subir_stoploss(base.mostrar_checkpoint(str(int(base.mostrar_check_actual()) - 1)), float(base.mostrar_checkpoint(str(base.mostrar_check_actual()))))))
                    stop_loss = base.mostrar_stoploss()
                    print 'DEP: Subimos el stop_loss a ' + str(stop_loss)
                if config.enviar_mails_checkpoint == True:
                    venta_total_stop_loss = (float(stop_loss) * float(cantidad_compra)) - (float(stop_loss) / 400)
                    avisos.ganancia_relativa(str(venta_total_stop_loss), str(total_compra))
                    print 'DEP: Avisamos por mail de la ganacia relativa '
                else:
                    pass
                base.actualizar_check_actual(str(int(base.mostrar_check_actual()) + 1))     # Nos vamos al siguiente check_actual
                print 'DEP: Actualizamos el check_actual a ' + base.mostrar_check_actual()
                llamadas.venta(base.mostrar_moneda(), llamadas.precio(base.mostrar_moneda(), config.vender), float(llamadas.balance(base.mostrar_moneda(), 'available')))
            else:
                print 'DEP: Precio < check_actual (' + str(base.mostrar_checkpoint(base.mostrar_check_actual())) + '), esperamos ' + str(config.espera) + ' segundos'
                print 'Stoploss: ' + str(base.mostrar_stoploss())
                time.sleep(int(config.espera))
        except KeyboardInterrupt:
            print 'Vas a detener el proceso de venta'
            print 'El programa no guardará el stop-loss actual'
            print 'Si deseas guardarlo deberás configurarlo manualmente desde http://www.poloniex.com'
            print 
            funcionamiento.pausar_trade_venta()
    print 'DEP: El stop loss ha saltado, comprobamos si es rentable vender a precio de mercado'
    estimacion_venta = float(llamadas.precio(moneda, config.vender)['precio']) * float(llamadas.balance(moneda, 'available'))
    if float(estimacion_venta - (estimacion_venta / 400)) > float(total_compra):    # Si la venta a precio de mercado con comisiones es rentable
        print 'DEP: Parece que es rentable, intentamos vender'
        respuesta = llamadas.venta(base.mostrar_moneda(), str(llamadas.precio(base.mostrar_moneda(), config.vender)), float(llamadas.balance(base.mostrar_moneda(), 'available'))) # Vende a precio de mercado
        print respuesta
        id_venta = respuesta[0]['orderNumber']
    else:               # Si no,pueden suceder dos cosas
        if float(llamadas.precio(moneda, config.vender)['precio']) < float(calculos.porcentaje_resta(config.stop_loss, calculos.media(base.mostrar_margen('soporte', 'minimo'), base.mostrar_margen('soporte', 'maximo')))):  # Que la venta haya caído por debajo del stop loss de protección
            print 'DEP: El precio ha caído por debajo del stoploss de protección'
            respuesta = llamadas.venta(base.mostrar_moneda(), str(llamadas.precio(base.mostrar_moneda(), 'bids')), float(llamadas.balance(base.mostrar_moneda(), 'available'))) # Vende desesperadamente a precio de compra
            print respuesta            
            id_venta = respuesta[0]['orderNumber']
        else:           # O que no haya caído por debajo del stop de protección, en ese caso
            venta()     # Vuelve a comenzar el bucle para redefinir el stop_loss movil (Esto se hace para defendernos de falsas caídas o de ordenes de compra en solitario cercanas al precio de venta que desaparecen de repente)
    print 'DEP: Esperamos 5 segundos a que el servidor procese la orden'
    time.sleep(5)       # Duerme 8 segundos para que el servidor procese la orden
    estado = 'en_proceso'
    while estado == 'en proceso':
        try:
            api.returnOpenOrders('BTC_' + moneda)[0]  # Si hay orden abierta todavía
            print 'DEP: La orden sigue abierta, esperamos 7 segundos' 
            time.sleep(7)           # Esto se hace para evitar que la venta no se haya cumplido por bajadas fuertes del mercado
            try:
                api.returnOpenOrders('BTC_' + moneda)[0]   # Si tras 7 segundos no se ha vendido
                print 'DEP: Aún no se ha vendido, cancelamos la orden volvemos a lanzar la función de venta'
                api.cancel('BTC_' + moneda, str(id_venta)) 
                venta()
            except IndexError:
                estado = 'vendido'
        except IndexError:
            estado = 'vendido'
    print 'DEP: La venta se ha realizado'
    if config.enviar_mails_operacion == True:
        informacion = llamadas.ultimo_trade(moneda)     # Cogemos la información de la venta
        avisos.operacion(informacion)            #Avisamos al correo de la venta efectuada
        print 'DEP: Enviando mail de aviso de venta'
    else:
        pass
    print 'DEP: LA DEPURACION DE LA VENTA SE HA COMPLETADO CORRECTAMENTE'
    if config.reiniciar == True:                               # Comprobamos si está el reinicio automático activado
        print 'DEP: El reinicio automático está activado, así que volvemos a comprar'
        organizador()
    else:
        print 'El reinicio automático esta desactivado, cerrando el programa...'
        print '¡Hasta la próxima!'
        base.cerrar()   # Cerramos la base de datos
        sys.exit(0)
    
#Bucle de compra
def compra():
    moneda = str(base.mostrar_moneda())
    print 'DEP: Obtenemos las constantes de compra'
    estado = 'en_proceso'
    while estado == 'en_proceso':
        try:
            if calculos.rango(str(llamadas.precio(moneda, config.comprar)['precio']), base.mostrar_margen('soporte', 'minimo'), base.mostrar_margen('soporte', 'maximo')) == True:  #Si el precio de venta/compra actual está en el rango de soporte
                print 'DEP: El precio de ' + moneda + ' (' + str(llamadas.precio(moneda, 'asks')['precio']) + ') está en el rango de soporte, intentamos comprar'   
                cantidad = float(llamadas.balance('BTC', 'available')) / (float(llamadas.precio(moneda, config.comprar)['precio']) + 0.00000001)  # La cantidad que vamos a comprar
                try:
                    respuesta = api.returnOpenOrders('BTC_' + moneda)[0]
                except IndexError:
                    # Significa que no hay ordenes abiertas
                    pass
                try:
                    id_compra = str(respuesta['orderNumber'])
                    print 'DEP: La compra esta abierta, la id es :' + str(id_compra)
                except IndexError or KeyError:
                    respuesta = api.buy('BTC_' + moneda, str(float(llamadas.precio(moneda, config.comprar)['precio']) + 0.00000001), str(cantidad))   #Compramos a precio de compra y nos quedamos con la id de la transacción
                    try:
                        id_compra = str(respuesta['orderNumber'])
                        print 'DEP: Abrimos la compra a ' + str(api.returnOpenOrders('BTC_' + moneda)[0]['rate']) + ', la id es :' + str(id_compra)
                    except IndexError or KeyError:
                        pass
                if llamadas.orden_abierta(moneda) == True:    #Mientras haya una orden abierta
                    print 'DEP: Esperamos  ' + str(config.espera) + ' segundos a que la compra se efectúe'                
                    time.sleep(config.espera)                          #Espera 30 segundos y repite el bucle hasta que ya no haya orden abierta
                    if llamadas.orden_abierta(moneda) == True:      # Si tras ese tiempo sigue abierta
                        print 'Cancelamos la compra y volvemos a empezar'
                        api.cancel('BTC_' + moneda, str(id_compra))      # Cancélala y vuelve a empezar el bucle
                        compra()
                    else:
                        pass
                else:
                    pass
                print 'DEP: La compra se ha efectuado'
                estado = 'comprado'
            else:                       #Si el precio de venta actual no está en el rango de soporte
                print 'El precio de compra actual de ' + moneda + ' no está en el rango de soporte (' + str(llamadas.precio(moneda, config.comprar)['precio']) + ' BTC)'
                print 'Pythoniex intentará comprar cuando llegue, ten paciencia...'
                print
                if calculos.rango(str(llamadas.precio(moneda, config.comprar)['precio']), base.mostrar_margen('soporte', 'minimo'), base.mostrar_margen('soporte', 'maximo')) == False:             
                    time.sleep(10)          #El programa duerme 10 segundos y vuelve a empezar el bucle While, para intentar de nuevo la compra
                    compra()
        except KeyboardInterrupt:
            print 'Vas a detener el proceso de compra'
            print
            funcionamiento.pausar_trade_compra()
    informacion = llamadas.ultimo_trade(moneda)     # Cogemos la información de la compra
    print 'DEP: Cogemos la información de la compra'    
    avisos.operacion(informacion)       # Avisamos al correo de la compra efectuada
    print 'DEP: Avisamos al correo de la compra efectuada'
    print 'DEP: Aquí lanzaríamos la función de venta'
    print
    print 'LA DEPURACION DE COMPRA SE HA COMPLETADO CORRECTAMENTE, PASAMOS AL BLOQUE DE VENTA'
    venta()       #Cuando se rompe el bucle lanzamos la función de venta

# Organiza el estado del programa y envia el trade a su bucle correspondiente
def organizador():
    try:
        base.insertar_id('compra', '0')     # Insertamos los ids de compra y venta en la base
        base.insertar_id('venta', '0')      # Así luego sólo debemos actualizarlos
        moneda = base.mostrar_moneda()
        print 'DEP: El organizador toma la moneda'
        try:
            api.returnOpenOrders('BTC_' + moneda)[0]     # Comprueba que hay una orden abierta, si la hay
            print 'Hay una orden abierta de ' + str(llamadas.tipo_orden(moneda)) + ' de ' + moneda + ' a ' + str(api.returnOpenOrders('BTC_' + moneda)[0]['rate']) + ' BTC'
            if api.returnOpenOrders('BTC_' + base.mostrar_moneda())[0]['type'] == 'buy': # Si es una orden de compra
                print 'DEP: Entramos en la función de compra'
                compra()
            else:
                print 'DEP: Entramos en la función de venta'
                venta()
        except IndexError:          # Si no la hay
            print 'No hay órdenes abiertas'
            if float(llamadas.balance(moneda, 'available')) == 0 and float(llamadas.balance('BTC', 'available')) > config.min_btc:
                print 'DEP: Entramos en la función de compra'
                compra()
            elif float(llamadas.balance('BTC', 'available')) < config.min_btc and float(llamadas.balance(moneda, 'available')) > 0:
                print 'DEP: Entramos en la función de venta'
                venta()
    except urllib2.URLError:
        print 'No se ha podido contactar con Poloniex, comprobando la conexion...'
        conexion = wifi_conexion.red()
        if conexion == False:
            print 'Intentando reconectar...'
            print 'Aún no hay un módulo instalado que permita reconectarse a la red'
        else:
            organizador()
# Bucle principal
def trade():
    print '¿Qué quieres hacer?'
    print '1.Comprar - 2.Vender - 3.Dejar elegir a Pythoniex'
    eleccion = raw_input('Inserta un número: ')
    if eleccion == '1':
        compra()
    elif eleccion == '2':
        venta()
    elif eleccion == '3':       
        organizador()
    else:
        print 'Te has equivocado de numero'
        trade()
        
#print llamadas.precio('BTC_' + 'LSK', 'bids')
#print llamadas.balance('MAID', 'available')
        
        
