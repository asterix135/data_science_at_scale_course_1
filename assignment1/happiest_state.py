import sys
import json
import numpy as np
from xml.etree import ElementTree as ET
import matplotlib.path as mp

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


def create_sentiment_dictionary(sent_file):
    """
    Turns sentiment text file into dictionary
    :param sent_file: open file of words & sentiment values, tab separated
    :return dictionary:
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


def contained_in(lat, lon, bound_pts):
    """
    checks if the lat, lon location is contained in the polygon defined
    by bound_coords = returns Boolean
    :param lat: latitude float
    :param lon: logitute float
    :param bound_pts: list of state name and boundaries
    :return Boolean:
    """
    boundary_path = mp.Path(np.array(bound_pts))
    return boundary_path.contains_point((lat, lon))


def state_from_location(lat, lon, state_bound_dic):
    """
    Tries to determine state locatio based on lat/lon data
    if found, returns state name & True, else Unknown & False
    :param lat: float
    :param lon: float
    :param state_bound_dic: dictionary of state names & boundaries
    :return state_name, boolean:
    """
    for state, bound_pts in state_bound_dic.iteritems():
        if contained_in(lat, lon, bound_pts):
            return state, True
    return 'Unknown', False


def parse_state_bounds():
    """
    parses dictionary of state abbreviations & boundary points from XML file
    :return dictionary:
    """
    xml_tree = ET.parse('states.xml')
    states = xml_tree.getroot()
    state_bounds = {}
    for state in states:
        coord_list = []
        for point in state:
            coord_list.append([point.attrib['lat'], point.attrib['lng']])
        name = state.attrib['name']
        state_bounds[name] = coord_list
    return state_bounds


def calculate_tweet_sentiment(tweet, sent_dict):
    """
    calculates & returns sentiment of a tweet based on values in dictionary
    :param tweet: tweet represented as a dictionary
    :param sent_dict: dictionary of words & sentiment values
    :return integer: sentiment value
    """
    tweet_sentiment = 0
    if decide_to_process(tweet):
        for word in tweet['text'].split():
            word = word.lower()
            if word in sent_dict:
                tweet_sentiment += sent_dict[word]
    return tweet_sentiment


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


def get_state_sentiments(tweet_list, sent_dict, state_bound_dic):
    state_happiness = {}
    for tweet in tweet_list:
        state_val = get_state(tweet)
        if decide_to_process(tweet) and state_val:
            sentiment = calculate_tweet_sentiment(tweet, sent_dict)
            if state_val in state_happiness:
                state_happiness[state_val][0] += sentiment
                state_happiness[state_val][1] += 1
            else:
                state_happiness[state_val] = [sentiment, 1]
    happiest =  max(state_happiness, key=lambda k: state_happiness[k])
    return happiest, state_happiness[happiest]


def main():
    """
    Main routine to calculate sentiment value per tweet
    """
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = create_sentiment_dictionary(sent_file)
    twit_list = parse_tweets(tweet_file)
    best = process_tweet_file(twit_list, sent_dict)
    avg_happiness = best[1][0] / float(best[1][1])
    print(str(best[0]) + ' ' + str(avg_happiness))


if __name__ == '__main__':
    main()
