import os
import subprocess
import sys
import time


import argparse
import ctypes
import re
from errors import *
import glob
import os
import glob
import subprocess



translation_dict = {
    'struct': ('static void'),
    'revoid': ('public static void'),
    'restring': ('public static string'),
    'reint': ('public static int'),
    'pubtask': ('public static async Task'),
    'rehouse': ('public static namespace'),
    'refloat': ('public static float'),
    'rebool': ('public static bool'),
    'redictionary': ('public static Dictionary'),
    'relist': ('public static List'),
    'rearray': ('public static Array'),
    'reobject': ('public static object'),
    'rechar': ('public static char'),
    'rebyte': ('public static byte'),
    'reuint': ('public static uint'),
    'reulong': ('public static ulong'),
    'reshort': ('public static short'),
    'reushort': ('public static ushort'),
    'relong': ('public static long'),
    'redecimal': ('public static decimal'),
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
    'bland': ('default'),
    'stop': ('break'),
    'at': ('case'),
    'using': ('using'),
    ';': (';'),
    '//': ('//')

}
keywords = [
    'struct',
    'revoid',
    'restring',
    'reint',
    'pubtask',
    'rehouse',
    'refloat',
    'rebool',
    'pubstring',
    'pubbool',
    'redictionary',
    'relist',
    'rearray',
    'reobject',
    'rechar',
    'rebyte',
    'reuint',
    'reulong',
    'reshort',
    'reushort',
    'relong',
    'redecimal',
    'public',
    'private',
    'protected',
    'static',
    'int',
    'house',
    'float',
    'bool',
    'var',
    'if',
    'else',
    'room',
    'while',
    'for',
    'void',
    'return',
    'stop',
    'continue',
    'true',
    'false',
    'empty',
    'this',
    'base',
    'bland',
    'stop',
    'at',
    'using',
    'static',
    ';',
    'await',
    'catch',
    'Exception',
    '//',
    
]
def InvalidSystax(lnumber, error):
    print_errors(lnumber, error)
    
    
    
def check_transpiled_code(non_transpiled_code, keywords, translation_dict):
    """
    Check if the transpiled code is valid by comparing it with a list of keywords and a translation dictionary.

    Parameters:
    non_transpiled_code (str): The code to be checked.
    keywords (list): A list of valid keywords.
    translation_dict (dict): A dictionary containing translations for certain keywords that dont fit within the keywords list.

    Raises:
    SyntaxError: If an unknown keyword is found in the code.

    Returns:
    bool: True if the code is valid, False otherwise.
    """
    

    inside_string = False
    word = ''
    ignore_line = False
    for char in non_transpiled_code:
        if char == '\n':
       
            ignore_line = False
        elif char == '"':
            inside_string = not inside_string
        elif not inside_string and (char.isalnum() or char == '_'):
            word += char
        elif not inside_string and (char == ' ' or char == '\n') and word:
            if word in keywords or word in translation_dict.keys():
                ignore_line = True
            elif not ignore_line:
                raise SyntaxError(f"Invalid syntax CUSP 00003: Unknown keyword '{word}'")
            word = ''
    return True
    
    
    

def transpile(event): # this is for transpiling
    """ Transpile the input text into C# code.

    Args:
        event (_str_): The input text to transpile.

    Returns:
        _str_: The transpiled C# code.
    """
    lines = event.splitlines()

    translated_lines = []

    # Apply translation line by line based on the dictionary
    for line in lines:

        # Split the line into words and punctuation marks
        words = re.split(r'(\W+)', line)
        translated_words = []
        try:
            check_transpiled_code(line, keywords,translation_dict)
        except Exception as e:
            print_errors(line, e)
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
    """Create the output file.`

    Args:
        translated_text (_str_): returns the translated text
    """
    file_path = "Program.cs"
    with open(file_path, 'w') as file:
        file.write(translated_text)

def Compilee(file_name): 
    """
    Compile the input file.
    Args:
        file_name (_str_): The name of the file to compile.
    """
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
  
    
        

def Compileprojectwithoutput():
    """instead of deleting the file like in the other compile project function, this one keeps the file and saves it to the output folder
    """
    # Read the project file
    try:
        with open("Project.cspm", 'r') as file:
            filedata = file.readlines()  # readlines instead of read
    except Exception as e:
        print_error(f"Error reading project file: {e}")
        exit()

    # Each line is a file with a .cusp extension. We need to transpile each one of them into a .cs file
    try:
        # Get the name of the .csproj file within the same directory
        current_directory = os.getcwd()

        # Find .csproj files in the current directory
        csproj_files = glob.glob(os.path.join(current_directory, "*.csproj"))

        # Get the first .csproj file name
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
            # Get the file name
            file_name = line.strip()  # Remove newline characters
            print(f"Compiling file '{file_name}'...")

            # Open the file
            Compilee(file_name)

            # Check if the OS is Windows or not
            if os.name == "nt":
                # If it is, use dotnet.exe
                subprocess.run(["c:/Program Files/dotnet/dotnet.exe", 'build'], shell=True)
            else:
                # If it is not, use dotnet
                subprocess.Popen(['/usr/local/share/dotnet/dotnet', 'build'], shell=True)

            # Remove the .cs file * not available within --compout
            # os.remove(file_name + ".cs")

    except Exception as e:
        print_error(f"Error compiling file '{file_name}': {e}")
        


def Compileproject(): 
    """ compile the whole project.cspm file
    """
    #read the project file
    try:
        with open("Project.cspm", 'r') as file:
            filedata = file.readlines()  # readlines instead of read
    except Exception as e:
        print_error(f"CUSP 00001`: {e}")
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
            print_error("No .csproj file found in the current directory.")
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
        
    except Exception as e:
        print_error(f"Error compiling file '{file_name}': {e}")
        
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



def Runproject(name):
    """runs a project

    Args:
        name (_str_): the name of the cspm file
        
    """
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
        
        