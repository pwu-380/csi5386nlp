#Opens a tokenized textfile and counts # tokens and # unique tokens

from nltk.tokenize.casual import TweetTokenizer
from nltk.probability import FreqDist

READFILE = 'data/microblog2011.txt'         #Open raw file here
SAVEFILE = 'out/tokens.txt'                 #Save distribution here

file_source = open(READFILE, 'r')
file_dist = open(SAVEFILE, 'w')


text = []

#Aggregate all tokens into list
for line in range(2):
    line = file_source.readline()
    print TweetTokenizer().tokenize(line.lower())
    text = text + TweetTokenizer().tokenize(line)

#Create frequency distribution
fdist = FreqDist(text)
total_tokens = fdist.N()
unique_tokens = fdist.B()

#Print distribution properties
print "The number of total tokens:", total_tokens
print "The number of unique tokens:", unique_tokens
print "The type/token ratio:", (unique_tokens + 0.0)/total_tokens
print "Tokens that only appear once:", fdist.hapaxes()
print "\nThe most common tokens:", ", ".join(str(w) for w in fdist.most_common(10))
print "\nCounts of all tokens:"
print "======================="
for x in fdist:
    print x, ":", fdist[x]
    #Save distribution to file
    out = str(fdist[x]) + "\t" + str(x)
    file_dist.write(out.encode('ascii', 'ignore') + '\n')