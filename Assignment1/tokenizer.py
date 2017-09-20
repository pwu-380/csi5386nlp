#Takes a textfile and outputs a tokenized textfile

from nltk.tokenize.casual import TweetTokenizer

#Use nltk.download if you don't have corpus:
# nltk.download('punkt')

READFILE = 'data/microblog2011.txt'                 #Open raw file here
SAVEFILE = 'out/microblog2011_tokenized.txt'        #Save tokenized file here

#Open files
file_source = open(READFILE, 'r')
file_tokenized = open(SAVEFILE, 'w')

#Tokenize each line and write it to save file
for line in file_source:
    tokens = TweetTokenizer().tokenize(line)
    out = " ".join(s.encode('ascii', 'ignore') for s in tokens)
    file_tokenized.write(out+'\n')