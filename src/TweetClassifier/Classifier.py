import csv
import pickle
from src.TweetClassifier import Tokenizer, FeatureExtraction


# Read the tweets one by one and process it


def featureListCorpus():
    inpTweets = csv.reader(open('../src/TweetClassifier/sampleDataset.csv', 'r'))
    tweets = []

    for row in inpTweets:
        sentiment = row[2]
        tweet = row[3]
        processedTweet = Tokenizer.preprocess(tweet)
        featureVector = FeatureExtraction.getfeatureVector(processedTweet)
        tweets.append((featureVector, sentiment))
    #print(tweets)
    return tweets


def extractFeatures(tweet):
    featureList = []
    tweets = featureListCorpus()
    for t in tweets:
        for i in t[0]:
            featureList.append(i)
    featureList = list(set(featureList))
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s) ' % word] = (word in tweet_words)
    #print(features)
    return features

def saveClassifier(classifier):
    f = open('../src/TweetClassifier/myClassifier.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()

def loadClassifier():
    f = open('myClassifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier