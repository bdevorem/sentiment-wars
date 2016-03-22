#!/usr/bin/python
# main.py
# connects API query with automaton
# author:Breanna Devore-McDonald
# Mar 21 2016

import tweepy
from tweepy import OAuthHandler
import json
import time
from keys import keys
from functions import *
from automaton import analyze

SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

if __name__ == '__main__':

	tweets = search_tweets(api)

	for tweet in tweets:
		print ("Tweet: \n" + tweet)
		# run tweet through automaton
		result = analyze(tweet)
		print (result)

	#result = analyze("I love Star Wars, this should be positive")	
	#print (result)
	#result = analyze("I was disappointed by Star Wars, should be negative.")
	#print (result)





