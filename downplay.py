#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:16:07 2022

@author: armsy326
"""
import os
import sys
import concurrent.futures
from tqdm import tqdm
import pytube
from pytube.cli import on_progress

class DownloadInquest(object):
    
    def __init__(self, 
                 link,audio=None,
                 video=None,
                 path = f"/home/{os.getlogin()}/Downloads"
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
        
        link = pytube.YouTube(self.link, on_progress_callback=on_progress)
        #use progressivce to try and get itag 22
        res  = link.streams.filter(progressive=True)
        
        video = link.streams.get_by_itag(22)
        try:
            os.path.exists(self.path)
            video.download(self.path)
            sys.stdout.write(f"File saved at: {self.path}\n")
            
        except Exception:
            sys.stderr.write("[Err]Link error.Pass a legit link after the download statement.Type 'help download' for more information. \n")

    """
    Downloads audio files
    """
    @loader
    def youtubeaudio(self):
        link = pytube.YouTube(self.link, on_progress_callback=on_progress)
        #use progressivce to try and get itag 22
        res  = link.streams.filter(only_audio=True)
        
        audio = link.streams.get_by_itag(251)
        try:
            os.path.exists(self.path)
            audio.download(self.path)
            sys.stdout.write(f"File at: {self.path}\n\n")
        except Exception:
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
            
