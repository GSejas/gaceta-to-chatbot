import tweepy
from datetime import datetime

# Set up Tweepy API credentials
consumer_key = "INSERT_CONSUMER_KEY_HERE"
consumer_secret = "INSERT_CONSUMER_SECRET_HERE"
access_token = "INSERT_ACCESS_TOKEN_HERE"
access_token_secret = "INSERT_ACCESS_TOKEN_SECRET_HERE"

# Authenticate with Tweepy API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Create function to post tweets
def post_tweet(text):
    api.update_status(text)
    print("Tweet posted successfully.")

# Create function to get latest gazette
def get_latest_gazette():
    # TODO: Write code to scrape latest gazette from website
    return "INSERT_LATEST_GAZETTE_TEXT_HERE"