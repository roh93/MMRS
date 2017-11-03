import requests
import oauth2 as oauth
import json

userProfile_url = 'https://api.twitter.com/1.1/users/show.json?user_id=2597834149'
userTweets_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=2597834149&count=20'

with open('Credentials.txt', 'r') as cred:
    credentials = cred.readlines()

CONSUMER_KEY = credentials[0].strip()
CONSUMER_SECRET = credentials[1].strip()
ACCESS_KEY = credentials[2].strip()
ACCESS_SECRET = credentials[3].strip()

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

#Get User Profile Details
'''response_code, response_content = client.request(userProfile_url)
userProfileInfo = {}
if response_code['status'] == str(200):
    userProfileInfo = json.loads(response_content)
print(userProfileInfo['status']['text'])'''

#Get User Tweets
response_code, response_content = client.request(userTweets_url)
userTweetsInfo = {}

userProfileInfo = json.loads(response_content)
for a in userProfileInfo:
    print(a['text'])

