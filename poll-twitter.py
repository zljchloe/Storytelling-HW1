#!/usr/bin/python
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey="MBfH5iDVmiA1DXbY6Gu02plfV"
csecret="kpEpmo6L3JV0AqABqtgWtwFmfyiMbyV4YtjlqHjfLWwFW90jQd"
atoken="1108551973-3UPADg83aqMRjCPgLTvzdzNzxH96pennisRiTJv"
asecret="xeHmJzpVGELKr1Ej2UsNL1L3empOtdzzmte9yia77k47o"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])