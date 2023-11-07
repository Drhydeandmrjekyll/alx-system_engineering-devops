#!/usr/bin/python3
"""
2-recurse
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to query the Reddit API and return a list of titles of all hot articles.
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The 'after' parameter for pagination.

    Returns:
        list: A list containing the titles of all hot articles.
    """
    url = 'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {'User-Agent': 'MyBot/1.0'}  # Set a custom User-Agent to avoid Too Many Requests error.
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return hot_list
        else:
            hot_list.extend([post['data']['title'] for post in posts])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
    else:
        return None

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        hot_titles = recurse(subreddit)
        if hot_titles is not None:
            print(len(hot_titles))
        else:
            print("None")
