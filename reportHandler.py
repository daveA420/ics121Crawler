#make file if it don't exist
#file is used to make my report
#doesn't carry over from last report
import newParser #used to tokenize content of website
from urllib.parse import urldefrag, urlparse
import shelve

MYREPORT = open("myCrawlerReport.txt", 'w+')
MYREPORT.close()

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
    updateReport(urlWithoutFrag, myFrequencies, sub)

def updateReport(url, tokenFrequencyDict, subdomain):
    global NUMUNIQUEPAGES
    global UNIQUEPAGES
    global MOSTWORDS
    global MOSTWORDSURL
    global UNIQUESUBDOMAINS

    print(str(url))
    print(str(subdomain))
    if str(url) not in UNIQUEPAGES:

        if str(subdomain) not in UNIQUESUBDOMAINS:
            UNIQUESUBDOMAINS[str(subdomain)] = 0
        else:
            UNIQUESUBDOMAINS[str(subdomain)] += 1

    UNIQUEPAGES[str(url)] = True
    NUMUNIQUEPAGES = 0
    for page in UNIQUEPAGES:
        NUMUNIQUEPAGES += 1

 #   NUMUNIQUEPAGES = len(UNIQUEPAGES)

    if len(tokenFrequencyDict) > MOSTWORDS:
        MOSTWORDSURL = str(url)
        MOSTWORDS = len(tokenFrequencyDict)

    try:
        MYREPORT.seek(0)

        MYREPORT.write("most words: " + str(MOSTWORDS) + '\n')
        MYREPORT.write("url with most words: " + MOSTWORDSURL+ '\n')
        MYREPORT.write("number of unique pages: " + str(NUMUNIQUEPAGES) + '\n')
        MYREPORT.write(str([sub +'   ' + str(UNIQUESUBDOMAINS[sub]) for sub in UNIQUESUBDOMAINS]))

    except:
            print('file Error')
