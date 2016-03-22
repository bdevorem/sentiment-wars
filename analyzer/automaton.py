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
POSITIVE = set(['exciting', 'entertaining', 'good', 'love', 'loved', 'great', 'awesome', 'best', 'adventure', 'perfect', ':)'])
NEGATIVE = set(['fine', 'disappointed', 'bad', 'worse', 'garbage', 'worst', 'mad', 'suck', 'sucked'])
CHANGE = set(['personally', 'theoretically'])

def is_negative(word):
	if word in NEGATIVE:
		return True
	else:
		return False

def is_positive(word):
	if word in POSITIVE:
		return True
	else:
		return False

def is_change(word):
	if word in CHANGE:
		return True
	else:
		return False


def start_state(word):
	"""
	s* in graph
	every string starts here
	if input word is positive, move to accept_1
	if input word is negative, move to reject_1
	else, stay here (if string ends here -> reject)
	"""
	#if tweet_input == -1:
	#	END = True
	#word = tweet_input[0]
	
	#if len(tweet_input) > 1:
	#	tweet_input = tweet_input[1:]
	#else
	#	tweet_input = -1

	if is_positive(word):
		return accept_1
	elif is_negative(word):
		return reject_1
	else:
		return start_state

def accept_1(word):
	"""
	a1 in graph
	if input word is a change word, move to accept_2
	if input word is negative, move to reject_1
	else, stay
	"""
	if is_change(word):
		return accept_2
	elif is_negative(word):
		return reject_1
	else:
		return accept_1


def reject_1(word):
	"""
	r1 in graph
	if input word is a change word, move to accept_2
    if input word is positive, move to reject_1
    else, stay

	"""
	if is_positive(word):
		return reject_1
	elif is_change(word):
		return accept_2
	else:
		return reject_1



def accept_2(word):
	"""
	a2 in graph
	if input word is positive, move to accept_1
    if input word is negative, move to reject_1
    else, stay

	"""
	if is_positive(word):
		return accept_1
	elif is_negative(word):
		return reject_1
	else:
		return accept_2


def analyze(tweet):
	#order of elements in python is persistent

	tweet_input = tweet.split(" ")	

	function = start_state(tweet_input[0])
	for word in tweet_input[1:]:
		function = function(word)	
		#print(word)
	
	#return function
	# check for ending state
	if function is accept_1:
		return "Positive"
	elif function is accept_2:
		return "Positive"
	else:
		return "Negative or Inconclusive"



