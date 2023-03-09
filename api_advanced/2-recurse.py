#!/usr/bin/python3
"""recursive function"""

import requests


def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if not response.ok:
        return None
    json_data = response.json()
    posts = json_data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    if json_data['data']['after'] is not None:
        recurse(subreddit,
                hot_list=hot_list,
                params={'after': json_data['data']['after']})
    return hot_list

