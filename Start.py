from TwitterCrawler import authorize_twitter 
from Secrets import authorization_key
import Secrets

class Starter:
    def __init__ (self):
        print("getting twitter oAuth")
        self.auth_plz = authorize_twitter(Secrets.Oauth_key)
        print(self.auth_plz)
        self.get_search_results()

    def get_search_results(self):
        status_results = self.auth_plz.api.search("BMW")
        for status in status_results:
            print (status.user.screen_name + ":" + status.text, end = "\n\n")
  

def Main():
    print("starting")
    Start = Starter()


Main()