#!/usr/bin/python
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from sys import stdout
import json
import unicodedata
import time

#consumer key, consumer secret, access token, access secret.
ckey="Enter consumer key"
csecret="Enter consumer secret key"
atoken="Enter access token"
asecret="Enter access secret token"

class listener(StreamListener):

    def on_data(self, data):
    	tweet = data.encode('utf-8')
        tweet_data = json.loads(tweet)
        print '===============New Tweet==================='
        print json.dumps(tweet_data["text"], indent=1)
        stdout.flush()
        return True

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            print(status_code)
            return False
while True:
	try:
		auth = OAuthHandler(ckey, csecret)
		auth.set_access_token(atoken, asecret)

		twitterStream = Stream(auth, listener())
		twitterStream.filter(track=["story"])
	except UnicodeEncodeError:
		pass