from numpy import loadtxt
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# configure nltk with stop words
stopWords = set(stopwords.words('english'))

# load additional stopwords
additionalWords = loadtxt("words.dat", delimiter='\n', dtype=str)
stopWords.update(additionalWords)

# Load up the data
with open("source.txt", "r") as f:
    data = f.read()

# perform the word search
words = word_tokenize(data)
wordsFiltered = []

for w in words:
    if w.lower() not in stopWords:
        wordsFiltered.append(w)

# Output the results
with open("results.dat", "w") as f:
    for w in set(wordsFiltered):
        f.write(w + '\n')
