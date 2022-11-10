import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from simhash import Simhash

#global set of stopwords
english_stopwords = set(stopwords.words('english'))

def tokenizeText(content):
    global english_stopwords
    #returns a list of tokens found in the given pathname
    tokens = word_tokenize(content)
    tokensWithoutStopWords = []
    for word in tokens:
        if word not in english_stopwords:
            tokensWithoutStopWords.append(word)
    #print(Simhash(tokensWithoutStopWords))
    return tokensWithoutStopWords

def computeWordFrequencies(tokens):
    mydict = dict()
    for token in tokens:
        frequency = 1
        if(token not in mydict.keys()):
            mydict[token] = frequency
        else:
            mydict[token] += frequency
    return mydict