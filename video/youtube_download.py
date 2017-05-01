
from pytube import YouTube

''' Descarga un vídeo de youtube, se necesita instalar pytube '''

''' Para una biblioteca más compleja de descarga de vídeos:
https://github.com/rg3/youtube-dl/blob/master/README.md#readme
'''

def youtube_download(url, save_in='', max_quality=True, extension='mp4', name='default'):
    from pytube import YouTube
    y = YouTube(url)
    if name != 'default':
        y.set_filename(name)
    if max_quality == True:
        video = y.filter(extension)[-1]
    try:
        video.download(save_in)
    except OSError:
        num = 0
        error = True
        while error == True:
            y.set_filename(name + '_' + str(num))
            try:
                video.download(save_in)
                error == False
            except OSError:
                num += 1
                error == True
    return 'Descarga finalizada'
   

# url = ''
# youtube_download(url))


