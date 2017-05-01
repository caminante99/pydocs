# -*- coding: utf-8 -*-

import config, sqlite3

ruta = config.ruta_estadisticas

# Base de datos donde se guardan las estadísticas
class Estadisticas:
    def __init__(self):
        self.con = sqlite3.connect(ruta)
        self.cursor = self.con.cursor()
        
    # El tipo puede ser compra o venta
    def crear_tabla_operaciones(self):
        self.cursor.execute('''CREATE TABLE OPERACIONES
            (TIPO CHAR(50) NOT NULL,
            MONEDA CHAR(50) NOT NULL,
            ID INT NOT NULL,
            PRECIO DOUBLE NOT NULL,
            CANTIDAD DOUBLE NOT NULL,
            TOTAL DOUBLE NOT NULL)''')
            
    
    def crear_tabla_ganancia_acumulada(self):
        self.cursor.execute('''CREATE TABLE GANANCIA_ACUMULADA
            (TIPO CHAR(50) NOT NULL,
            MONEDA CHAR(50) NOT NULL)''')
    
    def mostrar_operacion(self, tipo, dato):
        self.cursor.execute("SELECT '" + str(dato) + "' from OPERACIONES where TIPO='" + str(tipo) + "'")
        for i in self.cursor:
            if dato == 'moneda':
                return i[1]
            elif dato == 'id':
                return i[2]
            elif dato == 'precio':
                return i[3]
            elif dato == 'cantidad':
                return i[4]
            elif dato == 'total':
                return i[5]
                
                
# ------------------------------
# Funciones que procesan y guardan las estadísticas

# Procesamiento de operaciones, recoge el id de la transacción y el tipo (venta o compra)

        
    