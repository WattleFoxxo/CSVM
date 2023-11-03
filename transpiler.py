import os
import subprocess
import sys
import time

import pythonnet
import argparse
from pythonnet import *
import re




translation_dict = {
    'struct': ('static void'),
    'int': ('int'),
    'house': (' namespace '),
    'float': (' float '),
    'bool': (' bool '),
    'if': (' if '),
    'else': (' else '),
    'room': ('class'),
    'while': (' while '),
    'for': (' foreach '),
    ' > ': (' in '),
    'void': (' void '),
    'return': (' return '),
    'stop': (' break '),
    'continue': (' continue '),
    'true': (' true '),
    'false': (' false '),
    'null': (' null '),
    'new': (' new '),
    'this': (' this '),
    'base': (' base '),
    'AT ': (' case '),
    'bland': ('default'),
    'stop': ('break'),
    'at': ('case')

}

def createoutput(translated_text):
    file_path = "Program.cs"
    with open(file_path, 'w') as file:
        file.write(translated_text)

def Compile(translated_text,name):
    file_path = name + ".cs"
    with open(file_path, 'w') as file:
        file.write(translated_text)
    time.sleep(1)
    print("Compiling...")

    

def start(cspm_file):
    # this sets up a sln like workspace for the user
    # this will allow the user to create a new project

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    
    # now we check the file and if it contains exactly what we need
    #<HEAD>
    #    <version>1.2</version>
    #    <encoding>UTF-8</encoding>
    #    <stagingArea>
    #        <Library>Home</Library> # as many libraries as you want
    #        
    #    </stagingArea>
    #</HEAD>

    with open(cspm_file, 'r') as file:
        filedata = file.read()

    # check the whole file and see if it contains the above, if not, error out

    if "<HEAD>" in filedata:
        print("Found <HEAD>")
    else:
        print("Error: <HEAD> not found")
        sys.exit()
    if "<version>" in filedata:
        print("Found <version>")
    else:
        print("Error: <version> not found")
        sys.exit()
    if "<encoding>" in filedata:
        print("Found <encoding>")
    else:
        print("Error: <encoding> not found")
        sys.exit()
        


def transpile(event):
    lines = event.splitlines()

    translated_lines = []

    # Apply translation line by line based on the dictionary
    for line in lines:

        # Split the line into words and punctuation marks
        words = re.split(r'(\W+)', line)
        translated_words = []

        for word in words: # get the input text
            try:
                # Convert word to lower case
                lower_word = word.lower()
                if lower_word in translation_dict:
                    # Preserve the original case of the word
                    if word[0].isupper():
                        translated_words.append(translation_dict[lower_word].capitalize())
                    else:
                        translated_words.append(translation_dict[lower_word])
                else: #if the word is not in the dictionary
                    translated_words.append(word)
            except Exception as e:
                print(f"Error translating word '{word}': {e}")
                translated_words.append(word)

        translated_line = "".join(translated_words)
        translated_lines.append(translated_line)

    translated_text = "\n".join(translated_lines)
    createoutput(translated_text)
    # Display the translated text in the output field