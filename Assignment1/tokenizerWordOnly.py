#This script tokenizes words only

from nltk.tokenize.casual import TweetTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

#Use nltk.download if you don't have corpus:
# import nltk
# nltk.download('stopwords')

READFILE = 'data/microblog2011.txt'         #Open raw file here
EXCLUDE_STOPWORDS = True                    #Set to include/exclude stopwords

file_source = open(READFILE, 'r')
text = []

#Aggregate all tokens into list
for line in file_source:
    line = line.lower()
    token_list = TweetTokenizer().tokenize(line)
    for token in token_list:
        #Excludes non-word tokens
        if re.search('\W',token) == None:
            #Excludes stopwords
            if (EXCLUDE_STOPWORDS) and (token not in stopwords.words('english')):
                text.append(token)
            elif (not EXCLUDE_STOPWORDS):
                text.append(token)

print text

#Create frequency distribution
fdist = FreqDist(text)
total_tokens = fdist.N()
unique_tokens = fdist.B()

if EXCLUDE_STOPWORDS:
    print "Stopwords are excluded"
else:
    print "Stopwords are NOT excluded"

#Print distribution properties
print "\nThe number of total tokens:", total_tokens
print "The number of unique tokens:", unique_tokens
print "Lexical density:", (unique_tokens + 0.0)/total_tokens

print "\nThe most common Words:"
print "======================="
for x in fdist.most_common(100):
    w, n = x
    print str(n) + '\t' + w