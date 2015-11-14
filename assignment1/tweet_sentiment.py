import sys
import json


def lines(fp):
    """
    prints number of lines in input file - default supplied code
    not actually needed
    """
    print str(len(fp.readlines()))


def create_sentiment_dictionary(sent_file):
    """
    Turns sentiment text file into dictionary
    """
    scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    return scores


def parse_tweets(twit_file):
    """
    extracts info from file of tweets into a list
    returns the list of a dictionary per tweet
    """
    tweets = []
    for line in twit_file:
        try:
            tweets.append(json.loads(line))
        except:
            pass
    return tweets


def calculate_tweet_sentiment(tweet, sent_dict):
    """
    takes as input a tweet and a word sentiment dictionary
    Calculates the sentiment of a tweet based on dictionary
    only checks tweets where language is English
    returns integer value of tweet sentiment
    """
    tweet_sentiment = 0
    try:
        tweet_lang = tweet['lang']
    except:
        tweet_lang = 'none'
    #print('tweet_lang = ' + str(tweet_lang))
    if tweet_lang == 'en':
        try:
            tweet_text = tweet['text']
        except:
            tweet_text = ''
        #print('tweet_text = ' + str(tweet_text))
        if tweet_text:
            tweet_words = tweet_text.split()
        for word in tweet_words:
            if word.lower() in sent_dict:
                tweet_sentiment += sent_dict[word.lower()]
    return tweet_sentiment


def main():
    """
    Main routine to calculate sentiment value per tweet
    """
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = create_sentiment_dictionary(sent_file)
    twit_list = parse_tweets(tweet_file)
    for tweet in twit_list:
        print(calculate_tweet_sentiment(tweet, sent_dict))


if __name__ == '__main__':
    main()
