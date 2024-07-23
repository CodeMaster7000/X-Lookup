import tweepy

consumer_key = "" 
consumer_secret = "" 
access_token = "" 
access_token_secret = "" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)
id_input = input("Enter user IDs (separated by commas): ")
id_ = [int(id.strip()) for id in id_input.split(',')]

statuses = api.statuses_lookup(id_)

for status in statuses: 
    print("The status" + str(status.id) + "was posted by " + status.user.screen_name) 
    print("Status: \n\n" + status.text, end="\n\n")
