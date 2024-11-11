import os
import requests
from bs4 import BeautifulSoup
import socks
import socket
import mimetypes

# Set up SOCKS5 proxy
def set_socks_proxy(ip_address, port, username, password):
    socks.setdefaultproxy(socks.SOCKS5, ip_address, port, True, username, password)
    socket.socket = socks.socksocket
    print("Proxy set successfully.")

# Function to download a single image
def download_image(image_url, folder_path):
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Check for any request errors

        content_type = response.headers.get('Content-Type')
        
        extension = mimetypes.guess_extension(content_type)
        if not extension:
            extension = ".jpg"  # Default to .jpg if no content type or extension found
        
        # Ensure the image has a valid name
        image_name = os.path.basename(image_url)
        if not os.path.splitext(image_name)[1]:  # If the image name lacks an extension
            image_name += extension
        
        image_path = os.path.join(folder_path, image_name)
        
        # Save the image to the specified folder
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        
        print(f"Downloaded: {image_name}")
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")

# Function to download images from a webpage
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
            if img_url:
                img_url = requests.compat.urljoin(url, img_url)
                download_image(img_url, folder_path)

        print("All images downloaded!")
    except Exception as e:
        print(f"Failed to scrape images from {url}: {e}")

if __name__ == "__main__":
    # Set proxy details here
    proxy_ip = input("Enter proxy IP: ")
    proxy_port = int(input("Enter proxy port: "))
    proxy_username = input("Enter proxy username: ")
    proxy_password = input("Enter proxy password: ")

    # Set up the SOCKS5 proxy
    set_socks_proxy(proxy_ip, proxy_port, proxy_username, proxy_password)

    # Get the website URL from the user
    website_url = input("Enter website URL: ")

    # Set the folder to save images
    save_folder = 'downloaded_images'

    # Download images from the specified website
    download_images_from_website(website_url, save_folder)
