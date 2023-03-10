#!/usr/bin/python3
"""recursive function"""

import requests


def recurse(subreddit, hot_list=[], after=None):

    if after is not None:
        url = "https://www.reddit.com\
/r/{}/hot.json?after={}".format(subreddit, after)
    elif after is None and len(hot_list) == 0:
        url = "https://www.reddit\
.com/r/{}/hot.json".format(subreddit)
    else:
        return hot_list
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if not response.ok:
        return None
    json_data = response.json()
    length = len(hot_list)
    data = [i["data"]["title"] for i in json_data["data"]["children"]]
    hot_list.extend(data)
    if after is not None or length == 0:
        return recurse(subreddit, hot_list, json_data["data"]["after"])
    else:
        return hot_list
