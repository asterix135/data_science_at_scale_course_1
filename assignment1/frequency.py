import sys
import json


def parse_tweets(twit_file):
    """
    extracts info from file of tweets into a list
    :param twit_file - open file object
    :return tweets - list of tweet dictionaries:
    """
    tweets = []
    for line in twit_file:
        try:
            tweets.append(json.loads(line))
        except:
            pass
    return tweets


def decide_to_process(tweet):
    """
    helper function to decide if we should process a tweet.
    :param tweet - dictionary representation of tweet
    :return True if english and contains text, else False
    """
    if 'lang' in tweet and tweet['lang'] == 'en':
        if 'text' in tweet:
            return True
    return False


def do_not_process(word):
    """
    Decide to process word based on various content conditions
    :param word:
    :return Boolean:
    """
    word = word.lower()
    if word[0] in ['@', '.'] or word[0:4] == 'http' or word[0:2] == 'rt':
        return True
    return False


def update_frequency_list(tweet, freq_dic, total_words):
    """
    tokenizes text from a tweet and updates word count dictionary as well
    as keeping a running total of words
    :param tweet: tweet as dictionry
    :param freq_dic: word frequency dictionary
    :param total_words:  float
    :return total_words:  float
    """
    tweet_words = tweet['text'].split()
    for word in tweet_words:
        if do_not_process(word):
            continue
        word = word.lower()
        if word in freq_dic:
            freq_dic[word] += 1
            total_words += 1
        else:
            freq_dic[word] = 1
            total_words += 1
    return total_words


def process_all_tweets(twit_list):
    """
    Loops over all tweets in supplied list and builds word frequency list
    returns frequency list (dictionary) and total word count (float
    :param twit_list: list of tweets where each tweet is a dictionary
    :return frquency_dic, total_words: dictionary of words & counts & float
        of total words in all tweets
    """
    frequency_dic = {}
    total_words = 0.0
    for tweet in twit_list:
        if decide_to_process(tweet):
            total_words = update_frequency_list(tweet, frequency_dic,
                                                total_words)
    return frequency_dic, total_words


def main():
    """
    Main executable to meet question requirements
    """
    tweet_file = open(sys.argv[1])
    tweet_list = parse_tweets(tweet_file)
    results = process_all_tweets(tweet_list)
    freq_dict = results[0]
    wd_ct = results[1]
    for word in freq_dict:
        freq_pct = freq_dict[word] / wd_ct
        print(str(word.encode('utf-8')) + ' ' + str(freq_pct))


if __name__ == '__main__':
    main()
