#!/usr/bin/python
# author: Breanna Devore-McDonald
# automaton.py
# finite state automaton that performs sentiment analysis
# 	on inputs of tweet form, accepting valid strings
#	if and only if the sentiment is positive (in theory)
# Strings are read left-to-right, 1 word at a time
# Transitions are on words, not characters
#
#
#                         else
#                          v
#                          **
#                         *a1*
#            pos    ->     ** <- pos
#  else       -       pos  ^       -  
#   v     -                -           - 
#   **                     -         change -> **
#  *s**                    -                  *a2* <-else
#   **                     -         change -> **
#         -                -             -
#              -      neg  v          -
#            neg    ->     **      -
#                         *r1* <-  neg
#                          **
#                          ^
#                         else
#
#


def start_state(tweet_input):
	"""
	s* in graph
	every string starts here
	if input word is positive, move to accept_1
	if input word is negative, move to reject_1
	else, stay here (if string ends here -> reject)
	"""
	pass

def accept_1(tweet_input):
	"""
	a1 in graph
	if input word is a change word, move to accept_2
	if input word is negative, move to reject_1
	else, stay
	"""
	pass

def reject_1(tweet_input):
	"""
	r1 in graph
	if input word is a change word, move to accept_2
    if input word is positive, move to reject_1
    else, stay

	"""
	pass

def accept_2(tweet_input)
	"""
	a2 in graph
	if input word is positive, move to accept_1
    if input word is negative, move to reject_1
    else, stay

	"""
	pass

def analyze(tweet):
	#order of elements in python is persistent

	tweet_input = tweet.split(" ")	
	




