import json

filename = './emotionMap'
datafile = open(filename).read()
data = json.loads(datafile)


def extractEmotion(unicodeList):
    emotionList = []
    for unicodeVal in unicodeList:
        emotionList.append(data[unicodeVal])
    return emotionList


unicodeList = ["b'\\U0001F600", "b'\\U0001F623", "b'\\U0001F618"]
print(extractEmotion(unicodeList))
