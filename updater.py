from errors import *
import os
import socket
import socketserver
import sys
import requests
import json
import urllib.request
import urllib.parse
import urllib.error
import platform
import time
import webbrowser
import subprocess
import argparse

#################
# updater script
# for the CSVM
# made by charlie-sans
# this script will check for updates to the CSVM
# and will update if there is a new version
#################




if platform.system == "Windows":
    try:
        url = "https://github.com/charlie-sans/CSVM/raw/main/CSVM.exe"
        file = requests.get(url)
        with open("CSVM.exe", "wb") as f:
            f.write(file.content)
            f.close()
    except Exception as e:
        print_error(f"could not update CSVM: {e}")
else:
    try:
        url = "https://github.com/charlie-sans/CSVM/raw/main/CSVM.bin"
        file = requests.get(url)
        with open("CSVM.bin", "wb") as f:
            f.write(file.content)
            f.close()
    except Exception as e:
        print_error(f"could not update CSVM: {e}")



