#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:49:31 2022

@author: armsy326
"""

#This module is a collection of possible
#errors that can occur in this script.
#Also custom exceptions are created for
#unorthodox executions.

class Errors(Exception):
    
    pass

class UnknownCommand(Exception):
    
    def __init__(self, msg):
        
        self.msg = msg
  
command = "hell"
try:
    if command == "hello":
        
        print("nooa")
        
except UnknownCommand as e:
    print("kiler")
    print(e)
        
    
    
    