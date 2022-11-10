#make file if it don't exist
#file is used to make my report
#doesn't carry over from last report
import newParser #used to tokenize content of website
from urllib.parse import urldefrag, urlparse
import shelve

MYREPORT = open("myCrawlerReport.txt", 'w+')

MOSTWORDS = 0
MOSTWORDSURL = ''
NUMUNIQUEPAGES = 0
UNIQUEPAGES = shelve.open('UniquePages.shelve')
UNIQUESUBDOMAINS = shelve.open('uniqueDomains.shelve')

def addToReport(url, contents):
    myTokens = newParser.tokenizeText(contents)
    myFrequencies = newParser.computeWordFrequencies(myTokens)
    urlWithoutFrag= urldefrag(url).url
    sub = urlparse(urlWithoutFrag).netloc
    updateReport(urlWithoutFrag, myTokens, sub)

def updateReport(url, tokens, subdomain):
    global NUMUNIQUEPAGES
    global UNIQUEPAGES
    global MOSTWORDS
    global MOSTWORDSURL
    global UNIQUESUBDOMAINS

    if str(url) not in UNIQUEPAGES:

        if str(subdomain) not in UNIQUESUBDOMAINS:
            UNIQUESUBDOMAINS[str(subdomain)] = 1
        else:
            UNIQUESUBDOMAINS[str(subdomain)] += 1

    UNIQUEPAGES[str(url)] = True

    NUMUNIQUEPAGES = len(UNIQUEPAGES)

    if len(tokens) > MOSTWORDS:
        MOSTWORDSURL = str(url)
        MOSTWORDS = len(tokens)

    try:
        MYREPORT.seek(0)

        MYREPORT.write("most words: " + str(MOSTWORDS) + '\n')
        MYREPORT.write("url with most words: " + MOSTWORDSURL+ '\n')
        MYREPORT.write("number of unique pages: " + str(NUMUNIQUEPAGES) + '\n')
        MYREPORT.write(str([sub +'   ' + str(UNIQUESUBDOMAINS[sub]) for sub in UNIQUESUBDOMAINS]))

    except:
            print('file Error')
