#!/usr/bin/python
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from sys import stdout
import json
import unicodedata

# consumer key, consumer secret, access token, access secret to retreive twitter API
ckey="Enter consumer key"
csecret="Enter consumer secret key"
atoken="Enter access token"
asecret="Enter access secret token"

class listener(StreamListener):

    # Receive data from StreamListener
    def on_data(self, data):
        # Encode data with utf-8 format
    	tweet = data.encode('utf-8')
        # Load data in json style
        tweet_data = json.loads(tweet)
        # Message to separate each streaming tweet
        print '===============New Tweet==================='
        # Print out each data's "text" section, which is the tweet content
        print json.dumps(tweet_data["text"], indent=1)
        stdout.flush()
        return True

    # Handle error
    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            print(status_code)
            return False

# Continuously polling data
while True:
	try:
        # Verify key, secret key, token and secret token
		auth = OAuthHandler(ckey, csecret)
		auth.set_access_token(atoken, asecret)

        # Get twitter stream
		twitterStream = Stream(auth, listener())
        # Filter data with keyword "story"
		twitterStream.filter(track=["story"])
    # Throw UnicodeEncodeError exception
	except UnicodeEncodeError:
		pass