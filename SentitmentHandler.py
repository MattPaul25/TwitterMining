#class tells whether a tweet is either positive or negative
from DatabaseHandler import DatabaseHandler

class WordList():
    """single object that contains a list of words and their ratings"""
    def __init__(self):
        db = DatabaseHandler('some request', True)
        self._words = db.extract_data()


class SentimentEngine(WordList):
    """handles a phrase returns whether the phrase is good or bad"""

    def __init__(self):
        """initializing"""
        #gets wordlist after instantiated

    def getRating(self, tweet):
        rating = _assign_sentiment(tweet)
        post_tweet(tweet)
       ###add some method here to assign overall sentiment

    def _assign_sentiment(self, tweet):   
        """looks up a word or phrase for positive sentiment"""
        returnVal = 0    
        for word in self._words:
            if word[0] in tweet:
                returnVal += word[1]
        return returnVal


class UpdateWordList(WordList):
   """updates the word list based off the tweets"""
    def __init__(self):
        return super().__init__()




    

