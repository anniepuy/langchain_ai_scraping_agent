"""
Title: Twitter Scraper.py
Purpose: Scrapes users tweets NOT using third party API but saved GitGIST. Set up to use Twitter API if needed.
Author: Ann Hagan from Eden Marco's Udemy Course
Date: 2025--02-22
"""

import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()

#only needed if using Twitter API
#twitter_client = tweepy.Client(
 #   bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
 #   consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
 #   consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
 #   access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
#    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
#)

def scrap_user_tweets(username, num_tweets=5, mock: bool = True):
    """
    Scrapes a MOCK Twitter tweets from GitHub GIST and returns them as a list of dictionaries. Could be used with Twitter API. Each dictionary has three fields: "time_posted", "text", and "url". 
    """
    tweet_list = []
    if mock:
        EDEN_TWITTER_GIST ="https://gist.githubusercontent.com/emarco177/9d4fdd52dc432c72937c6e383dd1c7cc/raw/1675c4b1595ec0ddd8208544a4f915769465ed6a/eden-marco-tweets.json"
        tweets = requests.get(EDEN_TWITTER_GIST, timeout=10).json()
        #iterating through tweets and pulling out the text and url
        for tweet in tweets:
            tweet_dict = {}
            tweet_dict["text"] = tweet["text"]
            tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
            tweet_list.append(tweet_dict)

    else:
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_user_tweets(id=user_id, max_results=num_tweets, exclude=["rewteets", "replies"])

        for tweet in tweets.data:
            tweet_dict = {}
            tweet_dict["text"] = tweet["text"]
            tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
            tweet_list.append(tweet_dict)

    return tweet_list



## Test the function
if __name__ == "__main__":
    tweets = scrap_user_tweets(username="EdenEmarco177", mock=True)
    print(tweets)