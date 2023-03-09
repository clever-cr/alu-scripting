#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if not response.ok:
        return 0
    json_data = response.json()
    return json_data['data']['subscribers']