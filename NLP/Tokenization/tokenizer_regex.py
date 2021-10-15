#define a rule for splitting the text
import re

text = "I love going out\n with friends, but mostly \non weekends."

rule = ',|\n|\*'

tokens = re.split(rule,text)

print(tokens)