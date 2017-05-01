# -*- coding: cp1252 -*-
from PIL import Image

def abrir_imagen(ruta):
    try:
        imagen = Image.open(ruta)
        #imagen.show()
        return imagen
    except:
        print "No ha sido posible cargar la imagen"

imagen = Image.open("amapolas.jpg")


''' Consultar informaci�n de las im�genes '''
# FORMATO
print imagen.format # JPEG
print

# TAMA�O
print imagen.size # (600, 450)
print

# TIPO
print imagen.mode # RGB
print

# HISTOGRAMA
#print imagen.histogram
#print

# OTROS
#print imagen.info
#print imagen.palette

''' Recortar im�genes '''
# region es una tupla (x, y, ancho, alto)
# imagen_original e imagen_nueva son las rutas de las im�genes
def recortar(imagen_original, region, imagen_nueva):
    imagen = Image.open(imagen_original)
    recorte = imagen.crop(region)
    # recorte.show()
    recorte.size # Mostrar tama�o de imagen final
    recorte.save(imagen_nueva)
    
''' Cambiar tama�o de las im�genes '''
imagen.resize((400, 300))

''' Rotar imagen '''
imagen.rotate(45) # Sentido contrario de las agujas del reloj

'''Pegar una regi�n dentro de otra imagen:'''
'''
imagen.paste(region, caja) region es la imagen a pegar (como objeto)
y caja es una tupla (x, y, ancho, alto) que indica donde ser� colocada
'''

''' Crear miniaturas '''
imagen.thumbnail((160, 120))



