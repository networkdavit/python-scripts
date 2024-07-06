#IMPORTANT, RUN pip install requests/ pip3 install requests FIRST

import os
import requests
import sys

def download_website_source(url, save_folder):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        domain_name = url.split("//")[-1].split("/")[0]
        file_path = os.path.join(save_folder, f"{domain_name}.html")

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"Source code saved to {file_path}")

    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

url =  sys.argv[1]
save_folder = "downloaded_websites"
download_website_source(url, save_folder)
