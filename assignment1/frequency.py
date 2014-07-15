import sys
import json
import operator

def parse_tweets(tweet_file):
    tweets = []
    for line in tweet_file:
        jsonTweet = json.loads(line)
        tweets.append(jsonTweet)
    return tweets

def not_in_filter_fn(dictionary):
    def not_in_filter(entry):
        return not entry in dictionary
    return not_in_filter

def prn(x):
    print x

def main():
    tweet_file = open(sys.argv[1])
    tweets = parse_tweets(tweet_file)

    terms = {}
    def add_term(word):
        if not word in terms:
            terms[word] = 0
        terms[word] += 1

    map(lambda tweet: 
        map(add_term, tweet['text'].split()),
        filter(lambda tweet: 'text' in tweet, tweets))

    total_count = reduce(lambda x,y: x + terms[y], terms, 0)

    map(lambda key:
        prn(key + ' ' + str(float(terms[key])/total_count)),
        terms)

if __name__ == '__main__':
    main()
