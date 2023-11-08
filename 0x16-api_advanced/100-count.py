#!/usr/bin/python3
"""
100-count
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursive function to query Reddit API and count keywords in titles of hot articles.
    Args:
        subreddit (str): Name of subreddit to query.
        word_list (list): List of keywords to count.
        after (str): 'after' parameter for pagination.
        counts (dict): Dictionary to store word counts.

    Returns:
        None
    """
    if counts is None:
        counts = {}

    if not word_list:
        return print_results(counts)

    keyword = word_list.pop()
    url = 'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {'User-Agent': 'MyBot/1.0'}  # Set custom User-Agent to avoid Too Many Requests error.
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title'].lower()
        keyword = keyword.lower()
        if keyword in title and not title.startswith(keyword + '.'):
            counts[keyword] = counts.get(keyword, 0) + 1

    after = data['data']['after']

    if after:
        return count_words(subreddit, word_list, after, counts)
    else:
        return print_results(counts)

def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print("{word}: {count}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [x for x in sys.argv[2].split()]
        count_words(subreddit, keywords)
