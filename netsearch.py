#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:38:00 2022

@author: armsy326
"""
import sys
from youtubesearchpython import VideosSearch

"""
uses youtubesearchpython module to search for a particular media
and give back details plus the you tube link for that particular media file
the link should be pasted after download command.
"""
class SearchYouTube(object):
    
    def __init__(self,keyword):
        
        self.keyword = keyword
        
    def searchfile(self):
        
        try:
            cnt = 0
            res = VideosSearch(self.keyword, limit=3)
            for _ in range(3):
                
                type  = "type:     " + res.result()['result'][cnt]['type']
                title = "title     " + res.result()['result'][cnt]['title']
                duration = "duration: "+ res.result()['result'][cnt]['duration']
                channel = "channel      "+ res.result()['result'][cnt]['channel']['name']
                link = "yt_link   "+ res.result()['result'][cnt]['link']
                
                sys.stdout.write(f"{type} \n {title} \n {duration} \n {channel}\n {link}\n")
                print(" ")
                cnt = +1
            
        except  Exception:
            sys.stdout.write("[Err]Connection could not be established. \n")
        
#SearchYouTube('naanza aje diamond platinumz').searchfile()


