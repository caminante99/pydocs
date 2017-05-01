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


''' Consultar información de las imágenes '''
# FORMATO
print imagen.format # JPEG
print

# TAMAÑO
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

''' Recortar imágenes '''
# region es una tupla (x, y, ancho, alto)
# imagen_original e imagen_nueva son las rutas de las imágenes
def recortar(imagen_original, region, imagen_nueva):
    imagen = Image.open(imagen_original)
    recorte = imagen.crop(region)
    # recorte.show()
    recorte.size # Mostrar tamaño de imagen final
    recorte.save(imagen_nueva)
    
''' Cambiar tamaño de las imágenes '''
imagen.resize((400, 300))

''' Rotar imagen '''
imagen.rotate(45) # Sentido contrario de las agujas del reloj

'''Pegar una región dentro de otra imagen:'''
'''
imagen.paste(region, caja) region es la imagen a pegar (como objeto)
y caja es una tupla (x, y, ancho, alto) que indica donde será colocada
'''

''' Crear miniaturas '''
imagen.thumbnail((160, 120))



