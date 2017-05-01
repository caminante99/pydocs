from PIL import ImageGrab, ImageOps

# Devuelve la pantalla actual como un objeto
def screen(save=False, **ruta):
    im = ImageGrab.grab()
    if save == True:
        im.save(ruta, 'PNG')
    return im

''' OPERACIONES CON LA IMAGEN OBJETO '''

''' Buscar un pixel dadas unas coordenadas: '''
#print screen().getpixel((x, y))
