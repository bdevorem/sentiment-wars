#!/usr/bin/python
# functions.py
# functions that interact directly with Tweepy API
# author: Breanna Devore-McDonald
# Mar 21 2016
from keys import keys
import tweepy

SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

def unfollow_friends(api):
    """
    test function to unfollow everyone I follow, learn Twitter API
    """
    for f in api.friends_ids(SCREEN_NAME):
        if f not in api.followers_ids(SCREEN_NAME):
            a = input('Unfollow %s?' + api.get_user(f).screen_name)
            if a.rstrip()  == "y":
                #print ("\""+a+"\"")
                api.destroy_friendship(f)

def read_timeline(api):
    """
    test function to read tweets from project's own timeline,
    learn Twitter API
    """
    for status in tweepy.Cursor(api.home_timeline).items(10):
        # Process a single status
        print(status.text)

def update_stat(api):
    """
    test function to update status, learn Twitter API
    """
    api.update_status('testing')

def search_tweets(api):
	"""
	get relevant tweets
	"""
	rel_tweets = []
	for tweet in tweepy.Cursor(api.search,
				#q="the%20force%20awakens%20since%3A2015-12-16%20until%3A2015-12-25&src=typd",
				#q="the force awakens",
				#since="2015-12-16",
				#until="2016-01-20",
				q="saw OR opinion force awakens -Last -last -http -? -haven't -Marvel -trek -Curious -https -waiting",
				exclude_replies=True,
				lang="en").items(20):
		if "RT" not in tweet.text:
			#print (tweet.text)
			rel_tweets.append(tweet.text.replace(',', '').replace('.', '').lower())

	return rel_tweets
