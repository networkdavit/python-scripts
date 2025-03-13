import requests
from bs4 import BeautifulSoup
import time  
url = "https://www.shodan.io/search?query=webcamxp"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('div', class_='two columns result-details')

    for result in results:
        hostnames = result.find_all('li', class_='hostnames text-secondary')
        
        for hostname in hostnames:
            print(f"Host/IP: {hostname.get_text(strip=True)}")
        
        search_links = result.find_all('a', href=True)
        
        for link in search_links:
            link_url = f"https://www.shodan.io{link['href']}"
            print(f"Search Link: {link_url}")
        
        print("-" * 50)
        
        time.sleep(10) 

else:
    print(f"Error: {response.status_code}")
