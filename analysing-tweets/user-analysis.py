#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
from textblob import TextBlob

#Twitter API credentials
consumer_key = "qOnfdMIOKju3dTi78pi3B2iGb"
consumer_secret = "tnsNac26XPvO6YLJY1qaddiOSIJx7EteAztjzdCbMA9Pxe8PVH"
access_key = "949971570948100097-DSQg6ySE1pKZljDGa30eaIGI2wbH9Qw"
access_secret = "DIhfH3l0Sax8uuxa8MhlZPke1Qxc6r2eT7YWvvEU6jw72"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=100)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
#	#keep grabbing tweets until there are no tweets left to grab
#	while len(new_tweets) > 0:
#		print "getting tweets before %s" % (oldest)
#		
#		#all subsiquent requests use the max_id param to prevent duplicates
#		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
#		
#		#save most recent tweets
#		alltweets.extend(new_tweets)
#		
#		#update the id of the oldest tweet less one
#		oldest = alltweets[-1].id - 1
#		
	print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, len(tweet.text), len(tweet.entities.get('hashtags')), len(tweet.entities.get('user_mentions')), tweet.favorite_count, tweet.retweet_count, TextBlob(tweet.text).sentiment.polarity,tweet.created_at.time().hour] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","length","hashtag_count","mention_count","likes_count","retweet-count","sentiment","created_at"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("SrBachchan")
