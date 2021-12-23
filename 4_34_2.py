import json
import requests
from pprint import pprint


params = {
    'q': 'robot',
    'subreddit': 'technology',
    'sort_type': 'created_utc',
    'size': 100
}

resp = requests.get('https://api.pushshift.io/reddit/search/comment/', params=params)
data = resp.json()['data']

coment = list(com.get('body') for com in data)
pprint(coment)
with open('coment.json', 'w') as file:
    json.dump(coment, file)

