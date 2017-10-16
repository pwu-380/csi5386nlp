#Python 3

from nltk import TweetTokenizer
import re
from nltk.corpus import stopwords
from nltk import BigramCollocationFinder
from nltk import BigramAssocMeasures
from nltk import TrigramCollocationFinder
from nltk import TrigramAssocMeasures

# Use nltk.download if you don't have corpus:
#import nltk
#nltk.download('stopwords')

# Open files
input_file = open('data\microblog2011.txt', 'r', encoding="utf8")  # The corpus. Read mode
log_file = open('out\H. Log.txt', 'w', encoding="utf8")  # Log of the current run. Write mode
output_file1 = open('out\H. Most Frequent Bigrams.txt', 'w', encoding="utf8") # Write mode
output_file2 = open('out\H. Most Frequent Trigrams.txt', 'w', encoding="utf8") # Write mode

tokens = []  # Holds the tokens of the whole corpus
words = []  # Holds the words of the whole corpus (excluding punctuation & stopwords)

# Tokenize
#for i in range(100):
#    line = input_file.readline()
for line in input_file:
    line = line.lower()  # Change to lowercase

    # Tokenize
    lineTokens = TweetTokenizer().tokenize(line)
    #print(lineTokens, file=log_file)
    tokens = tokens + lineTokens
    #print(tokens, file=log_file)

# Exclude non-english words (%%%), punctuation & stopwords
for token in tokens:
    #Excludes non-word tokens
    if re.search('\W',token) == None:
        #Excludes stopwords
        if (token not in stopwords.words('english')):
            words.append(token)  # This will include all tokens except for stopwords and punctuation

# Find bigram collocations
# http://www.nltk.org/howto/collocations.html
finder = BigramCollocationFinder.from_words(words)
scored = finder.score_ngrams(BigramAssocMeasures.raw_freq)

# Write two-word expressions to log file
for item in scored:
    log_file.write(str(item[1]) + "\t" + str(item[0]) + "\n")

#sorted(bigram for bigram, score in scored)
mostFrequentBigramsList = finder.nbest(BigramAssocMeasures.raw_freq,150)
# To sort the list alphabetically, just use the sorted() function in Python.

# Write to file
for item in mostFrequentBigramsList:
    output_file1.write(str(item) + "\n")

# Find trigram collocations
finder = TrigramCollocationFinder.from_words(words)
scored = finder.score_ngrams(TrigramAssocMeasures.raw_freq)

# Write three-word expressions to log file
for item in scored:
    log_file.write(str(item[1]) + "\t" + str(item[0]) + "\n")

mostFrequentTrigramsList = finder.nbest(TrigramAssocMeasures.raw_freq,150)
# To sort the list alphabetically, just use the sorted() function in Python.

# Write to file
for item in mostFrequentTrigramsList:
    output_file2.write(str(item) + "\n")

log_file.close()