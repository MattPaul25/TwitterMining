import tweepy
#import Secrets



class TweetHandler:

    def __init__(self, auth_key):
        print("setting up authorization")
        self.is_authorized = False   
        self.auth_key = auth_key
        self.set_auth()
        self.set_api()

    def set_auth(self): 
        """authorizes application"""                
        auth = tweepy.OAuthHandler( self.auth_key.consumer_key, self.auth_key.consumer_secret )
        auth.set_access_token(self.auth_key.access_token, self.auth_key.access_token_secret)
        self.auth = auth

    def set_api(self):
        self.api = tweepy.API(self.auth)
        self.is_authorized = True;      
        
    def get_search_results(self, searchable):
        status_results = self.auth_plz.api.search(searchable)
        return status_results

    def post_tweet(self, tweet):
        """posts a tweet to the twitter account"""

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

