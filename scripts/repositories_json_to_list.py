import json

with open("../data/search_results.json") as infile:
    data = json.load(infile)

for page in data:
    
    items = data[page]
    for item in items['items']:
        print(item['full_name'])