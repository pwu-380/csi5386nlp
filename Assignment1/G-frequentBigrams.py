# Python 3

import re

from nltk.corpus import stopwords
from nltk.tokenize.casual import TweetTokenizer
from nltk.util import bigrams
from nltk.probability import FreqDist

# Use nltk.download if you don't have corpus:
#import nltk
#nltk.download('stopwords')

# Location of input & output files (legacy)
READ_FILE = 'data\microblog2011.txt'  # The corpus
WRITE_FILE1 = 'out\G. Bigrams List.txt'  # List of bigrams

# Open files
input_file = open(READ_FILE, 'r', encoding="utf8")  # Read mode
output_file1 = open(WRITE_FILE1, 'w', encoding="utf8") # Write mode
output_file2 = open('out\G. Most Frequent Bigrams.txt', 'w', encoding="utf8") # Write mode
log_file = open('out\G. Log.txt', 'w', encoding="utf8")  # Log of the current run

bgs = []  # list of bigrams in the whole corpus
words = []  # list of words in the whole corpus

# Tokenize each line
for i in range(10):
    lineWords = []

    line = input_file.readline()
    print(line, file=log_file)
    line = line.lower()  # Change to lowercase
    lineTokens = TweetTokenizer().tokenize(line)
    print(lineTokens, file=log_file)

    # Exclude punctuation & stopwords
    for token in lineTokens:
        #Excludes non-word tokens
        if re.search('\W',token) == None:
            #Excludes stopwords
            if (token not in stopwords.words('english')):
                lineWords.append(token)  # This will include all tokens except for stopwords and punctuation

    print("LineWords=",lineWords, file=log_file)
    words = words + lineWords
    print("words=",words, file=log_file)
    print("Line Bigrams:",list(bigrams(lineWords)), file=log_file)
    bgs = bgs + list(bigrams(lineWords))
    print("bgs=",bgs, file=log_file)
    #out = " ".join(s.encode('ascii', 'ignore') for s in tokens)
    #file_tokenized.write(out+'\n')
    print('**********', file=log_file)

# Write to file
for item in bgs:
    output_file1.write(str(item) + "\n")
output_file1.close()

# Compute frequency distribution for all the bigrams in the corpus
fdist1 = FreqDist(bgs)
total_bigrams = fdist1.N()
unique_bigrams = fdist1.B()
print("Number of total bigrams:", total_bigrams, file=log_file)
print("Number of unique bigrams:", unique_bigrams, file=log_file)
print("10 most common bigrams:", file=log_file)
mostFrequentBigramsList = fdist1.most_common(10)
print(mostFrequentBigramsList, file=log_file)

# Write to file
for item in mostFrequentBigramsList:
    #print(item[1],"\t",item[0],"\n\n")
    output_file2.write(str(item[1]) + "\t" + str(item[0]) + "\n")
output_file2.close()

# Compute frequency distribution for all the words (excluding stopwords) in the corpus
fdist2 = FreqDist(words)
total_words = fdist2.N()
unique_words = fdist2.B()
print("Number of total words:", total_words)
print("Number of unique words:", unique_words)
print("Lexical Density (type/token ratio for word-only tokens):", unique_words/total_words)