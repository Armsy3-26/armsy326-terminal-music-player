#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:16:07 2022

@author: armsy326
"""
from __future__ import unicode_literals
import os
import sys
import concurrent.futures
from tqdm import tqdm
import youtube_dl

class DownloadInquest(object):
    
    def __init__(self, 
                 link,audio=None,
                 video=None,
                 path = f"/home/{os.getlogin()}/Music"
                 )->str:
        
        self.link = link
        self.path = path
        self.audio = audio
        self.video = video
        
    #a wrapper for downloading
    #show download progress
    
    def loader(func):
        
        def wrapper(self):
            try:
                print("Downloading file in a few...\n")
                func(self)
            except Exception as e:
                print(e)
                sys.stderr.write('[Err]No internet connection\n')
        return wrapper
                
    """
    Downloads videos
    """
    @loader
    def youtubevideo(self):
        
        try:
            os.path.exists(self.path)
            ydl_opts = {
                'outtmpl': os.path.join(self.path, '%(title)s.%(ext)s')
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.link])
            sys.stdout.write(f"File saved at: {self.path}\n")
            
        except Exception:
            
            sys.stderr.write("[Err]Link error.Pass a legit link after the download statement.Type 'help download' for more information. \n")

    """
    Downloads audio files
    """
    @loader
    def youtubeaudio(self):
        
        try:
            os.path.exists(self.path)
            ydl_opts  = {
                'format': 'bestaudio/best',
                'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(self.path, '%(title)s.%(ext)s')
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.link])
            sys.stdout.write(f"File at: {self.path}\n\n")
        except Exception as e:
            print(e)
            sys.stderr.write("[Err]Link error.Pass a legit link after the download statement.Type 'help download' for more information. \n")
        
    @loader
    def both_media(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            
            executor.submit(self.youtubevideo)
            executor.submit(self.youtubeaudio)
        
    def manage_defaults(self):
        #by default get video media
        if (self.video != None and self.audio == None):
            self.youtubevideo()
            
        elif (self.audio != None and self.video == None):
            self.youtubeaudio()
            
        elif (self.video !=None and self.audio != None):
            self.both_media()
            
        else:
            self.youtubevideo()
            
