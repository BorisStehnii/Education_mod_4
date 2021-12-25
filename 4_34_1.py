import requests
from pprint import pprint


params = {
    'format': 'json',
    'action': 'query',
    'titles': 'robot',
    'rvprop': 'timestamp|content'
}

resp = requests.get('https://en.wikipedia.org/w/api.php/', params=params)
# resp = requests.get('http://en.wikipedia.org/w/api.php?'
#                     'action=query&titles=robot&rvprop=timestamp|content&format=json')
with open("robots_wiki.txt", "w") as file:
    file.write(resp.text)

pprint(resp.text)
