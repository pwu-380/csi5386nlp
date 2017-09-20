#Opens a tokenized textfile and counts # tokens and # unique tokens

from nltk.tokenize.casual import TweetTokenizer
from nltk.probability import FreqDist
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

READFILE = 'data/microblog2011.txt'         #Open raw file here
SAVEFILE = 'out/tokens.txt'                 #Save distribution here

file_source = open(READFILE, 'r')
file_dist = open(SAVEFILE, 'w')


text = []

#Aggregate all tokens into list
for line in range(2):
    line = file_source.readline()
    line = line.lower()
    # print TweetTokenizer().tokenize(line)
    text = text + TweetTokenizer().tokenize(line)

#Create frequency distribution
fdist = FreqDist(text)
total_tokens = fdist.N()
unique_tokens = fdist.B()

#Print distribution properties
print "The number of total tokens:", total_tokens
print "The number of unique tokens:", unique_tokens
print "The type/token ratio:", (unique_tokens + 0.0)/total_tokens

print "\nTokens that only appear once:"
print "======================="
for w in fdist.hapaxes():
    print w

print "\nThe most common tokens:"
print "======================="
for x in fdist.most_common(10):
    w, n = x
    print str(n) + '\t' + w

print "\nCounts of all tokens:"
print "======================="
for x in fdist:
    out = str(fdist[x]) + "\t" + str(x)
    print out
    #Save distribution to file
    file_dist.write(out + '\n')