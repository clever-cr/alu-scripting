#!/usr/bin/python3
""" count """

import requests
import re


def count_words(subreddit, word_list, count_dict=None):
    if count_dict is None:
        count_dict = {}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    titles = [post['data']['title'] for post in data['data']['children']]
    for title in titles:
        title = re.sub(r'[^\w\s]', '', title.lower())
        for word in word_list:
            if word in count_dict:
                continue
            count = title.count(word.lower())
            if count == 0:
                continue
            count_dict[word] = count_dict.get(word, 0) + count
    if len(count_dict) == len(word_list):
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print('{}: {}'.format(word.lower(), count))
        return
    count_words(subreddit, word_list, count_dict)
