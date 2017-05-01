# -*- coding: utf-8 -*-
from modules import llamadas

base = llamadas.Base_datos()

base.crear_tabla_moneda()
base.crear_tabla_estado()
base.crear_tabla_margenes()
base.crear_tabla_checkpoints()
base.crear_tabla_check_actual()
base.crear_tabla_stoploss()
base.crear_tabla_id()

print 'Las tablas se han creado correctamente'
