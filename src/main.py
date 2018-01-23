import csv

import nltk
import sklearn

from src.TweetClassifier import Tokenizer, FeatureExtraction, Classifier
from src.scraper.Datascraper import DataScraper
from src.scraper.OauthConnectionClient import OauthClient

from src.MusicRecommender.GenreClassifier import featureExtraction, classify

userTweets_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=2597834149&count=20'
userProfile_url = 'https://api.twitter.com/1.1/users/show.json?user_id=2597834149'

def main():
    oauth_obj = OauthClient()
    oauth_client = oauth_obj.getOauthClient()

    data_scraper = DataScraper(oauth_client)
    user_tweets = data_scraper.getUserTweets(userTweets_url)
    profileInfo = data_scraper.getUserProfileData(userProfile_url)
    print(profileInfo['name'], profileInfo['location'])

    for a in user_tweets:
        tokenList = Tokenizer.preprocess(a['text'])
        featureList = FeatureExtraction.getfeatureVector(tokenList)

    #Classifier.featureListCorpus()
    #tweets = Classifier.featureListCorpus()
    #print(tweets)
    #trainingSet = nltk.classify.util.apply_features(Classifier.extractFeatures, tweets)
    #print(trainingSet)
    #NBClassifier = nltk.NaiveBayesClassifier.train(trainingSet)

    #Classifier.saveClassifier(NBClassifier)
    cls = Classifier.loadClassifier()
    testTweet = 'At a gathering I found myself involuntarily sitting next to two � people who expressed opinions that I considered very low and � discriminating.,,'
    processedTestTweet = Tokenizer.preprocess(testTweet)
    #print(Classifier.extractFeatures(FeatureExtraction.getfeatureVector(processedTestTweet)))
    print(cls.classify(Classifier.extractFeatures(FeatureExtraction.getfeatureVector(processedTestTweet))))
    #print(cls.show_most_informative_features(10))

if __name__ == '__main__':
    #main()
    Y, X = featureExtraction()
    import numpy as np
    Y = np.array(Y).astype(np.float)
    X = np.array(X).astype(np.float)
    test = np.array([0,0,0,1,1,0,1,0,0,4,1]).astype(np.float)
    classify(X,Y, test)
