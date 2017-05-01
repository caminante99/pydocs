# -*- coding: utf-8 -*-

import sqlite3
import config
from wrappers import poloniex

# LLAMADAS
# Hace llamadas a la base de datos y a la API
#_________________________________

# BASE DATOS

#Conexion a la base de datos e insertar informacion
ruta = config.ruta_base_datos

class Base_datos:
    def __init__(self):
        self.con = sqlite3.connect(ruta)
        self.cursor = self.con.cursor()
        
    def crear_tabla_margenes(self):
        self.cursor.execute('''CREATE TABLE MARGENES
            (TIPO CHAR(50) NOT NULL,
            VALOR_MIN DOUBLE NOT NULL,
            VALOR_MAX DOUBLE NOT NULL)''')
        
    def crear_tabla_moneda(self):
        self.cursor.execute('''CREATE TABLE MONEDA
            (MONEDA CHAR(50) null)''')
            
    def crear_tabla_estado(self):
        self.cursor.execute('''CREATE TABLE ESTADO
            (ESTADO CHAR(50) null)''')
            
        # El tipo de id puede ser de compra o de venta
    def crear_tabla_id(self):
        self.cursor.execute('''CREATE TABLE ID
            (COMPRA INT null,
            VENTA INT null)''')

    def crear_tabla_checkpoints(self):
        self.cursor.execute('''CREATE TABLE CHECKPOINTS
            (NUMERO INT null,
            VALOR DOUBLE null) ''')
    
    # Esta tabla guarda el checkpoint sobre el que nos encontramos actualmente
    def crear_tabla_check_actual(self):
        self.cursor.execute('''CREATE TABLE CHECK_ACTUAL
            (CHECK_ACTUAL CHAR(50) null)''')
            
    def crear_tabla_stoploss(self):
        self.cursor.execute('''CREATE TABLE STOPLOSS
            (STOPLOSS DOUBLE null) ''')
    
        #El tipo puede ser resistencia o soporte
    def insertar_margen(self, tipo, valor_min, valor_max):
        self.cursor.execute("INSERT INTO MARGENES (TIPO, VALOR_MIN, VALOR_MAX) \
            VALUES ('" + tipo + "', '" + str(valor_min) + "', '" + str(valor_max) + "')")
        self.con.commit()
        
    def insertar_moneda(self, moneda):
        self.cursor.execute("INSERT INTO MONEDA (MONEDA) \
            VALUES ('" + moneda + "')")
        self.con.commit()
    
    def insertar_estado(self, estado):
        self.cursor.execute("INSERT INTO ESTADO (ESTADO) \
            VALUES ('" + estado + "')")
        self.con.commit()
        
    def insertar_id(self, tipo, numero):
        self.cursor.execute("INSERT INTO ID ('" + tipo + "') \
            VALUES ('" + str(numero) + "')")
        self.con.commit()
    
        #El numero será el checkpoint y el valor será el precio
    def insertar_checkpoint(self, numero, valor):
        self.cursor.execute("INSERT INTO CHECKPOINTS (NUMERO, VALOR) \
            VALUES ('" + str(numero) + "', '" + str(valor) + "')")
        self.con.commit()
        
    def insertar_stoploss(self, valor):
        self.cursor.execute("INSERT INTO STOPLOSS (STOPLOSS) \
            VALUES ('" + str(valor) + "')")
        self.con.commit()
        
    def insertar_check_actual(self, numero):
        self.cursor.execute("INSERT INTO CHECK_ACTUAL (CHECK_ACTUAL) \
            VALUES ('" + str(numero) + "')")
        self.con.commit()

    def mostrar_margenes(self):
        self.cursor.execute("SELECT TIPO, VALOR_MAX, VALOR_MIN from MARGENES")
        for i in self.cursor:
            print str(i[0]).capitalize() + ':'
            print "MÁXIMA = " + str(i[1])
            print "MÍNIMO = " +  str(i[2])
            print '----------------------'
    
    #El tipo es soporte/resistencia y valor es minimo/maximo
    def mostrar_margen(self, tipo, valor):
        self.cursor.execute("SELECT TIPO, VALOR_MAX, VALOR_MIN from MARGENES where TIPO='" + tipo + "'")
        for i in self.cursor:
            if valor == 'maximo':
                return i[1]
            elif valor == 'minimo':
                return i[2]
            
    def mostrar_moneda(self):
        self.cursor.execute("SELECT MONEDA from MONEDA")
        for i in self.cursor:
            return i[0]
    
    #El tipo puede ser compra o venta          
    def mostrar_estado(self):
        self.cursor.execute("SELECT ESTADO from ESTADO")
        for i in self.cursor:
            return i[0]
            
    def mostrar_id(self, tipo):
        self.cursor.execute("SELECT '" + tipo + "' from ID")
        for i in self.cursor:
            return i[0]
    
    # Muestra el valor del checkpoint actual
    def mostrar_checkpoint(self, numero):
        self.cursor.execute("SELECT VALOR from CHECKPOINTS where NUMERO='" + str(numero) + "'")
        for i in self.cursor:
            return i[0]
            
    # Muestra cual es el checkpoint operativo
    def mostrar_check_actual(self):
        self.cursor.execute("SELECT CHECK_ACTUAL from CHECK_ACTUAL")
        for i in self.cursor:
            return i[0]            
        
    def mostrar_stoploss(self):
        self.cursor.execute("SELECT STOPLOSS from STOPLOSS")
        for i in self.cursor:
            return i[0]
        
    def actualizar_margenes(self, tipo, valor_min, valor_max):
        self.cursor.execute("UPDATE MARGENES set VALOR_MIN='" + str(valor_min) + "' where TIPO='" + tipo + "'")
        self.cursor.execute("UPDATE MARGENES set VALOR_MAX='" + str(valor_max) + "' where TIPO='" + tipo + "'")
        self.con.commit()

    def actualizar_moneda(self, moneda):
        self.cursor.execute("UPDATE MONEDA set MONEDA = '" + moneda + "'")
        self.con.commit()
    
    def actualizar_estado(self, estado):
        self.cursor.execute("UPDATE ESTADO set ESTADO = '" + estado + "'")
        self.con.commit()
        
    def actualizar_stoploss(self, valor):
        self.cursor.execute("UPDATE STOPLOSS set STOPLOSS = '" + str(valor) + "'")
        self.con.commit()
        
    def actualizar_id(self, tipo, numero):
        self.cursor.execute("UPDATE ID set '" + tipo + '" = "' + str(numero) + "'")
        self.con.commit()
        
    def actualizar_check_actual(self, numero):
        self.cursor.execute("UPDATE CHECK_ACTUAL set CHECK_ACTUAL = '" + str(numero) + "'")
        self.con.commit()
        
    def borrar_checkpoints(self):
        self.cursor.execute("DELETE FROM CHECKPOINTS")
        self.con.commit()
    
    def cerrar(self):
        self.con.close()

