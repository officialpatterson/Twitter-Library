'''
    Author: Andrew R. Patterson
    Date:   14th June 2014
    Title:  setting up mongoDB with the Twitter stream
    Alt:    if connection to MongoDB instance cannot be established do *NOT* connect
            to Twitter stream.
'''
import sys
from Twitter4AP import TwitterStream
from pymongo import errors
from pymongo import MongoClient

class MyStream(TwitterStream):
    i = 0
    def dbSetup(self):
        try:
            tweets = MongoClient().Twitter.tweets
        except errors.ConnectionFailure, e:
            print '\033[91mCould not establish connection to MongoDB instance.\033[0m'
            sys.exit()
        print '\033[95mConnected to MongoDB instance and Twitter API \033[0m'
            
    def onSuccess(self, tweet):
        sys.stdout.write('\r\t\033[94mTweets Added: %i\033[0m ' % self.i)
        sys.stdout.flush()
        self.i = self.i+1

    
    def onError(self, msg, code):
        print '\033[91m' + msg + '\033[0m'
        print '\033[91m' + code + '\033[0m'

s = MyStream()
s.dbSetup()
s.start()