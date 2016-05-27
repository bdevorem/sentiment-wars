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

	
	print("Welcome to Sentiment Wars!")
	print("--------------------------")
	print("Web interface at:\nhttp://sentiment-wars.herokuapp.com/")
	
	while True:
		print("--------------------------")
		print("Would you like to use Twitter-queried tweets or enter your own input? ")
		choice = input("'y' for Twitter, 'n' for your own: ")

		if choice == 'y':
			with open('tweets.txt','r') as f:
				for tweet in f:			
					print ("Tweet:" + tweet)
					# run tweet through automaton
					result = analyze(tweet)
					print ("Result: " + result+ "\n")
					print("--------------------------")
	
		else:
			print("--------------------------")
			tweet = input("Think of something good and submit by pressing Enter!\n")

			result = analyze(tweet.replace(',', '').replace('.',''))
			print ("Sentiment: " + result)

		print("--------------------------")
		keep = input("Quit? y/n ")
		if keep == "y":
			break
	

	#result = analyze("I love Star Wars, this should be positive")	
	#print (result)
	#result = analyze("I was disappointed by Star Wars, should be negative.")
	#print (result)





