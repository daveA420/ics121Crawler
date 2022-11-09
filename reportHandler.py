#make file if it don't exist
#file is used to make my report
#doesn't carry over from last report
import newParser #used to tokenize content of website
from urllib.parse import urldefrag
import shelve

MYREPORT = open("myCrawlerReport.txt", 'w+')
MYREPORT.close()

MOSTWORDS = 0
MOSTWORDSURL = ''
NUMUNIQUEPAGES = 0
UNIQUEPAGES = shelve.open('UniquePages.shelve')

def addToReport(url, contents):
    myTokens = newParser.tokenizeText(contents)
    myFrequencies = newParser.computeWordFrequencies(myTokens)
    urlWithoutFrag= urldefrag(url)
    updateReport(urlWithoutFrag, myFrequencies)

def updateReport(url, tokenFrequencyDict):
    global NUMUNIQUEPAGES
    global UNIQUEPAGES
    global MOSTWORDS
    global MOSTWORDSURL

    UNIQUEPAGES[url] = '0'
    NUMUNIQUEPAGES = len(UNIQUEPAGES)

    if len(tokenFrequencyDict) > MOSTWORDS:
        MOSTWORDSURL = str(url)
        MOSTWORDS = len(tokenFrequencyDict)
    try:
        MYREPORT = open("myCrawlerReport.txt", 'w+')

        MYREPORT.write("most words: " + str(MOSTWORDS) + '\n')
        MYREPORT.write("url with most words: " + MOSTWORDSURL+ '\n')
        MYREPORT.write("number of unique pages: " + str(NUMUNIQUEPAGES) + '\n')
        MYREPORT.write("reached the end")
        MYREPORT.close()
    except:
            print('file Error')
