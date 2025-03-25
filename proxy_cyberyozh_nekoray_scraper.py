import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://127.0.0.1:2080",
    "https": "http://127.0.0.1:2080", 
}

def test_proxy():
    test_url = "https://httpbin.org/ip"  
    try:
        response = requests.get(test_url, proxies=proxies)
        if response.status_code == 200:
            print(f"Proxy is working! Response: {response.json()}")
            return True  
        else:
            print(f"Failed to get a valid response. Status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while testing the proxy: {e}")
        return False

def scrape_hacker_news():
    url = "https://news.ycombinator.com/"

    try:
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:
            print("Successfully fetched Hacker News!")
            soup = BeautifulSoup(response.content, 'html.parser')

            submissions = soup.find_all('tr', class_='athing')

            for submission in submissions:
                rank = submission.find('span', class_='rank').text.strip('.')
                title_element = submission.find('span', class_='titleline').find('a')
                title = title_element.text if title_element else 'No Title'
                link = title_element['href'] if title_element else '#'
                score = submission.find('span', class_='score').text if submission.find('span', class_='score') else 'No Score'
                user = submission.find('a', class_='hnuser').text if submission.find('a', class_='hnuser') else 'Anonymous'
                age = submission.find('span', class_='age').text if submission.find('span', class_='age') else 'Unknown'

                print(f"Rank: {rank}")
                print(f"Title: {title}")
                print(f"Link: {link}")
                print(f"Score: {score}")
                print(f"User: {user}")
                print(f"Age: {age}")
                print('-' * 40)
        else:
            print(f"Failed to fetch Hacker News. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while scraping: {e}")

if __name__ == "__main__":
    if test_proxy():
        scrape_hacker_news()
    else:
        print("Proxy is not working. Exiting...")
