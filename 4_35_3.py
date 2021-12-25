import json
import threading
import requests
from pprint import pprint


def request_url(url_, params_, text_, lock_):

    resp = requests.get(url_+f'?q={text_}', params=params_)
    lock_.acquire()
    data = resp.json()['data']
    coment = {text_: [com.get('body') for com in data]}

    # pprint(f"__________________________{text_}______________________________________")
    # pprint(coment)

    try:
        with open('coment_text.json', 'r') as file:
            data_ = json.load(file)
            pprint(data_)
    except:
        data_ = dict()

    data_.update(coment)
    with open('coment_text.json', 'w') as file:
        json.dump(data_, file, indent=4)
    lock_.release()


url_add = 'https://api.pushshift.io/reddit/search/comment/'
text_request = ['robot', 'nanotechnology', 'neural network']
params = {
    'subreddit': 'technology',
    'sort_type': 'created_utc',
    'size': 100
}
lock = threading.Lock()
thread_s = []
for text in text_request:

    thrd = threading.Thread(target=request_url, args=(url_add, params, text, lock))
    thread_s.append(thrd)
    thrd.start()

for thread in thread_s:
    thread.join()

