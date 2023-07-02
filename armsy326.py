#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:32:54 2022

@author: armsy326
"""

import os
import sys
import re
import playsound
import time
from netsearch import SearchYouTube
from manual import more_info
from downplay import DownloadInquest

matching_media = []
previous_list = []
current_media = []
selected   = []
fac_accuracy = []

#main path to music directory for linux distros
media_path  = os.path.abspath(f"{os.path.expanduser('~')}/Music")
#a function that scans top tier directory and sub directories inside the main music dir
 #by default  this deals with the music dir   
def progress(func):  
    
    def run():               
        print("Refreshing media files....", sep="", end="")
        for i in range(5):
            
            for frame in r'/|\.':
                
                print('\b', frame, end="", sep="", flush=True)
                time.sleep(0.1)
                
        print('\b')
        func()
    return run
@progress       
def scan_media():
    #music present in the main Music directory
    media   = os.listdir(media_path)
        
    with open(".music.txt", mode="w") as file:
        for media_files  in media:
            file.write(f"\n {media_path}/{media_files}")
    #get music in other directories
    
    other_media  = next(os.walk(media_path))[1]
    
    sys.stdout.write("{: ^50s}".format(f"Scanned Folders({len(other_media) + 1})\n\n"))

    #List of files in the parent directory
    #print("Music(parent dir)", len(music), "files")
    
    for folders in other_media:
        
        media_present  = os.listdir(os.path.join(media_path, folders))
            
        with open(".music.txt", mode="a") as file:
            for media_file in media_present:
                
                file.write(f"\n {media_path}/{folders}/{media_file}")
        
        #folders in music dir with number of files
        print(folders," ", len(folders),"files\n")

        
#searching music from the text file

def searching(song):
    try:
        
        matching_media.clear()
        with open(".music.txt", mode='r+', encoding="utf-8") as media:
            
            files = media.read()
            
            pattern = re.compile(f'.+{song}.+', re.IGNORECASE)
            
            matches  =  re.findall(pattern, files)
            
            cnt = 0
            
            for match in matches:
                matching_media.append(match.lstrip(" "))
                pattern = f'{media_path}'
                matches = re.sub(pattern, "", match)
                new_pattern = r'.+/'
                perfect_match = re.sub(new_pattern, "", matches)
                no_ext  = r'.(?:mp3|mp4|.webm|m4a)'
                res_media = re.sub(no_ext, "", perfect_match)
                time.sleep(0.01)
                sys.stdout.write(f"{cnt} {res_media}\n")
            
                cnt += 1
                    
    except FileNotFoundError:
        sys.stdout.write("Type 'refresh' to collect and update your playlist.\n")
        
def under_acc(song):
    fac_accuracy.clear()
    with open(".music.txt", mode='r+', encoding="utf-8") as media:
        
        files = media.read()
        
        pattern = re.compile(f'.+{song}.+', re.IGNORECASE)
        matches  =  re.findall(pattern, files)
        
        for match in matches:
            fac_accuracy.append(match.lstrip(" "))  
        
def add_path(path):
    try:
        files = os.listdir(path)
        app = input("Do you  wish to add media files from this path[Y/n]? ")
        
        if app.upper() == "Y":
            print("Adding files from path...", sep="", end="")
            
            for i in range(5):
                
                for frame in r'/\|.':
                    print('\b', frame, end="", sep="", flush=True)
                    time.sleep(0.1)
            print('\b')
            pattern  = re.compile(r'.+(?:.mkv|.mp4|.mp3|.mwa|.webm)')
            with open(".music.txt", mode='a') as play_list:
                for file in files:
                    media = re.search(pattern, file)
                    
                    if media != None:
                        play_list.write(f"\n {path}/{media.group(0)}")
            
            folders = next(os.walk(path))[1]
            
            for folder in folders:
                if folder != "Music":
                    files = os.listdir(os.path.join(path, folder))
                    
                    with open(".music.txt", mode="a") as playlist:
                        for file in files:
                            media = re.search(pattern, file)
                            if media != None:
                                playlist.write(f"\n {path}/{media.group(0)}")
                sys.stdout.write(f"{folder}  {len(folder)} files \n")
        else:
            sys.stdout.write("[Skipped] playlist not updated.\n")
                
    except FileNotFoundError:
        sys.stdout.write("[Err]The path ins't well configured.Exiting...\n")

        
        
def all_songs():
    matching_media.clear()
    try:
        with open(".music.txt", mode='r+', encoding="utf-8") as music:
            
            files = music.read()        
            pattern = re.compile(r'.+', re.IGNORECASE)
            
            matches  =  re.findall(pattern, files)
            
            cnt = 0
            
            for match in matches:
                matching_media.append(match.lstrip(" "))
                pattern = f'{media_path}'
                matches = re.sub(pattern, "", match)
                new_pattern = r'.+/'
                perfect_match = re.sub(new_pattern, "", matches)
                no_ext  = r'.(?:mp3|mp4|.webm|m4a)'
                res_media = re.sub(no_ext, "", perfect_match)
                time.sleep(0.01)
                sys.stdout.write(f"{cnt} {res_media}\n")
            
                cnt += 1
    except Exception as e:
        if e.__class__.__name__ == 'FileNotFoundError':
            sys.stdout.write("[Err]No music file generated.Use 'refresh' command to generate one.\n")
    """else:
        print(e)
        sys.stdout.write("[Err]Could not find generated music file.\n")"""
            
def total_media():
    with open(".music.txt", mode='r+', encoding="utf-8") as music:
        
        files = music.read()   
        pattern = re.compile(r'.+', re.IGNORECASE)
        
        matches  =  re.findall(pattern, files)
        
        sys.stderr.write(f"Total Media: {len(matches)}\n")
        
def audio(file  = None):
    
    matching_media.clear()
    with open(".music.txt", mode='r+', encoding="utf-8") as music:
        
        files = music.read()
        
        if file != None:
            pattern = re.compile(f'.+{file}.+(?:.mp3|.m4a|.webm)', re.IGNORECASE)
            
            matches  =  re.findall(pattern, files)
            
            cnt = 0
            
            for match in matches:
                matching_media.append(match.lstrip(" "))
                pattern = f'{media_path}/'
                matches = re.sub(pattern, "", match)
                new_pattern = r'.+/'
                perfect_match = re.sub(new_pattern, "", matches)
                no_ext  = r'.(?:mp3|mp4|.webm|m4a)'
                res_media = re.sub(no_ext, "", perfect_match)
                time.sleep(0.01)
                sys.stdout.write(f"{cnt} {res_media}\n")
            
                cnt += 1
        else:
            
            pattern = re.compile(r'.+(?:.mp3|.mkv)', re.IGNORECASE)
            
            matches  =  re.findall(pattern, files)
            
            cnt = 0
            
            for match in matches:
                matching_media.append(match.lstrip(" "))
                pattern = f'{media_path}'
                matches = re.sub(pattern, "", match)
                new_pattern = r'.+/'
                perfect_match = re.sub(new_pattern, "", matches)
                no_ext  = r'.(?:mp3|mp4|.webm|m4a)'
                res_media = re.sub(no_ext, "", perfect_match)
                time.sleep(0.01)
                sys.stdout.write(f"{cnt} {res_media}\n")
                
                cnt += 1
            

def video(file = None):
    
    matching_media.clear()
    with open(".music.txt", mode='r+', encoding="utf-8") as music:
        
        files = music.read()
        
        if file != None:
            pattern = re.compile(f'.+{file}.+.mp4', re.IGNORECASE)
            
            matches  =  re.findall(pattern, files)
            
            cnt = 0
            
            for match in matches:
                matching_media.append(match.lstrip(" "))
                pattern = f'{media_path}'
                matches = re.sub(pattern, "", match)
                new_pattern = r'.+/'
                perfect_match = re.sub(new_pattern, "", matches)
                no_ext  = r'.(?:mp3|mp4|.webm|m4a)'
                res_media = re.sub(no_ext, "", perfect_match)
                time.sleep(0.01)
                sys.stdout.write(f"{cnt} {res_media}\n")
            
                cnt += 1
        else:
            
            pattern = re.compile(r'.+.mp4', re.IGNORECASE)
            
            matches  =  re.findall(pattern, files)
            
            cnt = 0
            
            for match in matches:
                matching_media.append(match.lstrip(" "))
                pattern = f'{media_path}'
                matches = re.sub(pattern, "", match)
                new_pattern = r'.+/'
                perfect_match = re.sub(new_pattern, "", matches)
                no_ext  = r'.(?:mp3|mp4|.webm|m4a)'
                res_media = re.sub(no_ext, "", perfect_match)
                time.sleep(0.01)
                sys.stdout.write(f"{cnt} {res_media}\n")
            
                cnt += 1

def play_on_current_list(val: int):
    try:
        if len(matching_media) != 0:
          
            path = os.path.abspath(matching_media[val])
            #print(path)
            try:
                playsound.playsound(path, block=False)
                previous_list.append(path)
            except:
                sys.stderr.write("[Err] File does not exist or has been removed/renamed.\n")
        else:
            sys.stdout.write("No Media in the playlist: run 'play' to add songs or 'help' for guidance.\n")
            
    except IndexError:
        sys.stdout.write("[Err]Selected file not present.\n")
               
def previous_play():
    if len(previous_list) != 0:
        
        cnt = 0
        for song in previous_list:
            new_pattern = r'.+/'
            perfect_match = re.sub(new_pattern, "", song)
            no_ext  = r'.(?:mp3|mp4|.webm|m4a)'
            res_media = re.sub(no_ext, "", perfect_match)
            time.sleep(0.01)
            sys.stdout.write(f"{cnt} {res_media}\n")
            
            cnt += 1
    else:
        sys.stdout.write("No Media has been played.\n")
        
def play():
    try:
        
        if len(matching_media) == 1:
            
            app = input("Found one match.Do you want to play it[Y/n]? ")
            
            if app.upper() == "Y":
                current_media.clear()
                current_media.append(0)
                playsound.playsound(matching_media[0], block=False)
                previous_list.append(matching_media[0])
            else:
                pass
            
    except Exception:
        sys.stdout.write("File not Found! Type 'refresh' to update your playlist.\n")
    
        
def play_next(val1: int):
    try:
        
        if len(current_media) != 0:
          
            path = os.path.abspath(matching_media[val1])
            previous_list.append(path)
            playsound.playsound(path, block=False)
            
            
    except Exception:
        sys.stdout.write("File not Found! Type 'refresh' to update your list.\n")
   
def play_repeat():
    if len(current_media) != 0:
        path = os.path.abspath(matching_media[current_media[0]])
        previous_list.append(path)
        playsound.playsound(path, block=False)
        
    else:
        sys.stdout.write("No Media has 'probably' been played.\n")

       
    
def play_prev(val1: int):
    
    if len(current_media) != 0:
      
        path = os.path.abspath(matching_media[val1])
        previous_list.append(path)
        playsound.playsound(path, block=False)

def play_selected():
    
    if len(matching_media) != 0:
        
        for val in selected[0]:
            try:
                if val.isdigit():
                    path = os.path.abspath(matching_media[int(val)])
                    previous_list.append(path)
                    playsound.playsound(path, block=True)
            except IndexError:
                sys.stdout.write("ERROR: Out of queue\n")
                
    else:
        sys.stdout.write("No media has 'probably' been searched\n")
            
def play_all():
    
    if len(matching_media) != 0:
        sys.stdout.write(f"Qued songs: {len(matching_media)}\n")
        for song in matching_media:
            path = os.path.abspath(song)
            previous_list.append(path)
            try:
                playsound.playsound(path, block=True)
                
            except Exception:
                sys.stdout.write("WARNING: Skiped files not found.Run 'refresh' to update your playlist.\n")
            
    else:
        sys.stdout.write("No media files present!, if you meant to play your entire playslist, first run 'list all songs'.\n")
        
def playing():
    
    if len(previous_list) != 0:
        pattern = r'.+/'
        stream = re.sub(pattern , "", previous_list[-1])
        sys.stderr.write(f"playing: {stream}\n")
    else:
        sys.stdout.write("No Media has been played.\n")
        
def rename(pos: int, new_title: str)-> None:
    
    try:
        path = os.path.split(matching_media[int(pos)])[0]
        
        file_name  = os.path.split(matching_media[0])[1]
        
        base,ext  = os.path.splitext(file_name)
        
        os.rename(matching_media[int(pos)], path+'/'+new_title+ext)
        matching_media.pop(int(pos))
        sys.stderr.write(f'File has been renamed to {new_title+ext}.Refresh to update playlist.\n')
        matching_media.insert(int(pos), path+'/'+new_title+ext)
        
    except FileNotFoundError:
        sys.stderr.write("[Err] The media file has been removed or renamed.\n")
        
    except IndexError:
        sys.stderr.write("[Err] The selected file is not present.\n")
    
    except ValueError:
        sys.stderr.write("[Err] pass in a numeric value.Type 'help rename' for more guidance.\n")
        
def delete(path):
    try:
        if path != '':
            os.remove(matching_media[int(path)])
            app = input("Deleted Media file.\nWould you like to refresh your playlist[Y/n]?")
            if app.upper() == "Y":
                scan_media()
            else:
                pass
        else:
            sys.stdout.write("[Err]Pass a media file to be deleted.\n")
            
    except FileNotFoundError:
        sys.stdout.write("[Err]File to be deleted does not exist.\n")
    
def whole_sequence():
    
    command = input(f"{os.getlogin()}> ").strip()
    
    accepted_commands  = [
        command.isdigit(),
        command == "exit",
        command == "quit",
        command.replace(" ","") == "listall",
        command.replace(" ","") == "totalmedia",
        command[:4] == "play",
        command == "clear",
        command == "streamed",command == "streaming",
        command == "refresh",
        command[:4] == "help",
        command.replace(" ","")[:7] == "addpath",
        command == "video songs",
        command == "audio songs",
        command == "prev",
        command == "repeat",
        command == "next",
        command == "stop",
        command[:6] == "delete",
        command[:6] == "rename",
        command[:8] == "download",
        command[:6] == "search"
        ]
    
    try:
        
        assert any(accepted_commands)
        
    except AssertionError:
        sys.stdout.write("[Err]Unknown command.Type 'help' to view accepted commands.\n")
    
    #re-modify the command stderr.
    #accept a sing tab in between
    command  = " ".join(command.split())
    #print(command)
    if command.isdigit():
        current_media.clear()
        current_media.append(int(command))
        play_on_current_list(int(command))
    if command == ("exit" or "quit"):
        sys.stderr.write("Nice day!\n")
        sys.exit()
    if command.replace(" ","") == "listall":
        all_songs()
    if command.replace(" ","") == "totalmedia":
        total_media()
    #playing songs by searching through search fxn
    if command[:4] == "play":
        if command[-5:] == "audio":
            file = command[5:].rstrip("audio")
            audio(file.strip())
            play()
        elif command[-5:] == "video":
            file = command[5:].rstrip("video")
            video(file.strip())
            play()
        elif command[-3:] == "all":
            play_all()
        elif command.replace(" ","")[:5] == "play,":
            selected.clear()
            selected.append(command.split(","))
            play_selected()
        else:
            file = command[5:]
            pattern = re.compile(r'\S')

            match = re.findall(pattern, file)
            if match == []:
                sys.stdout.write("[Err221]: Enter a keyword to initiate a search.\n")
            else:
                if matching_media != 0:
                    acc_search = []
                    pattern = re.compile(f'.+{file}.+', re.IGNORECASE)
                    
                    for song in matching_media:
                        
                        res  = re.findall(pattern, song)
                        
                        if res != []:
                            acc_search.append(res[0])
                            
                    if len(acc_search) == 1:
                        under_acc(file)
                        if len(fac_accuracy) == 1:
                            path = os.path.abspath(acc_search[0])
                            previous_list.append(path)
                            playsound.playsound(path, block=False)
                        else:
                            print("Executed1")
                            searching(file)
                            play()
                    elif len(acc_search) == 0:
                        searching(file)
                        play()
                    elif len(acc_search) >= 2:
                        searching(file)
                        play()
     
    if command == "next":
        try:
            val = current_media[0] + 1
            current_media.clear()
            current_media.append(val)
            play_next(val)
            
        except IndexError:
            sys.stdout.write("No media has been played or no next song\n")
    
    if command == "repeat":
        play_repeat()
        
    if command == "prev":
        
        try:
            val = current_media[0] - 1
            current_media.clear()
            current_media.append(val)
            play_prev(val)
            
        except IndexError:
            sys.stdout.write("No media has been played or no prev song\n")
    
    if command == "audio songs":
        audio()
    if command == "video songs":
        video()
    #gives option to add path
    if command.replace(" ","")[:7] == "addpath":
        path = re.findall(r'/.+', command, re.IGNORECASE)
        add_path(path[0])
    if command[:6] == "delete":
        delete(command.replace(" ","")[6:])
    if command[:6] == "search":
        SearchYouTube(command[7:]).searchfile()
    if command[:8] == "download":
        #print(command[9:])
        pattern = re.compile(r'https://(?:www.youtube.com/watch?|youtu.be|m).+')
        res  = re.match(pattern, command[9:])
        
        if res == None:
            sys.stderr.write("[Err]please enter a valid youtube link.\n")
        else:
            if command[-5:].lower() == "audio":
                DownloadInquest(command[9:].strip("audio"), audio="audio").manage_defaults()
            elif command[-5:].lower() == "video":
                DownloadInquest(command[9:].strip("video"), video="video").manage_defaults()
            elif command[-4:].lower() == "both":
                DownloadInquest(command[9:].strip("both"),video="video", audio="audio").manage_defaults()
            else:
                DownloadInquest(command[9:]).manage_defaults()
                
    if command[:6] == "rename":
        rename(command[7:9], command[9:].strip())
    if command[:4] == "help":
        more_info(command)
    if command == "refresh":
        scan_media()
    if command == "streamed":
        previous_play()
    if command == "streaming":
        playing()
    if command == "clear":
        os.system("clear")
        
        
        
