import json
import multiprocessing as mp
import requests
from pprint import pprint


def request_url(url_, params_, text_):

    resp = requests.get(url_+f'?q={text_}', params=params_)

    data = resp.json()['data']
    coment = {text_: [com.get('body') for com in data]}

    try:
        with open('coment_text_mp.json', 'r') as file:
            data_ = json.load(file)
            pprint(data_)
    except:
        data_ = dict()

    data_.update(coment)
    with open('coment_text_mp.json', 'w') as file:
        json.dump(data_, file, indent=4)


if __name__ == "__main__":
    url_add = 'https://api.pushshift.io/reddit/search/comment/'

    text_request = ['robot', 'nanotechnology', 'neural network']
    params = {
        'subreddit': 'technology',
        'sort_type': 'created_utc',
        'size': 100
    }
    with mp.Pool() as pool:

        for text in text_request:
            pool.apply(request_url, args=(url_add, params, text))

