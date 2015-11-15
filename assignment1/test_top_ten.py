import top_ten as tt


def test_master():
    tweet_list = tt.parse_tweets(open('output.txt'))
    tt_list = tt.process_all_tweets(tweet_list)
    for item in tt_list:
        print(item[0]) + ' ' + str(item[1])


if __name__ == '__main__':
    test_master()