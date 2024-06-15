#first run pip install googlesearch-python or pip3 install googlesearch-python



import argparse
from googlesearch import search

def google_dork_search(query, num_results):
    results = []
    for result in search(query, num_results=num_results):
        results.append(result)
    return results

def display_results(dork, results):
    print(f"Results for dork: {dork}")
    for result in results:
        print(result)
    print("-" * 60)

def main():
    parser = argparse.ArgumentParser(description="Google Dork Automation Tool")
    parser.add_argument("query", help="Query keyword for Google Dorking")
    parser.add_argument("--num_results", type=int, default=10, help="Number of results to return per dork")
    args = parser.parse_args()

    query_keyword = args.query
    num_results = args.num_results

    dorks = [
        f'site:{query_keyword}',
        f'inurl:{query_keyword}',
        f'intitle:{query_keyword}',
        f'intext:{query_keyword}',
        f'filetype:pdf {query_keyword}',
        f'inurl:login {query_keyword}',
        f'inurl:admin {query_keyword}',
        f'inurl:index.of {query_keyword}',
        f'site:*/ {query_keyword}',
        f'allinurl:{query_keyword}'
    ]

    for dork in dorks:
        results = google_dork_search(dork, num_results)
        display_results(dork, results)

if __name__ == "__main__":
    main()
