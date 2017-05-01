
YOUTUBE_COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

MYCHANNEL = 'UCAgyf7c-giXPM0zgEExB74w'
API_KEY = 'AIzaSyC5FDxdh8ajj_2Qpnn7PV36Di5SUEAJ0dE'

import json
import sys
from urllib import *
import argparse
from urllib.parse import urlparse, urlencode, parse_qs
from urllib.request import  urlopen

import config

class YoutubeApi(object):
    def __init__(self):
        self.api_key = API_KEY

    def _openURL(self, url, parms):
            f = urlopen(url + '?' + urlencode(parms))
            print(url + '?' + urlencode(parms))
            data = f.read()
            f.close()
            matches = data.decode("utf-8")
            return matches

    def channel_videos(self, channel_id, max_res=50):
        ''' Toma una id de canal y devuelve todos los vídeos
        con su información en un diccionario. Se le puede pasar
        un número para indicar el límite máximo de resultados'''
        
        parms = {
                   'part': 'id,snippet',
                   'channelId': channel_id,
                   'maxResults': max_res,
                   'key': self.api_key
                }
    
        matches = self._openURL(YOUTUBE_SEARCH_URL, parms)
        search_response = json.loads(matches)

        videos = []
        for search_result in search_response.get('items', []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append(search_result['snippet'])

        return videos

    def search_channel(self, channel_id, max_res=50):
        ''' Toma una id de canal y devuelve información sobre el canal '''

        parms = {
                    'part': 'snippet',
                    'channelId': channel_id,
                    'maxResults': max_res,
                    'key': self.api_key
                }
        
        matches = self._openURL(YOUTUBE_SEARCH_URL, parms)
        search_response = json.loads(matches)
        return search_response

    def search_video(self, url, max_res=50):
        ''' Toma la url de un vídeo y devuelve su información '''
        from json import loads
        f = urlopen('https://www.youtube.com/oembed?url=' + url + '&format=json')
        response = loads(f.read().decode('ascii'))
        return response

def _time_conversion(time):
    ''' Convierte los tiempos del formato hora:minutos:segundos
    dados en cadenas de texto al total en segundos como entero '''
    splitter = time.split(':')
    seconds = int(splitter[2])
    minutes = int(splitter[1])
    hours = int(splitter[0])
    total = seconds + minutes * 60 + hours * 60**2
    return total
    

def cut(filename_in, t1, t2, filename_out, verbose=False):
    ''' Corta un trozo del vídeo y lo guarda en uno nuevo '''
    ''' t1 y t2 se meten indicando hora:minutos:segundos,
    como cadenas de texto '''
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    from os import path
    if verbose == True:
        print('Cutting from %s to %s' % (t1, t2))
    T1 = _time_conversion(t1)
    T2 = _time_conversion(t2)
    ffmpeg_extract_subclip(filename_in, T1, T2, filename_out)

def download_video(url, save_in=None, filename_out=None, verbose=False):
    ''' Descarga un vídeo de youtube, se necesita instalar pytube '''
    from pytube import YouTube
    y = YouTube(url)

    original_name = YoutubeApi().search_video(url)['title']
    
    if verbose == True:
        print('Downloading: ' + str(original_name))
        print('Please, wait...')
    
    if filename_out:
        y.set_filename(filename_out)
    else:
        filename_out = original_name
        y.set_filename(filename_out)
        
    video = y.filter('mp4')[-1]
    
    if save_in == None:
        video.download(config.PATH)
    else:
        video.download(save_in)

    if verbose == True:
        print('Video downloaded and saved as ' + filename_out)
    return filename_out + '.mp4'

def download_audio(url, filename_out=None, t1=None, t2=None, verbose=False):
    ''' Descarga un vídeo de youtube, extrae el audio y lo guarda en un archivo '''
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
    from os import remove

    # sudo apt-get install mplayer
    # sudo apt-get install lame

    if filename_out == None:
        filename_out = YoutubeApi().search_video(url)['title']
        
    response = download_video(url, filename_out='video_temp', verbose=verbose)

    if t1 != None and t2 == None or t1 == None and t2 != None:
        exc = 'You must provide both temps: start and end'
        raise AttributeError(exc)

    if t1 != None and t2 != None:
        cut('video_temp.mp4', t1, t2, 'video_temp_edit.mp4', verbose=verbose)
        if verbose == True:
            print('Converting into .wav\n Please, wait...') 
        ffmpeg_extract_audio('video_temp_edit.mp4', filename_out + '.wav')
        remove('video_temp_edit.mp4')
    elif t1 == None and t2 == None:
        if verbose == True:
            print('Converting into .wav\n Please, wait...') 
        ffmpeg_extract_audio('video_temp.mp4', filename_out + '.wav')
        remove('video_temp.mp4')
    
    if verbose == True:
        print('Video converted correctly')

    return filename_out + '.wav'
        
#URL = 'https://www.youtube.com/watch?v=rg4N6hdQ0Uk'
#download_youtube_audio(URL, verbose=True)

def downcutup(url, t1, t2, title, description, verbose=False,
              category=None, default_language=None,
              default_audio_language=None, playlist=None,
              privacy=None, thumbnail=None, tags=None):
    import shlex
    from os import path, remove
    from subprocess import Popen, PIPE

    original_name = YoutubeApi().search_video(url)['title']
    original_author = YoutubeApi().search_video(url)['author_name']
        
    download_video(url, filename_out='video_temp', verbose=verbose)

    if verbose == True:
        print('Cutting from %s to %s' % (t1, t2))
        
    cut(config.PATH + 'video_temp.mp4', t1, t2, config.PATH + 'video_temp_edit.mp4')

    final_description = description + '\n\nVideo extraído del canal ' +  original_author + ' (' + url + ')'
    command = 'youtube-upload --title=' + "'" + title + "'"
    command += ' --description=' + "'" + final_description + "'"
    if category:
        category = sub('category', "'category'", category)
        command += " --category='" + category + "'"
    if default_language:
        command += " --default-language='" + default_language + "'"
    if default_audio_language:
        command += " --default-audio-language='" + default_audio_language + "'"
    if playlist:
        command += " --playlist='" + playlist + "'"
    if privacy:
        command += " --privacy='" + privacy + "'"
    if thumbnail:
        command += " --thumbnail='" + thumbnail + "'"
    if tags:
        command += " --tags='" + tags + "'"
    command += ' ' + config.PATH + 'video_temp_edit.mp4'
    
    if verbose == True:
        print()
        print('Uploading \n Title: ' + str(title))
        print('Description: ' + str(final_description))
        print('Please, wait...')
        
    args = shlex.split(command)
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    url_video_uploaded = 'https://www.youtube.com/watch?v=' + str(process.communicate()[0].decode('ascii'))
    remove(config.PATH + 'video_temp.mp4')
    remove(config.PATH + 'video_temp_edit.mp4')
    if verbose == True:
        print('Video uploaded correctly')
        
    return url_video_uploaded

def youtube_upload(filename_in, title, description, verbose=False,
              category=None, default_language=None,
              default_audio_language=None, playlist=None,
              privacy=None, thumbnail=None, tags=None):
    final_description = description + '\n\nVideo extraído del canal ' +  origin$
    command = 'youtube-upload --title=' + "'" + title + "'"
    command += ' --description=' + "'" + final_description + "'"
    if category:
        category = sub('category', "'category'", category)
        command += " --category='" + category + "'"
    if default_language:
        command += " --default-language='" + default_language + "'"
    if default_audio_language:
        command += " --default-audio-language='" + default_audio_language + "'"
    if playlist:
        command += " --playlist='" + playlist + "'"
    if privacy:
        command += " --privacy='" + privacy + "'"
    if thumbnail:
        command += " --thumbnail='" + thumbnail + "'"
    if tags:
        command += " --tags='" + tags + "'"
    command += ' ' + config.PATH + filename_in
    
    if verbose == True:
        print()
        print('Uploading... \n Title: ' + str(title))
        print('Description: ' + str(final_description))
        print('Please, wait...')

    args = shlex.split(command)
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    url_video_uploaded = 'https://www.youtube.com/watch?v=' + str(process.commu$

    if verbose == True:
        print('Video uploaded correctly')

    return url_video_uploaded

# Ejemplo de descarga de vídeo, recorte y subida
'''
url = 'https://www.youtube.com/watch?v=XPPPYe1NfCM'
start = '0:00:15'
end = '0:00:30'
titulo = 'locura de prueba'
descripcion= 'Prueba con python'
privacy='private'

print(downcutup(url, start, end, titulo, descripcion))
'''

''' Para una biblioteca más compleja de descarga de vídeos:
https://github.com/rg3/youtube-dl/blob/master/README.md#readme
'''

# Como subir un vídeo

'''

Para subir un vídeo a youtube hay que instalar youtube-upload:

sudo pip3 install --upgrade google-api-python-client progressbar2

wget https://github.com/tokland/youtube-upload/archive/master.zip
unzip master.zip
cd youtube-upload-master
sudo python setup.py install
PYTHONPATH=. python bin/youtube-upload


--title='Nombre del vídeo'
--description="A.S. Mutter plays Beethoven" \
  --category=Music \
  --tags="mutter, beethoven" \
  --recording-date="2011-03-10T15:32:17.0Z" \
  --default-language="en" \
  --default-audio-language="en" \
  --client-secrets=my_client_secrets.json \
  --credentials-file=my_credentials.json \
  --playlist "My favorite music" \
  path_al_video.mp4
tx2Zb-145Yz

Other extra medata available :

--privacy (public | unlisted | private)  
--publish-at (YYYY-MM-DDThh:mm:ss.sZ)  
--location (latitude=VAL,longitude=VAL[,altitude=VAL])  
--thumbnail (string)  

'''

''' OPCIONAL:
export PATH=$PATH:/home/pi/youtube-upload-master/bin/youtube-upload
'''
        
