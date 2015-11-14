import term_sentiment as ts


def test_master():
    sent_dic = ts.create_sentiment_dictionary(open('AFINN-111.txt'))
    tweet_list = ts.parse_tweets(open('output.txt'))
    new_dict = ts.process_all_tweets(tweet_list, sent_dic)
    for word in new_dict:
        print(word + ' ' + str(float(new_dict[word][1] / new_dict[word][0])))
    print('the' + ' ' + str(float(new_dict['the'][1] / new_dict['the'][0])))


if __name__ == '__main__':
    test_master()
