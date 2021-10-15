from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = stopwords.words('english')

text = "I love to play football.".lower()

tokens = word_tokenize(text)

clean_data = tokens[:]

for token in tokens:
    if token in stop_words:
        clean_data.remove(token)

filter_data = []

for token in tokens:
    if token not in stop_words:
        filter_data.append(token)

print(filter_data)