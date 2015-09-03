import tweepy
#import Secrets



class authorize_twitter:

    def __init__(self, auth_key):
        print("setting up authorization")
        self.auth_status = False   
        self.auth_key = auth_key
        self.set_auth()
        self.set_api()

    def set_auth(self):                 
        auth = tweepy.OAuthHandler( self.auth_key.consumer_key, self.auth_key.consumer_secret )
        auth.set_access_token(self.auth_key.access_token, self.auth_key.access_token_secret)
        self.auth = auth
        self.auth_status = True;

    def set_api(self):
        self.api = tweepy.API(self.auth)        

    def __str__(self):
        public_tweets = self.api.home_timeline()
        tweets = "tweets : "
        for tweet in public_tweets:
            tweets += "\n\n" + tweet.text
        return tweets
         


#auth_plz = authorize_twitter(Secrets.Oauth_key)
#if (auth_plz.auth_status):
#    print("auth is OK")
#    print(auth_plz)

