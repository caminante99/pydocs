# -*- coding: utf-8 -*-

__author__ = 'Álvaro Mondéjar'

from bs4 import BeautifulSoup
import requests

class Parser(object):
    def __init__(self, base_url= 'http://coinmarketcap.com/'):
        self.base_url = base_url

    def _url(self, currency_id):
        ''' Internal function for build currencies urls '''
        return self.base_url + 'currencies/' + currency_id + '/'

    def _html(self, currency_id):
        ''' Internal function for parse currencies htmls '''
        req = requests.get(self._url(currency_id))
        status_code = req.status_code
        if status_code == 200:
            return BeautifulSoup(req.text, "html.parser")
        else:
            print("Status Code %d" % status_code)
            return 'Error'
            

    def pos(self, currency_id):
        ''' Currency position in the global ranking '''
        pos = self._html(currency_id).find('span', {'class': 'label label-success'}).getText()
        return int("".join([c for c in pos if c.isdigit()]))

    def markets(self, currency_id):
        ''' Creamos la lista que contendrá los mercados '''
        markets = []
        
        ''' Cargamos el html '''
        html = self._html(currency_id)
        
        ''' Buscamos los mercados '''
        marks = html.find('tbody').find_all('tr')
        
        for m in marks:
            volume_24h = int(m.find('span', {'class': 'volume'}).getText().replace('$', '').replace(',', ''))
            price = float(m.find('span', {'class': 'price'}).getText().replace('$', ''))
            childs = m.contents
            for n, c in enumerate(childs):
                nav = unicode(c.string)
                if n == 3:
                    source = str(nav)
                elif n == 4:
                    pair = str(c.getText())
                    if pair[-1] == '*':
                        pair = pair.replace(' *', '')
                elif n == 10:
                    percent_volume = float(nav.replace('%', ''))
            market = {'source': source, 'pair': pair, '24h_volume_usd': volume_24h, 'price_usd': price, 'percent_volume': percent_volume}
            markets.append(market)
        return markets

    def _get_ranks(self, query, temp):
        ''' Internal function for get gainers and losers '''
        url = self.base_url + 'gainers-losers/'
        req = requests.get(url)
        status_code = req.status_code
        if status_code == 200:
            html = BeautifulSoup(req.text, "html.parser")
        else:
            exc("Error: Status Code %d" % status_code)
            

        call = str(query) + '-' + str(temp)

        final_list = []
        html_rank = html.find('div', {'id': call}).find_all('tr')
        for curr in html_rank[1:]:
            for n, g in enumerate(curr.contents):
                if n == 3:
                    name = str(g.img.getText().replace('\n', ''))
                elif n == 5:
                    symbol = str(unicode(g.string))
                elif n == 7:
                    volume_24h = int(str(g.a.getText()).replace('$', '').replace(',', ''))
                elif n == 9:
                    price = float(str(g.a.getText()).replace('$', ''))
                elif n == 11:
                    percent = float(str(unicode(g.string)).replace('%', ''))
            currency = {'name': name, 'symbol': symbol, '24h_volume_usd': volume_24h, 'price_usd': price, 'percent_change': percent}
            final_list.append(currency)

        return final_list
    
    def ranks(self, *args, **kwargs):
        ''' Function that returns information from gainers and losers rankings:
        http://www.coinmarketcap.com/gainers-losers/
        
        {'1h': [
                 {
                  'name': 'ethereum',
                  'symbol': 'ETH',
                  '24h_volume_usd': 29785452,
                  'price_usd': 50.45,
                  'percent_change': 20.65%
                 },
                 {
                  'name': 'dash',
                  'symbol': 'DASH',
                  '24h_volume_usd': 2343256,
                  'price_usd': 7.32,
                  'percent_change': 20.65%
                 },
                 
                ...
                ]
         '24_h: [
                 {
                  ...
                 },
                 {
                  ...
                 },
                 
                ...
                ]
            
                
        '''
        
        if len(args) == 0:
            temps = ['1h', '24h', '7d']
        else:
            temps = []
            for a in args:
                temps.append(a)
                
        gainers = True
        losers = True

        if 'gainers' in kwargs:
            gainers = kwargs['gainers']
        if 'losers' in kwargs:
            losers = kwargs['losers']

        queries = ['gainers', 'losers']
        if gainers == False:
            queries.remove('gainers')
        if losers == False:
            queries.remove('losers')

        if len(queries) == 0:
            exc = 'gainers or losers must be True'
            raise AttributeError(exc)

        response = {}
        if len(queries) > 1:
            for q in queries:
                response[q] = {}
            for q in queries:
                rankings = {}
                for t in temps:
                    ranking = self._get_ranks(q, t)
                    rankings[t] = ranking
                response[q] = rankings
        else:
            for q in queries:
                rankings = {}
                for t in temps:
                    ranking = self._get_ranks(q, t)
                    rankings[t] = ranking
                response = rankings
        
        return response
        
        
            
#from time import time
#start_time = time()
#print Parser().markets('ark')
#elapsed_time = time() - start_time
#print
#print("Tiempo transcurrido: %0.10f seconds." % elapsed_time)
