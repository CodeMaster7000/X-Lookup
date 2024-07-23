import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_input = input("Enter user IDs (separated by commas): ")
user_ids = [int(uid.strip()) for uid in user_input.split(",")]
users = api.lookup_users(user_ids)

for user in users:
    print("ID: " + str(user.id))
    print("Screen Name: " + user.screen_name, end="\n\n")
