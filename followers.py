import re
import json
import tweepy
import config
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    '''
    Generic Twitter Class for gathering followers.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = config.consumer_key
        consumer_secret = config.consumer_secret
        access_token = config.access_token
        access_token_secret = config.access_token_secret

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except: 
            print("Error: Authentication Failed")
    
    def get_followers(self, screen_name):
        ''' 
        Main function to fetch followers and parse them.
        '''
        # empty list to store parsed followers
        followers = []

        try:
            # call twitter api to fetch followers
            fetched_followers = []
            
            for item in tweepy.Cursor(self.api.followers, id = screen_name).items():
                fetched_followers.append(item)
            
            for follower in fetched_followers:
                parsed_follower = {}
                parsed_follower['screen_name'] = follower.screen_name
                parsed_follower['id'] = follower.id
                parsed_follower['name'] = follower.name
                followers.append(parsed_follower)

            return followers

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

    def get_total_followers(self, screen_name):
        user = self.api.get_user(screen_name = screen_name)
        total = user.followers_count
        return total

    def clean_text(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def main():
    api = TwitterClient()
    screen_name = "_calcast"
    total_followers = api.get_total_followers(screen_name)

    user = {}
    user['screen_name'] = screen_name
    user['total_followers'] = total_followers
    user['followers'] = api.get_followers(screen_name)


    with open("followers.json", "w") as outfile:
        json.dump(user, outfile, indent=4)


if __name__ == "__main__":
    # calling main function
    main()