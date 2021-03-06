__author__ = 'csiwale'

import sys
import json
import io
import re

def find_popular_tweets(twitter_api, statuses, retweet_threshold=3):
    # You could also consider using the favorite_count parameter as part of
    # this heuristic, possibly using it to provide an additional boost to
    # popular tweets in a ranked formulation
    return [ status for status in statuses if status['retweet_count'] > retweet_threshold ]

def load_json(filename):
    with io.open('{0}.json'.format(filename), encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    tweets = open(sys.argv[1])
    x = 1
    #evaluate tweets
    for line in tweets:
        try:
            line = line.decode('ascii')
            #print line
            tweet = json.loads(line)
            x += 1

        except Exception as e:
            #print(tweet["text"])
            print (e, x)
            x += 1



