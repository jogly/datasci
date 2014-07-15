import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = parse_sentiment_scores(sent_file)
    tweets = parse_tweets(tweet_file)

    unknown_words = {}
    sentiment = 0
    def add_sentiment(word):
        if not word in unknown_words:
            unknown_words[word] = {'value': 0, 'count': 0}
        unknown_words[word]['count'] += 1
        unknown_words[word]['value'] = unknown_words[word]['value'] + sentiment

    for tweet in tweets:
        sentiment = tweet_sentiment(tweet, sent_scores);
        words = (tweet['text'].split() if 'text' in tweet else [''])

        map(add_sentiment, filter(not_in_filter_fn(sent_scores), words))

    map(lambda key: 
        prn(key.encode('utf-8') + ' ' + str(float(unknown_words[key]['value'])/unknown_words[key]['count'])), 
        unknown_words)

def word_map_fn(word_dict, no_match_value=None):
    def word_map(word):
        if word in word_dict:
            return word_dict[word]
        else:
            return no_match_value
    return word_map

def parse_sentiment_scores(sent_file):
    sent_scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        sent_scores[term] = int(score)
    return sent_scores

def parse_tweets(tweet_file):
    tweets = []
    for line in tweet_file:
        jsonTweet = json.loads(line)
        tweets.append(jsonTweet)
    return tweets

def tweet_sentiment(tweet, sent_scores):
    sentiment_map = word_map_fn(sent_scores, 0)
    return reduce(
        lambda x,y: x+y, 
        map(sentiment_map, 
            (tweet['text'].split() if 'text' in tweet else [0])),
        0)

def not_in_filter_fn(dictionary):
    def not_in_filter(entry):
        return not entry in dictionary
    return not_in_filter

def prn(x):
    print x

if __name__ == '__main__':
    main()
