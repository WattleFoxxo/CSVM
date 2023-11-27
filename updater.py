from httpx import get
from downloader import download_nupkg
from errors import *
import os, socket, socketserver, sys, requests, json, urllib.request, urllib.parse, urllib.error, platform, version, time, webbrowser, subprocess,argparse,concurrent
from version import __CSVM__, __HOME__, __name__
from tqdm import tqdm

#################
# updater script
# for the CSVM
# made by charlie-sans
# this script will check for updates to the CSVM
# and will update if there is a new version
#################
def simulate_loading(background_function):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(background_function)
        while not future.done():
            yield
            time.sleep(0.05)
        return future.result()
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

def slow(text):
    """prints text one character at a time

    Args:
        text (str): the text to print
    """
    for i in text:
        print(i, end="")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def download(url, filename):
    """downloads a file from the intrnet

    Args:
        url (str): the url to get the file from
        filename (str): the file name
        
    """
    try:
       
        file = requests.get(url)
        with open(filename, "wb") as f:
            f.write(file.content)
            f.close()
    except Exception as e:
        print_error(f"could not update CubeScript: {e}")

    
def main():
    slow("welcome to the CubeScript updater")
    slow("checking for updates...")
    for i in tqdm(range(100)):
        time.sleep(0.01)
    slow("getting version info...")
    for i in tqdm(range(100)):
        time.sleep(0.01)
    slow("done!")
    time.sleep(0.5)
    slow("Now, before we get started, i just want to ask you a few questions")
    time.sleep(0.5)
    slow("first, what is your Operating system? { windows, linux }")
    
    operating = input(">>> ")
    if operating == "windows":
        try:
            CSVM = get_version("CSVM")
            home = get_version("Home.dll")
            if home != __HOME__:
                slow("there is a new version of Home.dll available!")
                slow("ill go grab that for you now")
                url = "https://github.com/OpenStudioCorp/CSVM/raw/main/raw/main/Home.dll"
                filename = "home.dll"
                download(filename, url)
            if CSVM != __CSVM__:
                slow("there is a new version of CSVM available!")
                slow("ill go grab that for you now")
                url = "https://github.com/OpenStudioCorp/CSVM/raw/main/raw/main/CSVM.exe"
                filename = "CSVM.exe"
                download(filename, url)
                slow("done!")
            else:
                slow("you are up to date!")
                sys.exit()
                
                
        except Exception as e:
            print_error(f"could not get version info: {e}")
            slow("well, thats weird... seems like i can't get the version info?")
    elif operating == "linux":
        try:
            CSVM = get_version("CSVM")
            home = get_version("Home.dll")
            if home != __HOME__:
                slow("there is a new version of Home.dll available!")
                slow("ill go grab that for you now")
                url = "https://github.com/OpenStudioCorp/CSVM/raw/main/raw/main/Home.dll"
                filename = "home.dll"
                download(filename, url)
            if CSVM != __CSVM__:
                slow("there is a new version of CSVM available!")
                slow("ill go grab that for you now")
                url = "https://github.com/OpenStudioCorp/CSVM/raw/main/raw/main/CSVM.bin"
                filename = "CSVM.exe"
                download(filename, url)
                slow("done!")
            else:
                slow("you are up to date!")
                sys.exit()
                
                
        except Exception as e:
            print_error(f"could not get version info: {e}")
            slow("well, thats weird... seems like i can't get the version info?")
            slow("i'd say try again, if this keeps happening then you might have to update manually")
            slow("you can do this by going to the github page and downloading the latest release")
            slow("oh and please make a issue on github if this keeps happening")
            
    else:
        slow("hmmmmm, there doesnt seem to be a operating system with that name within my files...")
        slow("i'd say try again.")
        exit()
    
main()
    