#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 20:43:10 2022

@author: armsy326
"""
import sys

class Manual:
    #takes in the help message
    
    def __init__(self, *args, **kwargs):
        pass
    
    def cli(func):
        
        def msg(self=None):
            print("{: ^50s}".format("**CLI Media Player**"))
            
            func(self=None)
            
        return msg
        
    """
    The following is an help message.
    Gives accepted commands with brief explanations.
    If you want more about the commands type 'help followed_by_command'.
    
    """
    @property
    @cli
    def help_message(self):
        
        help_mess = """
        audio songs     gives a list of audio files
        add path        adds path to other medial files not in the default path.
        clear           this command clears the screen.
        download        accepts a youtube link/keyword to download a media file.
        delete          it completely removes a file not only from your playlist but also from the system.
        help            shows this message.
        play            with right keyword it searches songs/artists or plays an accurate finding after search.
        play all        plays all songs in the current playlist(searched).
        prev            plays previous/backward playing of songs.same as play prev.
        next            plays the next song. same as play next
        repeat          re-plays the media file that has been played.
        list all        lists all songs in the top tier Music dir and the sub folders only
        search          with a 'keyword' it searches for media from youtube.
        streamed        shows a list of media files that have been played.
        steaming        shows the media that is playing.
        total media       gives total numeric value of media.
        refresh         refreshes the media playlist.
        rename          renames media files.
        exit            exit closes the player.same as quit.
        video songs     outputs video files.
        
        To know more about how these commands work,type "help 'command'".
        """
        return sys.stdout.write(f"{help_mess}\n")
    
    @property
    @cli
    def audio(self):
        
        sys.stdout.write("""
                 *audio songs*
                 
        Executed by user> audios songs
        Displays all audio files.
        Files with .mp3,.webm,.m4a extensions only.
        
        \n""")
        
    @property
    @cli
    def video(self):
        
       sys.stdout.write("""
                 *video songs*
                 
        Executed by user> video songs
        Displays all video files.
        Files with .mp4,.mkv extensions only.
        
        \n""")
    @property
    @cli
    def add(self):
        
        sys.stdout.write("""
                 *add path*
                 
        Executed by user> add path /followed/by/path/to/files
        After adding path, you are prompted to refresh your playlist.
        Files from an added path are just appended to the original list.
        
        
        \n""")
    @property
    @cli
    def all(self):
        
        sys.stdout.write("""
                 *play all*
                 
        Executed by user>play all
        all comes after the play command has been executed.
        play + all, plays all the songs that you have just searched for.
        all alone results to an error(Unknown command).
        
        
        \n""")
    @property
    @cli
    def clear(self):
        
        sys.stdout.write("""
                 *clear*
                 
        Executed by user> clear
        clears the screen.
        
        
        \n""")
    @property
    @cli
    def download(self):
        
        sys.stdout.write("""
                 *download*
                 
        Executed by user>download followed_by_youtube_link
        The download command accepts a YOUTUBE link,option of the media file you want.
        By default it downloads a video.
        
        If you want a specific media type:
            user>download followed_by_youtube_link specify_media_type
            
            for audio:
                user>download followed_by_youtube_link audio
                
            for both media(audio and video):
                user>download folllowed_by_youtube_link both
                
        This is meant to download the file.
        The default resolution quality is 720 for now.
        
        
        \n""")
    @property
    @cli
    def delete(self):
        
        sys.stdout.write("""
                 *delete*
                 
        Executed by user>delete song/numerical_number_of_the_file in searched list
        This command deletes a passed in file.
        
        \n""")
    @property
    @cli
    def rename(self):
        
        sys.stdout.write("""
                 *rename*
                 
        Executed by user>rename followed_by_numeric_value_of_file_in_searched_list followed_by_new_file_name
        Illustration  user>rename 8 new file name
        This command renames a file.
        
        \n""")
        
    @property
    @cli
    def help(self):
        
        sys.stdout.write("""
                 *help*
                 
        Executed by user>help
        Shows the help message.
        
        \n""")
    @property
    @cli
    def play(self):
        
        sys.stdout.write("""
                 *play*
                 
        Executed by user>play folowed_by_artist/song/hint_file_name
        Advisable to insert only a hint_file_name ALONE or hint_artist_name ALONE.
        Example: user>play kenny rodgers
                 user>play coward of the country
                 
        The following is not ideal for an  accurate search, unless you are sure of the title:
            user>play kenny rodgers - coward of the country(not advisable)
            
        For an accurate pick, after media files have been searched:
            0. Zuchu wana official music video
            1. Zuchu Litawachoma official video
            
            user>play zuchu wana 
            (Above execution plays the media 0.)
            
      REMINDER:
          First play is for search unless there is a single match.
          The second play can be used to play a song from the searched media files.
        
        \n""")
    @property
    @cli
    def streamed(self):
        
        sys.stdout.write("""
                 *streamed*
                 
        Executed by user>streamed
        Shows a list of media files that have been played.
        
        \n""")
    @property
    @cli
    def streaming(self):
        
        sys.stdout.write("""
                 *streaming*
                 
        Executed by user>streaming
        Shows a media file that is playing.
        
        \n""")
    @property
    @cli
    def prev(self):
        
        sys.stdout.write("""
                 *prev*
                 
        Executed by user>prev
        plays the previous media.
        Works after selecting a media file using the digits(0-9) only.
        
        \n""")
    @property
    @cli
    def next(self):
        
        sys.stdout.write("""
                 *next*
                 
        Executed by user>next
        plays the next media.
        Works after selecting a media file using the digits(0-9) only.
        
        \n""")
    @property
    @cli
    def repeat(self):
        
        sys.stdout.write("""
                 *repeat*
                 
        Executed by user>repeat
        re-plays the media that has been jsut played.
        Works after selecting a media file using the digits(0-9) only.
        
        \n""")
    @property
    @cli
    def list(self):
        
        sys.stdout.write("""
                 *list all *
                 
        Executed by user>list all
        lists all the media files that have been refreshed.
        
        \n""")
    @property
    @cli
    def search(self):
        
        sys.stdout.write("""
                 *search*
                 
        Executed by user>search followed_by_the_file_keyword
        This search is used to search for a file from youtube and give a link that,
        should be pasted after download  command to download it and add it to your local storage.
        
        \n""")
    @property
    @cli
    def refresh(self):
        
        sys.stdout.write("""
                 *refresh*
                 
        Executed by user>refresh
        scans and updates your playlist.
        
        \n""")
    @property
    @cli
    def exit(self):
        
        sys.stdout.write("""
                 *exit*
                 
        Executed by user> exit
        Closes the media file being played.
        Generally terminates/kills the session.
        
        \n""")
    @property
    @cli
    def total_media(self):
        
        sys.stdout.write("""
                 *total media*
                 
        Executed by user>total media
        shows total numeric value of media in the playlist.
        
        
        \n""")
def more_info(HELPMESSAGE):
    
    MESSAGE = " ".join(HELPMESSAGE.split())
    
    if len(MESSAGE.split(' ')) == 1:
        Manual().help_message
    else:
        FUNCTION = MESSAGE.split()[1]
        
        if FUNCTION == "download":
            Manual().download
        elif FUNCTION == "audio":
            Manual().audio
        elif FUNCTION == "streamed":
            Manual().streamed
        elif FUNCTION == "video":
            Manual().video
        elif FUNCTION == "add":
            Manual().add
        elif FUNCTION == "all":
            Manual().all
        elif FUNCTION == "clear":
            Manual().clear
        elif FUNCTION == "rename":
            Manual().rename
        elif FUNCTION == "delete":
            Manual().delete
        elif FUNCTION == "help":
            Manual().help
        elif FUNCTION == "play":
            Manual().play
        elif FUNCTION == "prev":
            Manual().prev
        elif FUNCTION == "next":
            Manual().next
        elif FUNCTION == "repeat":
            Manual().repeat
        elif FUNCTION == "list":
            Manual().list
        elif FUNCTION == "search":
            Manual().search
        elif FUNCTION == "refresh":
            Manual().refresh
        elif FUNCTION == "exit":
            Manual().exit
        else:
            sys.stdout.write(F"[ERR]{FUNCTION} is not documented/does not exist.\n")
            
        