#!/usr/bin/python3
""" return top ten"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if not response.ok:
        print(None)
        return
    json_data = response.json()
    posts = json_data['data']['children']
    for i in range(min(10, len(posts))):
        print(posts[i]['data']['title'])
