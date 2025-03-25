import requests

proxies = {
    "http": "http://127.0.0.1:2080",
    "https": "http://127.0.0.1:2080", 
}

url = "https://httpbin.org/ip" 

try:
    
    response = requests.get(url, proxies=proxies)
    if response.status_code == 200:
        print(f"Proxy working! Response from {url}: {response.json()}")
    else:
        print(f"Failed to get a valid response. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
