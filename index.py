from numpy import loadtxt
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')


# Fetch the data from the web
data = "O SON OF SPIRIT!My first counsel is this: Possess a pure, kindly and radiant heart, that thine may be a sovereignty ancient, imperishable and everlasting. O SON OF SPIRIT!The best beloved of all things in My sight is Justice; turn not away therefrom if thou desirest Me, and neglect it not that I may confide in thee. By its aid thou shalt see with thine own eyes and not through the eyes of others, and shalt know of thine own knowledge and not through the knowledge of thy neighbor. Ponder this in thy heart; how it behooveth thee to be. Verily justice is My gift to thee and the sign of My loving-kindness. Set it then before thine eyes. Veiled in My immemorial being and in the ancient eternity of My essence, I knew My love for thee; therefore I created thee, have engraved on thee Mine image and revealed to thee My beauty Thy Paradise is My love; thy heavenly home, reunion with Me. Enter therein and tarry not. This is that which hath been destined for thee in Our kingdom above and Our exalted dominion. If thou lovest Me, turn away from thyself; and if thou seekest My pleasure, regard not thine own; that thou mayest die in Me and I may eternally live in thee."

# configure nltk with stop words
stopWords = set(stopwords.words('english'))

# load additional stopwords
additionalWords = loadtxt("words.dat", delimiter='\n', dtype=str)
print(additionalWords)
stopWords.update(additionalWords)

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
