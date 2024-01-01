import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string


with open('text.txt', 'r') as file:
    text = file.read()
# Токенізація
tokens = word_tokenize(text)

# Лемматизація та стеммінг
wordnet_lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
lemmatized = [wordnet_lemmatizer.lemmatize(token) for token in tokens]
stemmed = [ps.stem(token) for token in lemmatized]

# Видалення стоп-слів
stopwords = set(stopwords.words('english'))
filtered = [token for token in stemmed if token.lower() not in stopwords]

# Видалення пунктуації
filtered = [token for token in filtered if token not in string.punctuation]


with open('finaltext.txt', 'w') as file:
    file.write(' '.join(filtered))