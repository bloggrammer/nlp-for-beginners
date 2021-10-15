from nltk.tokenize import SpaceTokenizer, LineTokenizer
from nltk.tokenize import word_tokenize

space_tokenizer = SpaceTokenizer()

text  = "That is John's laptop. He bought it on Amazon.".lower()

tokens = space_tokenizer.tokenize(text)

line_tokenizer = LineTokenizer()

line_text  = "That is John's laptop. \nHe bought it on Amazon.".lower()
#That is John's laptop.
#He bought it on Amazon.
line_tokens = line_tokenizer.tokenize(line_text)

#Tokenization using nltk word_tokenize
word_text  = "That is John's laptop. He bought it on Amazon.".lower()

word_tokens = word_tokenize(word_text)

print(word_tokens)