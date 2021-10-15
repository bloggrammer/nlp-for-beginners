
#I, my, is, to, etc.

text = "I love to play football.".lower()

stop_words = ["i", "my", "the","to", "for"]

tokens = text.split()

clean_data = tokens[:]

for token in tokens:
    if token in stop_words:
        clean_data.remove(token)

print(clean_data)