import csv
import pickle
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

def featureExtraction():
    inpData = csv.reader(open('../src/MusicRecommender/MusicData.csv','r'))
    mood = []
    sentiment_list = []
    for row in inpData:
        genre = row[0]
        mood.append(genre)
        sentiment_list.append([row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]])
    import pprint
    pprint.pprint(mood)
    pprint.pprint(sentiment_list)
    return mood, sentiment_list

def saveClassifier(classifier):
    f = open('../src/MusicRecommender/musicGenreClassifier.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()

def loadClassifier():
    f = open('../src/MusicRecommender/musicGenreClassifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier

def classify(X,Y,new):
    clf = GaussianNB()
    clf.fit(X, Y)
    print(clf.predict([new]))
    testPrediction(clf)

def testPrediction(cls):
    inpData = csv.reader(open('../src/MusicRecommender/SampleCorpus.csv', 'r'))
    mood = []
    sentiment_list = []
    for row in inpData:
        genre = row[0]
        mood.append(genre)
        sentiment_list.append(
            [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]])
    Y = np.array(mood).astype(np.float)
    X = np.array(sentiment_list).astype(np.float)
    print(cls.score(X,Y))