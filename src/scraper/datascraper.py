import requests
import oauth2 as oauth
import json

userProfile_url = 'https://api.twitter.com/1.1/users/show.json?user_id=2597834149'
userTweets_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=2597834149&count=20'

with open('Credentials.txt', 'r') as cred:
    credentials = cred.readlines()

CONSUMER_KEY = 'ki2injLpdVL2eqV3ZL79gcQo7'#credentials[0].strip()
CONSUMER_SECRET = 'PKvpnkAr2oaHTKzL6Q2IKKbLhHvXSUiNgUdOJmY5AnKJZM9Qi9'#credentials[1].strip()
ACCESS_KEY = '2597834149-P9kSt49DG0yNMEngqw6dnYb8C5T6znqQkpuDF1f'#credentials[2].strip()
ACCESS_SECRET = 'FOoMWzMWJUzEfFGhj8ltGGvY0EPHEOZTwtoDMxltXFTKE'#credentials[3].strip()

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

