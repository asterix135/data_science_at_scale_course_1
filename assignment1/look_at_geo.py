"""Scratch file to figure out geocodeing in Twitter"""

import json

STATES = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def parse_tweets(twit_file):
    """
    extracts info from file of tweets into a list
    returns the list of a dictionary per tweet
    :param twit_file: open file of tweets in json forma
    :return list of dictionaries:
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
    checks if tweet is coded as English and has text
    :param tweet: tweet represented as dictionary
    :return boolean:
    """
    if 'lang' in tweet and tweet['lang'] == 'en':
        if 'text' in tweet:
            return True
    return False


def examine_data(tweet_list):
    for tweet in tweet_list:
        if 'coordinates' in tweet and tweet['coordinates']:
            print(tweet['coordinates'])


def get_state(tweet):
    """
    Examines tweet place data to determine if in US and if so, what state
    :param tweet: tweet represented as dictionary
    :return str value of State:
    """
    if 'place' in tweet and tweet['place'] and \
                    tweet['place']['country_code'] == 'US':
        for state in STATES:
            if state in tweet['place']['full_name'] or \
                            STATES[state] in tweet['place']['full_name']:
                return state
    return None


def get_location(tweet):
    state_val = ''
    if 'place' in tweet and tweet['place'] and \
                    'country_code' in tweet['place'] and \
                    tweet['place']['country_code'] == 'US':
        for state in STATES:
            if state in tweet['place']['full_name'] or \
                            STATES[state] in tweet['place']['full_name']:
                state_val = state
        if state_val:
            return state_val
        elif 'geo' in tweet and tweet['geo']:
            print(tweet['geo'])
    return None


def main():
    twit_file = open('output.txt')
    twit_list = parse_tweets(twit_file)
    # examine_data(twit_list)
    for tweet in twit_list:
        print(get_state(tweet))


if __name__ == '__main__':
    main()