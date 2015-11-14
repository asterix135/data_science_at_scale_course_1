"""
Testing routines
"""

import tweet_sentiment as ts


def test_dic_conversion():
    """
    Test create_sentiment_dictionary
    """
    sent_file = open('AFINN-111.txt')
    sent_dic = ts.create_sentiment_dictionary(sent_file)
    ctr = 0
    for key in sent_dic:
        print(str(key) + ", " + str(sent_dic[key]))
        if ctr > 5:
            break
        ctr += 1
    sent_file.close()


def test_json_load():
    """
    test parse_tweets()
    """
    tweet_file = open('output.txt')
    parsed = ts.parse_tweets(tweet_file)
    cnt = 0
    for item in parsed:
        print(item)
        cnt += 1
        if cnt > 5:
            break
    tweet_file.close()


def test_calculate_sentiment():
    """
    tests calculate_tweet_sentiment
    """
    tweet_dic = ts.create_sentiment_dictionary(open('AFINN-111.txt'))
    tweet_list = ts.parse_tweets(open('problem_1_submission.txt'))
    for tweet in tweet_list:
        print(ts.calculate_tweet_sentiment(tweet, tweet_dic))


def test_master():
    """
    Use to set up what's being tested
    """
    #test_dic_conversion()
    #test_json_load()
    test_calculate_sentiment()


if __name__ == '__main__':
    test_master()