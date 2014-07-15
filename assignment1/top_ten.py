import sys
import json
import operator
import heapq

def main():
    tweet_file = open(sys.argv[1])
    tweets = parse_tweets(tweet_file)

    hash_counts = {}

    for tweet in tweets:
        if "entities" in tweet and "hashtags" in tweet["entities"]:
            for hashtag in tweet["entities"]["hashtags"]:
                hashtag_text = hashtag["text"]
                if not hashtag_text in hash_counts:
                    hash_counts[hashtag_text] = 0
                hash_counts[hashtag_text] -= 1

    hash_list = heapq.nsmallest(10, hash_counts.iteritems(), operator.itemgetter(1))

    for tuple in hash_list:
        print tuple[0] + " " + str(-tuple[1])

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

def not_in_dict_filter_fn(dictionary):
    def not_in_dict_filter(entry):
        return not entry in dictionary
    return not_in_dict_filter

def prn(x):
    print x 


if __name__ == '__main__':
    main()