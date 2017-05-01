# -*- coding: cp1252 -*-

''' Cargar un html en BeautifulSoup con requests'''
from bs4 import BeautifulSoup
import requests

URL = 'http://coinmarketcap.com/currencies/steem/'
# Realizamos la petición a la web
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code
if status_code == 200:
    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")
else:
    print "Status Code %d" % status_code

#------------------------------------------------------

''' Buscar dentro de etiquetas '''
search_headers = html.find_all('th', {'class': 'sortable'})
# Esto busca todo lo que este dentro de etiquetas th y devuelve una lista   
# 'class': 'sortable' significa todo lo que contenga sortable dentro de 'class'

''' Buscar dentro de una etiqueta (la primera que encuentre) '''
html.find('tbody').string # string devuelve la info en una cadena

''' Buscar por tags '''
html.a.getText() # getText() devuelve solo el texto, sin las etiquetas
# Si no funciona también se puede usar la función strip()

#------------------------------------------------------

''' Obtener el título de una web '''
objeto = html.title.string # Obtiene un objeto NavigableString

''' Convertir NavigableString en texto '''
texto = unicode(objeto)


#------------------------------------------------------

''' Cargar varias páginas a la vez '''
quote_page = ['http://www.bloomberg.com/quote/SPX:IND', 'http://www.bloomberg.com/quote/CCMP:IND']

import urllib2
data = []  
for pg in quote_page:  
    # query the website and return the html to the variable 'page'
    page = urllib2.urlopen(pg)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('h1', attrs={'class': 'name'})
    name = name_box.text.strip() # strip() is used to remove starting and trailing
    print name_box
    print name
    # get the index price
    price_box = soup.find('div', attrs={'class':'price'})
    price = price_box.text

    # save the data in tuple
    data.append((name, price))