#____________________________________________________
        
# SERVIDOR API (Poloniex)

api = poloniex.poloniex(config.keypublic, config.keysecret)

# Pide el balance de una moneda, ej: ('STEEM')
# Tipos de balances: available, onOrders o btcValue
def balance(moneda, tipo):
    balance = api.returnCompleteBalances().get(moneda).get(tipo)
    return balance

# Pide el precio de una moneda
# Tipos de precios: bids o asks
# Devuelve un diccionario con las claves "precio" y "volumen"
def precio(moneda, tipo):
    moneda = str(Base_datos().mostrar_moneda())
    precio = api.returnOrderBook('BTC_' + moneda).get(tipo)[0][0]
    volumen = api.returnOrderBook('BTC_' + moneda).get(tipo)[0][1]
    datos = {"precio": precio, "volumen": volumen}
    return datos

#Consulta si una orden está abierta, devuelve un booleano
def orden_abierta(moneda):
    try:
        api.returnOpenOrders('BTC_' + moneda)[0]
        return True
    except IndexError:
        return False

# Funcion de compra en Poloniex
def compra(moneda, precio, cantidad):
    id_compra = api.buy('BTC_' + moneda, str(precio), str(cantidad))
    return id_compra

# Función de venta en Poloniex
def venta(moneda, precio, cantidad):
    id_venta = api.sell('BTC_' + moneda, str(precio), str(cantidad))
    return id_venta
    
def ultimo_trade(moneda):
    trade = api.returnTradeHistory('BTC_' + moneda)[0]
    tipo = trade.get('type')
    precio = trade.get('rate')
    cantidad = trade.get('amount')
    total = trade.get('total')
    fecha = trade.get('date')
    informacion = {'precio': precio, 'tipo': tipo, 'cantidad': cantidad, 'total': total, 'fecha': fecha}
    return informacion

def tipo_orden(moneda):
    orden = api.returnOpenOrders('BTC_' + moneda)[0]['type']
    if str(orden) == 'buy':
        return 'compra'
    else:
        return 'venta'