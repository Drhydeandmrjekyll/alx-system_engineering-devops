#!/usr/bin/python3
"""Querying Reddit"""

import requests


def number_of_subscribers(subreddit):
    """Query subreddit and retrieve number of subscribers"""

    # Reddit API endpoint for the getting subreddit information
    url = "https://www.reddit.com/r/{subreddit}/about.json"

    # Set custom User-Agent to avoid many requests error
    headers = {'User-Agent': 'My User Agent 1.0'}

    # Send GET request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if request was successful and not redirect
    if response.status_code == 200:
        # Parse JSON response to extract number of subscribers
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
