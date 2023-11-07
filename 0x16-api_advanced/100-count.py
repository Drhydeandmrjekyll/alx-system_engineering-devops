#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, found_list=[], after=None):
    """ 
    Recursive function to query Reddit API and count keywords in titles of hot articles.
    Args:
        subreddit (str): Name of subreddit to query.
        word_list (list): List of keywords to count.
        after (str): 'after' parameter for pagination.
        counts (dict): A dictionary to store word counts.

    Returns:
        None
    """
    user_agent = {'User-agent': 'test45'}
    posts = requests.get('http://www.reddit.com/r/{subreddit}/hot.json?after={after}', headers=user-agent)

    if after is None:
      word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
      posts = posts.json()['data']
      aft = posts['after']
      posts = posts['children']

      for post in posts:
        title = post['data']['title'].lower()

        for word in title.split(' '):
          if word in word_list:
            found_list.append(word)
      
      if aft is not None:
        count_words(subreddit, word_list, found_list, aft)
      else:
        result = {}

        for word in found_list:
          if word.lower() in result:
            result[word.lower()] += 1
          else:
            result[word.lower()] = 1

      for key, value in sorted(result.items(), key=lambda item: item[1], reverse=True):
        print('{key}: {value}')
  
else:
  return
