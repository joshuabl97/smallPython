#!/usr/bin/python3 

import re
import pyperclip

# Regex Version of Strip() that performs on what is currently in clipboard

strip = input("What character would you like to strip from your clipboard?(whitespace is default): ") 

text = str(pyperclip.paste()) 

if strip == '': 
    print(re.sub(r"\s+", "", text)) 
else: 
    print(re.sub(r'('+ strip +')', "" , text)) 
