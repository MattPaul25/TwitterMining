#class tells whether a tweet is either positive or negative
from DatabaseHandler import DatabaseReader
from DatabaseHandler import DatabaseWriter


class WordList():
    """single object that contains a list of words and their ratings"""
    def __init__(self):
        db = DatabaseReader('some request')
        self._words = db.extract_data()
        self.word_list = []

    def push_tweets(self):
       db_push = DatabaseWriter(self.tweet_list)
       db_push.push_data()


class SentimentEngine(WordList):
    """handles a phrase returns whether the phrase is good or bad"""

    def __init__(self, search_term):
        super(SentimentEngine, self).__init__()
        self.search_term = search_term
        #gets wordlist after instantiated

    def getRating(self, tweet):
        rating = assign_sentiment(tweet)
        save_tweet(tweet)
       ###add some method here to assign overall sentiment

    def assign_sentiment(self, tweet):   
        """looks up a word or phrase for positive sentiment"""
        returnVal = 0    
        for word in self._words:
            if word[0] in tweet:
                returnVal += word[1]
                self.word_list.append([self.search_term, word[0], word[1]])
        return returnVal

    def save_tweet(self, tweet):
       self.tweet_list.add(tweet) 

    

class UpdateWordList(WordList):
     """updates the word list based off the tweets"""
