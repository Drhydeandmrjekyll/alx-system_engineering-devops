#!/usr/bin/python3
"""Query Reddit for top ten posts"""

import requests


def top_ten(subreddit):
    """
    Function to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.
    """

    # Reddit API endpoint for getting top posts
    url = "https://www.reddit.com/r/{subreddit}/hot.json"

    # Set custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'My User Agent 1.0'}

    try:
        # Send GET request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])

            # Print titles of first 10 hot posts
            for child in data[:10]:
                post_data = child.get('data', {})
                print(post_data.get('title'))
        else:
            print("None")
    except requests.RequestException as e:
        print("None")


if __name__ == "__main__":
    subreddit = input("Enter the subreddit: ")
    top_ten(subreddit)
