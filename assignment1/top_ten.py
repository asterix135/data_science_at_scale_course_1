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


def is_hashtag(word):
    """
    determines whether word is a hashtag
    :param word:
    :return Boolean:
    """
    word = word.lower()
    if word[0] == '#':
        return True
    return False


def update_frequency_list(tweet, hash_dic):
    """
    tokenizes text from a tweet and updates hashtag frequency dictionary
    :param tweet: tweet as dictionary
    :param hash_dic: word frequency dictionary for hashtags
    """
    tweet_words = tweet['text'].split()
    for word in tweet_words:
        if is_hashtag(word):
            word = word.lower()[1:]
            if word in hash_dic:
                hash_dic[word] += 1
            else:
                hash_dic[word] = 1


def process_all_tweets(twit_list):
    """
    Loops over all tweets in supplied list and builds word frequency list
    returns frequency list (dictionary) and total word count (float
    :param twit_list: list of tweets where each tweet is a dictionary
    :return frquency_dic: top ten hashtags & counts as list of tuples
    """
    hashtag_dict = {}
    for tweet in twit_list:
        if decide_to_process(tweet):
            update_frequency_list(tweet, hashtag_dict)
    return find_top_ten_hashes(hashtag_dict)


def find_top_ten_hashes(hash_dict):
    """
    sorts dictionary by values and returns top ten values as list of tuples
    :param hash_dict: dictionary of values & counts
    """
    sorted_hash = sorted(hash_dict.items(), key=lambda x: x[1],
                         reverse=True)
    return sorted_hash[:10]


def main():
    """
    Main executable to meet question requirements
    """
    tweet_file = open(sys.argv[1])
    tweet_list = parse_tweets(tweet_file)
    tt_list = process_all_tweets(tweet_list)
    for item in tt_list:
        print(str(item[0].encode('utf-8')) + ' ' + str(item[1]))


if __name__ == '__main__':
    main()
