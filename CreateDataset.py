import os
import csv
import tweepy    
from tweepy import OAuthHandler
import json
import re
import sys
from textblob import TextBlob

#provide your access details below 
consumer_key = " oUeZDCFbDdzFVXDXw2VslypPI"
consumer_secret = "0VeYgCwdLjYmpGIKUhkk7YYGpvTgavpMNkIij5duha6hFDm6di"
access_token = "1218782784-xNhKXZbj7qzlgUqX1qA8VwN6pBAcXQLRAZwsoyd"
access_token_secret = " 0VeYgCwdLjYmpGIKUhkk7YYGpvTgavpMNkIij5duha6hFDm6di"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)    
    
from tweepy import Stream
from tweepy.streaming import StreamListener


i=0
class MyListener(StreamListener):
    def on_data(self, data):
        global i
        try:
            with open('twitter.json', 'a') as f: 
            	i=i+1
            	print(i)
            	f.write(data)
            	if i>200:
            		sys.exit(1)
            		return False
            	else:
            		return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return False
 
    def on_error(self, status):
        print(status)
        return False

def clean_tweet(tweet):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def sentiment(tweet):
        analysis = TextBlob(tweet)
       
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'positive'
        else:
            return 'negative'   


def process():
	twitter_stream = Stream(auth, MyListener())
	#change the keyword here
	twitter_stream.filter(track=['#covid19'])
	
	with open('twitter.json') as in_file, open('data.csv', 'w',newline='') as out_file:
		writer = csv.writer(out_file, delimiter=',')
		writer.writerow(["text","Sentiment","label"])
		for line in in_file:
			if line.strip() == "" :
				continue
			else:
				tweet = json.loads(line)
				tweet['text']=clean_tweet(tweet['text'])
				dd=sentiment(tweet['text'])
				print(tweet['text'])
				d=-1
				if dd == "positive":
					d=1
				else:
					d=0
				row = (tweet['text'],dd,d)
				writer.writerow(row)
	out_file.close()

		

    
