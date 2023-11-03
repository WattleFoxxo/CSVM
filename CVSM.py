__name__ = "CVSM"

__version__ = "0.1.2"


import webbrowser
import os
import subprocess
import sys
import time
import transpiler
from transpiler import transpile, createoutput, Compile
import pythonnet
import argparse
from pythonnet import *
import re


# setup argument parser
parser = argparse.ArgumentParser(description="Cubescript to C# transpiler")
parser.add_argument(
    "-o", type=str, nargs="?", help="the output file for the cusp program"
)
parser.add_argument("-t", action="store_true", help="Termanial")
parser.add_argument("-help", action="store_true", help="help")
parser.add_argument(
    "input_file", type=str, nargs="?", help="the input file for the cusp program"
)
parser.add_argument("-ve", action="store_true", help="version")
parser.add_argument("-v", action="store_true", help="verbose")
parser.add_argument("-new", action="store_true", help="new project")
parser.add_argument("-c", action="store_true", help="compile")
parser.add_argument("-r", action="store_true", help="run")
parser.add_argument("-d", action="store_true", help="debug")


args = parser.parse_args()


def exit():
    print("Exiting...")
    sys.exit()


def help():
    # open a web browser to the documentation
    print("Opening documentation...")
    webbrowser.open("https://CubeScript.vercel.app/learn/functions")


if args.ve:
    print("CubeScript CSVM Version:" + __version__)
    exit()

if args.t:
    print("Welcome to the Cubescript to C# transpiler!")
    print("Type 'new' to create a new project")
    print("using -r will run the program")
    print("using -c will compile the program")
    print("using -t will open the terminal for interacting with Documentation")
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


def main():
    with open(args.input_file, "r") as file:
        event = file.read()
    transpile(event)
    print("Transpile complete")
    print("Compiling...")
    print("CubeScript CSVM v0.1.1")
    # get the csproj file

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
else:
    if args.c:
        print("Compiling...")
        print(f"CubeScript CSVM {__version__}")
        with open(args.input_file, "r") as file:
            event = file.read()
        transpile(event)
        # get the csproj file
        subprocess.call(["dotnet", "build"])
        print("Compile complete")
        exit()
    elif args.r:
        print("Running...")
        print(f"CubeScript CSVM{__version__}")
        with open(args.input_file, "r") as file:
            event = file.read()
        transpile(event)
        # get the csproj file
        subprocess.call(["dotnet", "run"])

        print("Run complete")
        exit()
    else:
        help()
        exit()
