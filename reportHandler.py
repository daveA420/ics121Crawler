#make file if it don't exist
#file is used to make my report
#doesn't carry over from last report
import PartA #used to tokenize content of website
from urllib.parse import urldefrag

MYREPORT = open("myCrawlerReport.txt", 'w+')
MYREPORT.close()

MOSTWORDS = 0
MOSTWORDSURL = ''
NUMUNIQUEPAGES = 0
UNIQUEPAGES = dict()

def addToReport(url, contents):
    myTokens = PartA.tokenizeText(contents)
    myFrequencies = PartA.computeWordFrequencies(myTokens)
    urlWithoutFrag= urldefrag(url)
    updateReport(urlWithoutFrag, myFrequencies)

def updateReport(url, tokenFrequencyDict):
    NUMUNIQUEPAGES = len(UNIQUEPAGES)
    UNIQUEPAGES[url] = 1
    if len(tokenFrequencyDict) > MOSTWORDS:
        MOSTWORDSURL = url
        MOSTWORDS = len(tokenFrequencyDict)
    MYREPORT = open("myCrawlerReport.txt", 'r+')
    MYREPORT.write("most words: " + str(MOSTWORDS))
    MYREPORT.write("url with most words: " + MOSTWORDSURL)
    MYREPORT.write("number of unique pages: " + str(NUMUNIQUEPAGES))
    MYREPORT.close()
