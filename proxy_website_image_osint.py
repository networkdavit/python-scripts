import os
import requests
from bs4 import BeautifulSoup
import socks
import socket
import mimetypes

socks.setdefaultproxy(socks.SOCKS5, "ip_address", port, True, "username", "password")
socket.socket = socks.socksocket
def download_image(image_url, folder_path):
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  

        content_type = response.headers.get('Content-Type')
        
        extension = mimetypes.guess_extension(content_type)
        
        if not extension:
            extension = ".jpg" 
        
        image_name = os.path.basename(image_url)
        if not os.path.splitext(image_name)[1]:
            image_name += extension
        
        image_path = os.path.join(folder_path, image_name)
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {image_name}")
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")

def download_images_from_website(url, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        image_tags = soup.find_all('img')

        for img in image_tags:
            img_url = img.get('src')
            img_url = requests.compat.urljoin(url, img_url)
            download_image(img_url, folder_path)

        print("All images downloaded!")
    except Exception as e:
        print(f"Failed to scrape images from {url}: {e}")

if __name__ == "__main__":
    website_url = input("Enter website URL: ")

    save_folder = 'downloaded_images'

    download_images_from_website(website_url, save_folder)

