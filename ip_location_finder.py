#first of all do 'pip install requests', or 'pip3 install requests'
import requests
import sys 

def ip_geolocation(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        geo_data = response.json()
        print(f"IP: {geo_data['ip']}")
        print(f"City: {geo_data['city']}")
        print(f"Region: {geo_data['region']}")
        print(f"Country: {geo_data['country']}")
        print(f"Org: {geo_data['org']}")
    else:
        print(f"Error: {response.status_code}")

ip = sys.argv[1]
ip_geolocation(ip)
                   
