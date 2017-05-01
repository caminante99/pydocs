# -*- coding: cp1252 -*-

# https://owenashurst.com/?p=242

sudo apt-get remove --purge libmp3lame-dev libtool libssl-dev libaacplus-* libx264 libvpx librtmp ffmpeg

sudo apt-get update; sudo apt-get upgrade; sudo apt-get install libmp3lame-dev; sudo apt-get install -y libopus-dev; sudo apt-get install autoconf; sudo apt-get install libtool; sudo apt-get install checkinstall; sudo apt-get install libssl-dev

''' Downloading & Compiling LibaacPlus '''

sudo apt-get install libtool-bin
wget http://tipok.org.ua/downloads/media/aacplus/libaacplus/libaacplus-2.0.2.tar.gz
tar -xzf libaacplus-2.0.2.tar.gz
cd libaacplus-2.0.2
./autogen.sh --with-parameter-expansion-string-replace-capable-shell=/bin/bash --host=arm-unknown-linux-gnueabi --enable-static
make
sudo make install

''' Downloading & Compiling Libx264 '''

cd /home/pi/src
git clone git://git.videolan.org/x264
cd x264
./configure --host=arm-unknown-linux-gnueabi --enable-static --disable-opencl
make
sudo make install

'''  Downloading & Compiling LibVPX '''

cd /home/pi/src
git clone https://chromium.googlesource.com/webm/libvpx
cd libvpx
./configure
make
sudo checkinstall --pkgname=libvpx --pkgversion="1:$(date +%Y%m%d%H%M)-git" --backup=no     --deldoc=yes --fstrans=no --default

''' Downloading & Compiling LibRTMP '''

cd /home/pi/src
git clone git://git.ffmpeg.org/rtmpdump
cd rtmpdump
make SYS=posix
sudo checkinstall --pkgname=rtmpdump --pkgversion="2:$(date +%Y%m%d%H%M)-git" --backup=no --deldoc=yes --fstrans=no --default
sudo ldconfig

''' Downloading & Compiling Libfaac '''
cd /home/pi/src
curl -#LO http://downloads.sourceforge.net/project/faac/faac-src/faac-1.28/faac-1.28.tar.gz
tar xzvf faac-1.28.tar.gz
cd faac-1.28
nano common/mp4v2/mpeg4ip.h

'''
When you’re in the nana editor, you will need to go to line 126.
Once you’re at that line, make the below code the same as in the file…

#ifdef __cplusplus
extern "C" {
#endif
#ifndef _STRING_H
char *strcasestr(const char *haystack, const char *needle);
#endif
#ifdef __cplusplus
}
#endif
'''

./configure --host=arm-unknown-linux-gnueabi
make
sudo make install
sudo ldconfig
sudo reboot

''' Downloading & Compiling LibFDK-aac '''

cd /home/pi/src
git clone --depth 1 https://github.com/FFmpeg/FFmpeg.git
cd ffmpeg
./configure --enable-cross-compile --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree --enable-libfdk-aac --enable-libvpx --enable-libopus --enable-librtmp --enable-libmp3lame
make -j3
sudo make install

''' Downloading & Compiling FFMPEG (Latest Version) '''
cd /home/pi/src
git clone --depth 1 https://github.com/FFmpeg/FFmpeg.git
cd ffmpeg
./configure --enable-cross-compile --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree --enable-libfdk-aac --enable-libvpx --enable-libopus --enable-librtmp --enable-libmp3lame
make -j3
sudo make install

sudo reboot


''' INSTALL MOVIEPY '''
sudo pip3 install numpy --upgrade

sudo pip3 install moviepy
