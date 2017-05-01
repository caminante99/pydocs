#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

def _reimport(update=False):
    """ Internal function for serves symbols correspondences """
    from os import path
    p = path.dirname(path.abspath(__file__))
    if update == True:
        from sys import path as pth
        pth.insert(1, p)
        import up
        up.update_currencies()
        pth.remove(p)
        if '' in pth:
            pth.remove('')
    with open(p + '/temp/symbols.txt', 'r') as f:
        availables = f.read()
        from ast import literal_eval as l
        return l(availables)

def _convert(currency):
    try:
        availables = _reimport()
    except IOError:
        availables = _reimport(update=True)
    if currency in availables:
        return availables.get(currency)
    else: # If the coin isn't in the dict
        availables = _reimport(update=True)
        if currency not in availables:
            exc = "The currency %s isn't in coinmarketcap" % currency
            raise NameError(exc)

from bs4 import BeautifulSoup
html = urllib2.urlopen("http://coinmarketcap.com/").read()
soup = BeautifulSoup( html, 'html.parser' )

class Market(object):
    def __init__(self, base_url='https://')#api.coinmarketcap.com/v1/'):
        self.base_url = base_url
        self.opener = urllib2.build_opener()
        self.opener.addheaders.append(('Content-Type', 'application/json'))
        self.opener.addheaders.append(('User-agent', 'coinmarketcap - python wrapper \
        around coinmarketcap.com (github.com/mrsmn/coinmarketcap-api)'))

    def _api(self, 

    def _urljoin(self, *args):
        """ Internal urljoin function because urlparse.urljoin sucks """
        urljoin = "/".join(map(lambda x: str(x).rstrip('/'), args))
        print urljoin
        return urljoin
    
    def _get(self, api_call, query):
        url = self._urljoin(self.base_url, api_call)
        if query == None:
            response = self.opener.open(url).read()
        else:
            response_url = self._urljoin(url, query)
            response = self.opener.open(response_url).read()
        return response

    def _up(self, param=None):
        """ Internal function for update symbols currencies """
        data = self._get('ticker/', query=param)
        import json, sys
        if int(sys.version[0]) < 3:
            return json.loads(data)
        else:
            return json.loads(data.decode('utf-8'))


    def ticker(self, currency=None, VERBOSE=False, V=False):
        """ ticker() returns a dict containing all the currencies
            ticker(currency) returns a dict containing only the currency you
            passed as an argument.
            
            VERBOSE=False (as default) -> ticker() return in json
            VERBOSE=True or V=True -> ticker() return a string
        """
        if currency != None:
            if currency.isupper() == True:
                currency = _convert(currency)
                
        data = self._get('ticker/', query=currency)
        if VERBOSE == True or V == True:
            return data
        else:
            import json, sys
            if int(sys.version[0]) < 3:
                return json.loads(data)
            else:
                return json.loads(data.decode('utf-8'))
        
        
    def stats(self, VERBOSE=False, V=False):
        """ stats() returns a dict containing cryptocurrency statistics.

            VERBOSE=False (as default) -> stats() return a dict
            VERBOSE=True or V=True -> stats() return a string
        """
        data = self._get('global/', query=None)
        if VERBOSE == True or V == True:
            return data
        else:
            import json, sys
            if int(sys.version[0]) < 3:
                return json.loads(data)
            else:
                return json.loads(data.decode('utf-8'))

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

    def markets(self, currency, VERBOSE=False, V=False):
        ''' Function that returns information from markets. It needs a currency as argument.
        pass VERBOSE=True or V=True for return a more readable string reponse

        Examples:
        markets('STEEM'), markets(ethereum, V=True)
        '''
        if currency.isupper():
            currency = _convert(currency)
        
        markets = []
        html = self._html(currency)
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
            
        if VERBOSE == True or V == True:
            import json
            return json.dumps(markets, indent=1)
        else:
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
    
    def ranks(self, VERBOSE=False, V=False, *args, **kwargs):
        ''' Function that returns information from gainers and losers rankings:
        You can pass '7d', '24h', '1h', gainers= False and losers=False for filter response

        pass VERBOSE=True or V=True for return a more readable string reponse

        http://www.coinmarketcap.com/gainers-losers/
        
        {
         "losers": {
          "1h": [
           {
            "24h_volume_usd": 10566, 
            "symbol": "SPHR", 
            "price_usd": 0.139695, 
            "percent_change": -13.21, 
            "name": "Sphere"
           }, 
           {
            "24h_volume_usd": 19346, 
            "symbol": "DTB", 
            "price_usd": 0.127478, 
            "percent_change": -12.91, 
            "name": "Databits"
           },
           ...
           ],
           
          "7d":
           [
            {
            "24h_volume_usd": 38521, 
            "symbol": "KASHH", 
            "price_usd": 0.00511, 
            "percent_change": -55.46, 
            "name": "KashhCoin"
            }, 
           ]
           ...
         },
         
         "gainers": {
          "1h": [
           {
            "24h_volume_usd": 12810, 
            "symbol": "SLING", 
            "price_usd": 0.022415, 
            "percent_change": 41.63, 
            "name": "Sling"
           },
           ...
            
                
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

        if VERBOSE == True or V == True:
            import json
            return json.dumps(response, indent=1)
        else:
            return response

