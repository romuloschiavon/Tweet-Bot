#==================================================================
# Import statements
#==================================================================

from datetime import datetime, timedelta, timezone
import tweepy
from dateutil.parser import parse
import json
import apikeys as apiKeys

#==================================================================
# API Credentials
#==================================================================
ConsumerKey = apiKeys.CONSUMER_KEY
ConsumerSecret = apiKeys.CONSUMER_SECRET
AccessTokenKey = apiKeys.ACCESS_TOKEN_KEY
AccessTokenSecret = apiKeys.ACCESS_TOKEN_SECRET

#==================================================================
# API Initialize
#==================================================================

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessTokenKey, AccessTokenSecret)
api = tweepy.API(auth)

#==================================================================
# Reading Tweets as JSON
#==================================================================
myTweets = None
with open('./tweets.json', encoding="utf8") as jsonTweets:
    myTweets = json.load(jsonTweets)

#==================================================================
# Delete Tweets Function
#==================================================================

def deleteTweets(id):
    try:
        api.destroy_status(id)
        print("Deleted")
    except Exception as err:
        print("Deu bigode doidao")
        print("Exception %s\n" % err)
    pass

#==================================================================
# Defining range of tweets
#==================================================================

endRange = datetime.now(timezone.utc) - timedelta(days = 365)

#==================================================================
# Defining tweets to delete/ignore
#==================================================================

toDelete = []
toIgnore = []

#==================================================================
# Iteration
#==================================================================

for tweet in myTweets["data"]:
    tweetPostTime = datetime.strptime(tweet["tweet"]["created_at"], '%a %b %d %H:%M:%S %z %Y')
    if(tweetPostTime <= endRange):
        toDelete.append(tweet["tweet"]["id_str"])
    else:
        toIgnore.append(tweet["tweet"]["id_str"])

for id in toDelete:
    deleteTweets(id)

print(f"The number of ignored tweets was: {str(len(toIgnore))}\n" + f"The number of deleted tweets was: {str(len(toDelete))}")