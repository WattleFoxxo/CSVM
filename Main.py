import tkinter as tk
translation_dict = {
    'struct': ('private static void'),
    'int': ('int'),
    'house': (' namespace '),
    'float': (' float '),
    'bool': (' bool '),
    'if': (' if '),
    'else': (' else '),
    'room': ('class'),
    'while': (' while '),
    'string': ('var'),
    'for': (' foreach '),
    ' > ': (' in '),
    'double': ('var'),
    'char': ('var'),
    'long': ('var'),
    'byte': ('var'),
    'short': ('var'),
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

}
import os
import subprocess
import sys
import time

import pythonnet
import argparse
from pythonnet import *
import re




#@ setup argument parser
parser = argparse.ArgumentParser(description='Cubescript to C# transpiler')

parser.add_argument('-t',  action='store_true', help='Termanial')
parser.add_argument('-help', action='store_true', help='help')
parser.add_argument('input_file', type=str, help='the input file for the cusp program')
parser.add_argument('-ve',  action='store_true', help='version')
parser.add_argument('-v',  action='store_true', help='verbose')


args = parser.parse_args()

if args.t:
    print("Welcome to the Cubescript to C# transpiler!")
    print("Type 'help' for help")
    print("Type 'compile' to compile a Cubescript file")
   

# Load the necessary .NET assemblies
script_dir = os.path.dirname(os.path.realpath(__file__))

def createoutput(translated_text):
    
    file_path = "Program.cs"
    with open(file_path, 'w') as file:
        file.write(translated_text)

        




def translate_text(event):
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

def create_project(name):
    print("Creating project...")
    with open("Program.cs", 'w') as file:
        file.write("")
    with open("{0}.csproj".format(name), 'w') as file:
        file.write("""<Project Sdk="Microsoft.NET.Sdk">

  <ItemGroup>
        <!-- .cs files -->
    <Compile Include="program.cs" />
    <Reference Include="System" />
    <Reference Include="System.IO" />
    <Reference Include="System.Linq" />
    <Reference Include="System.Text" />
    <Reference Include="System.Threading.Tasks" />
    <Reference Include="System.Collections.Generic" />
    <Reference Include="System.Diagnostics" />
    <Reference Include="System.Runtime" />
    <Reference Include="Home.dll" />
  </ItemGroup>

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net6.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
""")
    with open("Program.cusp", 'w') as file:
        file.write("using static home;\n\nPrint(\"Hello World!\");")
 
        print("Project created! \n\n\n\n")
        print("You can run './cusp compile' to compile your project")
        print("Or you can add the CVSM to your path")
        print("Please make sure that you have .NET 6.0 installed")
        print("You can download it from https://dotnet.microsoft.com/download/dotnet/6.0")
        print("And you have Home.dll in the same folder as the program")
        print("you should have been given a copy of Home.dll with this program from the zip file you downloaded")
def open_help():
    print("Welcome to the help page!")
    print("Type 'build' to compile a Cubescript file")
    print("Type 'new' to create a new project")
    print("Type 'exit' to exit the program")

def main():
    with open(args.input_file, 'r') as file:
        event = file.read()
    translate_text(event)
    print("Transpile complete") 
    print("Compiling...")
    
    subprocess.call(["dotnet", "build"])
    print("Compile complete")
if args.input_file == "":
    print("You can run 'cusp new' to create a new project")
    exit()
elif args.input_file == "new":
    print("Creating new project...")
    name = input("What do you want to name your project? ")
    create_project(name)
    print("Project created!")
    exit()
elif args.input_file == "help":
    open_help()
    exit()
else :
    main()
    exit()
