#!/usr/bin/python3
"""  functions returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if not response.ok:
        return 0
    json_data = response.json()
    return json_data['data']['subscribers']
