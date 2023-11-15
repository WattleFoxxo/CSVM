"""
This script is the main file for the CubeScript VM. It includes other files such as errors.py, templates.py, and transpiler.py. The script provides functions to check if the current version of CSVM and the 'home.dll' library are up-to-date by comparing them with the latest version available on a web server. It also provides a function to get the version of a project with the given name, as listed in the OpenStudioCorpProjects.json file on GitHub. Additionally, the script includes an argument parser to handle various command-line arguments such as compiling, running, and creating new projects. Finally, the script calls the main() function to execute the program.
"""
import webbrowser
import os
import subprocess
import sys
import time
import transpiler
from transpiler import transpile, createoutput, Compileproject, Compileprojectwithoutput
import templates
from templates import create_project, CreateDll
import argparse
import re
import requests
import json
import urllib.request
import urllib.parse
import urllib.error
import templates
from errors import *
from templates import create_project, CreateDll
import ssl
from colorama import Fore, Style

#################
##CubeScript VM##
#################

# made by Charlie-sans
# this is the main file for the CubeScript VM
# other files include
# - errors.py (for errors)
# - templates.py (for templates)
# - transpiler.py (for transpiling)
# - tests.py (for testing) * not included within the final build



__name__ = "CVSM"
__version__ = "1.2.1"
__dllversion__ = "1.0.0"

##important stuff##

def get_version(name):
    """
    Returns the version of a project with the given name, as listed in the OpenStudioCorpProjects.json file on GitHub.

    Args:
        name (str): The name of the project to get the version for.

    Returns:
        str: The version of the project with the given name, or None if no project with that name is found.
    """
    version = requests.get("https://raw.githubusercontent.com/OpenStudioCorp/NewOpenStudioCorpSite/main/OpenStudioCorpProjects.json")
    data = json.loads(version.text)
    
    for item in data:
        if item['Name'] == name:
            return item['Version']


def homedlllocation():
    """
    Check if the home.dll file is within the current directory.

    Returns:
    bool: True if the file exists, False otherwise.
    """
    if os.path.isfile("home.dll"):
        return True
    else:
        return False
    


def CheckCSVM():
    """
    Check if the current version of CSVM is up-to-date by comparing it with the latest version available on a web server.
    If the current version is outdated, prompt the user to download the latest version.
    """
    version = requests.get("https://raw.githubusercontent.com/OpenStudioCorp/NewOpenStudioCorpSite/main/OpenStudioCorpProjects.json")
    name = 'CSVM'  
    version = get_version(name)
    if version == __version__:
        pass
    else:
        print("\n")
        print_info("hey! there is a new version of CSVM!")
        print_link("Click here to download the new version", "https://CubeScript.vercel.app/Download ")
        print("\n")
        


def CheckHomedll():
    """
    Check if the current version of the 'home.dll' library is up-to-date by comparing its version number with the one
    available on a web server. If the version number is different, prompt the user to download the new version.
    """
    name = 'home.dll'  
    version = get_version(name)
    if version == __dllversion__:
        pass
    else:
        print("\n")
        print_info("hey! there is a new version of the standard Home library!")
        print_link("Click here to download the new version", "https://CubeScript.vercel.app/Download ")
        print("\n")

## important stuff ##


# setup argument parser
parser = argparse.ArgumentParser(description="Cubescript to C# transpiler")
parser.add_argument("-o", type=str, nargs="?", help="the output file for the cusp program")
parser.add_argument("-t", action="store_true", help="Termanial")
parser.add_argument("-help", action="store_true", help="help")
parser.add_argument("input_file", type=str, nargs="?", help="the input file for the cusp program")
parser.add_argument("-ve", action="store_true", help="version")
parser.add_argument("-v", action="store_true", help="verbose")
parser.add_argument("-new", action="store_true", help="new project")
parser.add_argument("-compile", action="store_true", help="compile")
parser.add_argument("-r", action="store_true", help="run")
parser.add_argument("-d", action="store_true", help="debug")
parser.add_argument("-compout", action="store_true", help="compile")
args = parser.parse_args()




def exit():
    """
    Exits the program.

    This function prints a message indicating that the program is exiting, and then calls the sys.exit() function to terminate the program.
    """
    print("Exiting...")
    sys.exit()


def help():
    # open a web browser to the documentation
    print("Opening documentation...")
    webbrowser.open("https://CubeScript.vercel.app/learn/functions")


if args.ve:
    """prints the version
    """
    print("CubeScript CSVM Version:" + __version__)
    exit()

# get the directory of the script for later use
script_dir = os.path.dirname(os.path.realpath(__file__))





def open_help():
    print("Welcome to the Cubescript to C# transpiler!")
    print("Type 'new' to create a new project")
    print("using -r as a argument will run the program")
    print("using -c will as a argument compile the program")
    print(
        "using -t without a file and as a argument will open the terminal for interacting with Documentation"
    )
def open_term_help():
    print("welcome to the official CubeScript terminal!")
    print("unfortunatly there is not much you can do here")
    print("type 'help' for help")
    print("type 'exit' to exit")
    
if args.t:
    open_term_help()
    while True:
        command = input(">>> ")
        if command == "help":
            help()
        elif command == "exit":
            exit()
        else:
            print("Invalid command")
            print("Type 'help' for help")
            continue


def main():
    """
    The main function of the CSVM program. It checks for the presence of required files, compiles the project, and creates a new project if needed.
    """
    CheckCSVM()
    CheckHomedll()
    homedlllocation()
    
    # use checkhomedll to check if the home.dll is in the folder
    if homedlllocation() == False:
        print_error("home.dll not found! Please download it from the website")
        webbrowser.open_new_tab("https://cubescript.vercel.app/Download")
        exit()

    
    if args.compile:
        try:
            print("Compiling...")
            Compileproject()
            with open("Project.cspm", 'r') as file:
                filedata = file.readlines()
            if os.name == "nt":
            # if it is, use dotnet.exe
                subprocess.run(["c:/Program Files/dotnet/dotnet.exe", 'build'])
            else:
            # if it is not, use dotnet
                subprocess.Popen(['/usr/bin/dotnet', 'build'])
            # remove the .cs file
            for line in filedata:
                # get the file name
                file_name = line.strip()
                os.remove(file_name + ".cs")
        
            exit()
    
        except Exception as e:
            print_error(f"Error compiling file: {e}")
            exit()
    if args.compout:
        try:
            print("Compiling...")
            Compileproject()
            with open("Project.cspm", 'r') as file:
                filedata = file.readlines()
            if os.name == "nt":
            # if it is, use dotnet.exe
                subprocess.run(["c:/Program Files/dotnet/dotnet.exe", 'build'])
            else:
            # if it is not, use dotnet
                subprocess.Popen(['/usr/bin/dotnet', 'build'])
            # remove the .cs file
            for line in filedata:
                # get the file name
                file_name = line.strip()
                
            exit()
        except Exception as e:
            print_error(f"Error compiling file: {e}")
            exit()
    elif args.input_file == "new":
        name = input("Name of project: ")
        type = input("Type of project (dll, executable): ")
        if type == "dll":
            CreateDll(name)
            exit()
        elif type == "executable":
            create_project(name)
            exit()
    #elif args.input_file == "update":
    elif args.input_file == "ouput":
        Compileprojectwithoutput()
        exit()
main()