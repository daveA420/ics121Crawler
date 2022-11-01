
def tokenize(pathname):
    #returns a list of tokens found in the given pathname
    tokens = list()
    f = open(pathname,'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        word = ""
        for character in line:
            if((47 < ord(character) < 58) or ord(character) > 64 ):
                word += character
                if(character is line[-1]):
                    tokens.append(word)
            else:
                tokens.append(word)
                word = ''
    return tokens

def tokenizeText(content):
    #returns a list of tokens found in the given pathname
    tokens = list()
    word = ""
    for character in content:
        if((47 < ord(character) < 58) or ord(character) > 64 ):
            word += character
        else:
            if(word.len() > 2):
                tokens.append(word)
            word = ''
    return tokens
def computeWordFrequencies(tokens):
    mydict = dict()
    for token in tokens:
        frequency = 1
        if(token not in mydict.keys()):
            mydict[token] = frequency
        else:
            mydict[token] += frequency
    return mydict



def printFrequencies(mydict):
    sorteddict = dict(sorted(mydict.items(), key= lambda item: -item[1]))
    #figured out how to sort the dictionary by it's values with python 3.6
    #by using website https://realpython.com/sort-python-dictionary/#:~:text=Sorting%20Dictionaries%20in%20Python%201%20Using%20the%20sorted,...%206%20Converting%20Back%20to%20a%20Dictionary%20
    for pair in sorteddict:
        print(pair + " => " + str(sorteddict[pair]))

    return
if __name__ == '__main__':
    mytokens = tokenize(input("give a file path"))
    mydictionary = computeWordFrequencies(mytokens)
    printFrequencies(mydictionary)