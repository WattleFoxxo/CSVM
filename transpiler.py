import os
import subprocess
import sys
import time


import argparse

import re
from errors import *
import glob



translation_dict = {
    'struct': ('static void'),
    'revoid': ('public static void'),
    'restring': ('public static string'),
    'reint': ('public static int'),
    'pubtask': ('public static async Task'),
    'rehouse': ('public static namespace'),
    'refloat': ('public static float'),
    'rebool': ('public static bool'),
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
    'empty': (' null '),

    'this': (' this '),
    'base': (' base '),
    'AT ': (' case '),
    'bland': ('default'),
    'stop': ('break'),
    'at': ('case')

}
def transpile(event): # this is for transpiling
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
    return translated_text
    

def createoutput(translated_text): # this is for creating files
    file_path = "Program.cs"
    with open(file_path, 'w') as file:
        file.write(translated_text)

def Compilee(file_name): # this is for compiling a single file
    file_path = file_name + ".cs"
    file_name = file_name + ".cusp"
    print(f"Compiling file '{file_name}'...")
    print(f"Transpiling file {file_path}")
    with open(file_name, 'r') as file:
        event = file.read()
    translated_text = transpile(event)
    with open(file_path, 'w') as file:
        file.write(translated_text)
    print("Compiling...")
  
    


def start(cspm_file): # unused
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
        
def Compileprojectwithoutput(): # this is used for compiling a full project full of files that people would want to use
    #read the project file
    try:
        with open("Project.cspm", 'r') as file:
            filedata = file.readlines()  # readlines instead of read
    except Exception as e:
        print_error(f"Error reading project file: {e}")
        exit()
# each line is a file with a .cusp extension
# we need to transpile each one of them into a .cs file

    try:
        #get the name of the .csproj file within the same directory
       

        # get the current directory
        current_directory = os.getcwd()

        # find .csproj files in the current directory
        csproj_files = glob.glob(os.path.join(current_directory, "*.csproj"))

        # get the first .csproj file name
        if csproj_files:
            csproj_file_name = os.path.basename(csproj_files[0])
            print(f".csproj file found: {csproj_file_name}")
        else:
            print_warning("No .csproj file found in the current directory.")
            exit()
    except Exception as e:
        print_error(f"Error finding .csproj file: {e}")
        exit()

    try:
        for line in filedata:
            # get the file name
            file_name = line.strip()  # remove newline characters
            print(f"Compiling file '{file_name}'...")
    except Exception as e:
        print_error(f"Error reading project file: {e}")
        exit()
    try:
        # open the file
        Compilee(file_name)
        
        #check if the os is windows or not
        if os.name == "nt":
            # if it is, use dotnet.exe
            subprocess.run(["c:/Program Files/dotnet/dotnet.exe", 'build'], shell=True)
        else:
            # if it is not, use dotnet
            subprocess.Popen(['/usr/local/share/dotnet/dotnet', 'build'], shell=True)
        # remove the .cs file
        
        # os.remove(file_name + ".cs")
        
    except Exception as e:
        print_error(f"Error compiling file '{file_name}': {e}")
        


def Compileproject(): # this is used for compiling a full project full of files that people would want to use
    #read the project file
    try:
        with open("Project.cspm", 'r') as file:
            filedata = file.readlines()  # readlines instead of read
    except Exception as e:
        print_error(f"Error reading project file: {e}")
        exit()
# each line is a file with a .cusp extension
# we need to transpile each one of them into a .cs file

    try:
        #get the name of the .csproj file within the same directory
       

        # get the current directory
        current_directory = os.getcwd()

        # find .csproj files in the current directory
        csproj_files = glob.glob(os.path.join(current_directory, "*.csproj"))

        # get the first .csproj file name
        if csproj_files:
            csproj_file_name = os.path.basename(csproj_files[0])
            print(f".csproj file found: {csproj_file_name}")
        else:
            print_warning("No .csproj file found in the current directory.")
            exit()
    except Exception as e:
        print_error(f"Error finding .csproj file: {e}")
        exit()

    try:
        for line in filedata:
            # get the file name
            file_name = line.strip()  # remove newline characters
            print(f"Compiling file '{file_name}'...")
    except Exception as e:
        print_error(f"Error reading project file: {e}")
        exit()
    try:
        # open the file
        Compilee(file_name)
        
        #check if the os is windows or not
        if os.name == "nt":
            # if it is, use dotnet.exe
            subprocess.run(["c:/Program Files/dotnet/dotnet.exe", 'build'], shell=True)
        else:
            # if it is not, use dotnet
            subprocess.Popen(['/usr/bin/dotnet', 'build'], shell=True)
        # remove the .cs file
        
        # os.remove(file_name + ".cs")
        
    except Exception as e:
        print_error(f"Error compiling file '{file_name}': {e}")
        

def Runproject(name):
    #read the project file
    with open(name + ".cspm", 'r') as file:
        filedata = file.read()
    # each line is a file with a .cusp extension
    # we need to transpile each one of them into a .cs file==
    
    for line in filedata:
        # get the file name
        file_name = line
        # open the file
        with open(file_name, 'r') as file:
            event = file.read()
        # transpile the file
        translated_text = transpile(event)
        # create the output file
        createoutput(translated_text)
        
        subprocess.run(["dotnet run"])
        
        