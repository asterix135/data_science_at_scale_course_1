import frequency as f


def test_master():
    tweet_list = f.parse_tweets(open('output.txt'))
    results = f.process_all_tweets(tweet_list)
    freq_dict = results[0]
    word_ct = results[1]
    print(word_ct)
    for word in freq_dict:
        freq_pct = freq_dict[word] / word_ct
        print(str(word.encode('utf-8')) + ' ' + str(freq_pct))


if __name__ == '__main__':
    test_master()