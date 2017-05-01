# -*- coding: utf-8 -*-

import config, smtplib

# Cada vez que se supera un stoploss, avisamos con la ganancia que hemos asegurado
def ganancia_relativa(venta_total_stop_loss, total_compra):
    ganancia = float(venta_total_stop_loss) - float(total_compra)
    titulo = config.nombre + ' - Checkpoint superado'
    destinatario = config.mail_to
    mensajero = config.mail_from
    contra = config.contra
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(mensajero, contra)
    header = 'To:' + destinatario + '\n' + 'From: ' + mensajero + '\n' + 'Subject: ' + str(titulo) + ' \n'
    msg = header + 'Has asegurado una ganancia de ' + str(ganancia) + ' BTC'
    smtpserver.sendmail(mensajero, destinatario, msg)
    smtpserver.close()

# Cada vez que se completa una venta, avisamos con la ganancia que nos hemos llevado
# Recoge un diccionario con la información del último trade
# Envía un correo con todos los datos de la última transacción
def operacion(informacion):
    info = informacion
    if info.get('tipo') == 'sell':
        tipo_operacion = 'venta'
    elif info.get('tipo') == 'buy':
        tipo_operacion = 'compra'
    precio = info.get('precio')
    cantidad = info.get('cantidad')
    total = info.get('total')
    fecha = info.get('fecha')
    titulo = config.nombre + ' - Aviso de ' + tipo_operacion
    destinatario = config.mail_to
    mensajero = config.mail_from
    contra = config.contra
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(mensajero, contra)
    header = 'To:' + destinatario + '\n' + 'From: ' + mensajero + '\n' + 'Subject: ' + str(titulo) + ' \n'
    msg = header + 'Precio: ' + str(precio) + '\n' + 'Cantidad: ' + str(cantidad) + '\n' + 'Total: ' + str(total) + '\n' + 'Fecha: ' + str(fecha)
    smtpserver.sendmail(mensajero, destinatario, msg)
    smtpserver.close()

 
    

    