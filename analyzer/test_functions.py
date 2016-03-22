#!/usr/bin/python
from keys import keys

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
            print ('Unfollow %s?' + api.get_user(f).screen_name)
            a = input('Y/N?')
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

def get_tweets(api):
	"""
	get tweets w/ 'the force awakens', between 12/15 and 12/25 of
	2015, the release week of Star Wars 7
	"""
	for tweet in tweepy.Cursor(api.search,q='the force awakens',since='2015-12-15',until='2015-12-25').items():
		print (tweet.text)


