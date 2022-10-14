#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 12:07:16 2022

@author: armsy326
"""
import argparse
import sys

animation = """
         created by Armsy326
                         fuck GUIs:)-
                 Am a terminal media player
                   
Type 'help' to understand some of the basic executable statements.
To clear statements type 'clear'.
To exit simply type 'exit'.

"""

def initialize():
    sys.stdout.write(animation)
    
def main():
    initialize()
    
    while 1:
        from armsy326 import whole_sequence
        whole_sequence()  
        
parser  =  argparse.ArgumentParser(prog='armsy326', description="This is a command line music player tool.")
parser.add_argument('--version', action='version', version='0.0.1')
args  =  parser.parse_args()


if sys.platform != "linux":
    sys.stdout.write("WARNING:This executable file was created to run on gnu/linux.Although it can be configured to run on other Operating systems.")
    main()
else:
    main()
