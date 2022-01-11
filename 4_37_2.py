import json
import asyncio
import aiohttp
from pprint import pprint


async def request_url(url_, params_, text_):
    async with aiohttp.ClientSession() as session_:
        async with session_.get(url_+f'?q={text_}', params=params_) as resp:
            data = await resp.json()
            data_dict = data['data']
            comment = {text_: [com.get('body') for com in data_dict]}

    try:
        with open('comment_text_aio.json', 'r') as file:
            data_ = json.load(file)

    except:
        data_ = dict()

    data_.update(comment)
    with open('comment_text_aio.json', 'w') as file:
        json.dump(data_, file, indent=4)


async def get_task():
    url_add = 'https://api.pushshift.io/reddit/search/comment/'

    text_request = ['robot', 'nanotechnology', 'neural network']
    params = {
        'subreddit': 'technology',
        'sort_type': 'created_utc',
        'size': 100
    }

    await asyncio.gather(*[request_url(url_add, params, text_r) for text_r in text_request])


asyncio.run(get_task())
