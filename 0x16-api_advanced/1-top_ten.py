#!/usr/bin/python3
"""
1-top_ten
"""

import requests

def top_ten(subreddit):
    """
    Function to query Reddit API and print the titles of first 10 hot posts for a given subreddit.
    Args:
        subreddit (str): Name of subreddit to query.

    Returns:
        None
    """
    url = 'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'MyBot/1.0'}  # Set a custom User-Agent to avoid Too Many Requests error.

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                print(post['data']['title'])
        else:
            print("No posts found in the subreddit.")
    else:
        print("Not a valid subreddit or an issue with the Reddit API.")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
