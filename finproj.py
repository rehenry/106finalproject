import requests
import json
import tweepy
import test106 as test 

print "Welcome to Weather++"
print "---~~~~~*~~~~~---"

access_token_w = "179c91fab5b8fda30219fd4dc14f491b"
if access_token_w == None: 
	access_token_w = raw_input("Enter weather API key: ")

baseurl_w= "http://api.openweathermap.org/data/2.5/weather"
api_key = access_token_w
url_params = {}
url_params['APPID'] = access_token_w
url_params['q'] = raw_input("Enter a city name: ")

weather_data = requests.get(baseurl_w, params=url_params)
w_d = json.loads(weather_data.text)

print "\n"
print w_d['name'] + ", " + w_d['sys']['country']
temp = w_d['main']['temp']*1.8-459.67
print "%.1f"%temp + " F"

r = w_d['weather']
q = [value['description'].encode('utf-8') for value in r]
for value in q: 
	print value + "\n"

lat = (w_d['coord']['lat'])
lon = (w_d['coord']['lon'])

consumer_key = "pHFgoAklGYm2SjdCiTubD7JoB"
consumer_secret = "DHzeTst7gL9hEwUFBzlchlPt5JtKOgBujOFQCHksSlVWOhodm4"
access_token = "2205286339-S9N1nHkhEms90889VtcB2SXtuakRtdbXyx82bF1"
access_token_secret = "nF2Vcka6Kad5pbQDYnxHXWaoIa0sm5pvHOk35girQNjPq"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

req = api.search(q="weather", lang="en", geocode="{},{},5mi".format(lat, lon), count=5)

tweet_list = [tweet.text for tweet in req]
name_list = [tweet.user.screen_name for tweet in req]
rt_list = [tweet.retweet_count for tweet in req]

x = list(reversed(tweet_list))
y = list(reversed(name_list))
z = sorted(rt_list, reverse = True)

cache_fname = "twitterdata.txt"

f = open(cache_fname, 'w')
f.write(str(req))
f.close()

class Tweet_Info():
	def __init__(self, messages, handles, retweets):
		self.messages = messages
		self.handles = handles
		self.retweets = retweets

	def display_tweet(self):
		return "Tweet: " + self.messages

	def display_handle(self):
		return "Author: " + self.handles

	def display_retweets(self):
		return "Retweets: " + str(self.retweets)

	def __str__(self):
		return "{}\n {}\n {}\n".format(self.display_tweet().encode('utf-8'),
		 self.display_handle().encode('utf-8'), 
		 self.display_retweets().encode('utf-8'))

tweet = Tweet_Info(messages= "hello", handles= "adele", retweets= 100)
test.testEqual(tweet.display_tweet(), "Tweet: " + "hello")
test.testEqual(tweet.display_handle(), "Author: " + "adele")
test.testEqual(tweet.display_retweets(), "Retweets: " + str(100))
print "\n"

accum = 0
list_of_tweets = []
for item in x:
	list_of_tweets.append(Tweet_Info(item, y[accum], z[accum]))
	accum += 1

for tweet in list_of_tweets:
	print tweet.__str__()

print "Would you like to post a status to Twitter? YES or NO"
answ = raw_input()
if answ == "yes":
	r = api.update_status(raw_input("Add to the conversation by tweeting your own weather experience! Type in your message and hit enter to post. >>>>>> "))
elif answ == "no": 
	None
