import sys
import json


def create_sentiment_dictionary(sent_file):
    """
    Turns sentiment text file into dictionary
    returns dictionary
    """
    scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    return scores


def parse_tweets(twit_file):
    """
    extracts info from file of tweets into a list
    returns a list with one dictionary per tweet
    """
    tweets = []
    for line in twit_file:
        try:
            tweets.append(json.loads(line))
        except:
            pass
    return tweets


def calculate_sentiment(word_list, sent_dict):
    """
    takes as input a list of words and a word sentiment dictionary
    Calculates the sentiment of a word list based on dictionary
    returns integer value of sentiment sum
    """
    tweet_sentiment = 0
    for word in word_list:
            if word.lower() in sent_dict:
                tweet_sentiment += sent_dict[word.lower()]
    return tweet_sentiment


def update_new_sentiments(tweet, sent_dict, new_dict):
    """
    Takes a tweet and calculates overall sentiment
    Updates new_dict with average sentiment value for words not in
    provided default sentiment dictionary
    new_dict has structure word: [count, total_sentiment]
    """
    words_in_orig_dict = 0
    new_words = set([])
    tweet_words = tweet['text'].split()
    tweet_sentiment = calculate_sentiment(tweet_words, sent_dict)
    if tweet_sentiment == 0:
        return
    for word in tweet_words:
        word = word.lower()
        if word in sent_dict:
            words_in_orig_dict += 1
        else:
            new_words.add(word)
    avg_sentiment = float(tweet_sentiment / words_in_orig_dict)
    for word in new_words:
        if word in new_dict:
            new_dict[word][0] += 1
            new_dict[word][1] += avg_sentiment
        else:
            new_dict[word] = [1, avg_sentiment]


def decide_to_process(tweet):
    """
    helper function to decide if we should process a tweet.
    Must be coded as English and have text
    returns Boolean
    """
    if 'lang' in tweet and tweet['lang'] == 'en':
        if 'text' in tweet:
            return True
    return False


def process_all_tweets(twit_list, sent_dict):
    """
    Main routine to process all tweets
    takes list of tweets and sentiment dictionary
    returns dictionary of new words with sentiment value
    """
    new_word_sentiments = {}
    for tweet in twit_list:
        if decide_to_process(tweet):
            update_new_sentiments(tweet, sent_dict, new_word_sentiments)
    return new_word_sentiments


def main():
    """
    Main executable to meet question requirements
    """
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = create_sentiment_dictionary(sent_file)
    tweet_list = parse_tweets(tweet_file)
    new_dict = process_all_tweets(tweet_list, sent_dict)
    for word in new_dict:
        print(str(word.encode('utf-8')) + ' ' + \
              str(float(new_dict[word][1] / new_dict[word][0])))


if __name__ == '__main__':
    main()
