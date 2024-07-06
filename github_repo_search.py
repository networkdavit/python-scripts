import requests
import sys

def search_github_repositories(keyword):
    url = f"https://api.github.com/search/repositories?q={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()['items']
        for repo in repos[:5]:  
            print(f"Name: {repo['name']}")
            print(f"URL: {repo['html_url']}")
            print(f"Description: {repo['description']}\n")
    else:
        print(f"Error: {response.status_code}")

keyword = sys.argv[1]
search_github_repositories(keyword)
