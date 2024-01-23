import requests
import sys
import json

n_pages = 10
query = "website"

url = f"https://api.github.com/search/repositories?q={query}++is%3Apublic&per_page=100&page="

responses = dict()

for i in range(1, n_pages+1):
    print(f"progress: {i}/{n_pages}", end='\r', file=sys.stderr)
    response = requests.get(url+str(i))
    if (response.status_code!=200):
        print(f"page {i} failed with error {response.status_code}", file=sys.stderr)
    else:
        responses[i]=response.json()
    
with open("../data/search_results.json", 'w') as outfile:
    json.dump(responses, outfile)