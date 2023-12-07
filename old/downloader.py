import os
import requests
import zipfile
import argparse
import sys


parser = argparse.ArgumentParser(description="Download a NuGet package and extract the .dll file from it.")
parser.add_argument('package_name', help="The name of the NuGet package to download")

parser.add_argument('version', help="The version of the NuGet package to download")

args = parser.parse_args()

package_name = args.package_name
version = args.version



BASE_URL = 'https://api.nuget.org/v3-flatcontainer/'

def download_nupkg(package_name, version):
    url = BASE_URL + package_name.lower() + '/' + version + '/' + package_name.lower() + '.' + version + '.nupkg'

    # Send a HTTP request to the URL
    response = requests.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the path of the current script
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Create the full path for the new file
        file_path = os.path.join(script_dir, package_name.lower() + '.' + version + '.nupkg')

        # Write the contents of the response to a new file
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        


def extract_dll(nupkg_filename):
    # Get the path of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Create the full path for the .nupkg file
    nupkg_path = os.path.join(script_dir, nupkg_filename)

    # Open the .nupkg file
    with zipfile.ZipFile(nupkg_path, 'r') as zip_ref:
        # Iterate over the files in the .nupkg file
        for filename in zip_ref.namelist():
            # If the file is a .dll file
            if filename.endswith('.dll'):
                # Extract the .dll file to the same directory as the script
                zip_ref.extract(filename, script_dir)
                
                
def Main():
    download_nupkg(package_name, version)
    extract_dll(package_name.lower() + '.' + version + '.nupkg')
    print("Done!")
    
if __name__ == '__main__':
    Main()