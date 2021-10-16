# NLP Assignment

## Tokenization: Exercise 1

1. Why do we need to tokenize a text in NLP?

2. Can you tell me how many tokens contains in the bold text:
**The wolf said: "Little pig, little pig, let me come in."**
3. Consider the following book title: ***This Is the Beat Generation: New York-San Francisco-Paris.*** What would it take to be able to tokenize such strings so that each city name was stored as a single token?
4. Is this text tokenized?
	- The wolf said : " Little pig , little pig , let me come in . "
	- Welcome
	
		 !     
		 Can  
     
		I     
		help     
		you     
		?     
		I 
    
		’m     
		fine     
		.
    
5. Given the text:

***’The receptor-ligand complexes were then released from the cell membrane preparation ’ +\ ’by incubation with RIB + detergent, which contained RIB appended with 50 mM ’ +\ ’N-dodecyl-N, N (dimethylammonio) butyrate, 1.5% glycerol, and 2% NP-40 for 1 h at 37C’ +\ ’and centrifuged at 95,000 rpm for 3 h at 15C.’***

	- Tokenize using regular expression
	- Tokenize using nltk package
	- For each tokenization, compute the number of tokens, using the len() function, and print the result.
  
  ## Stop Words: Exercise 2
  
  1. Lists the approach used to remove stop words?
2. Remove stop words from the text below:

"Stop words are most common words found in any natural
language which carries very little or no significant semantic
context in a sentence. It just carry syntactic importance which
aid in formation of sentence. As a preprocessing operation it
must be removed to ease further task and speedup core task in
text processing. Ibrahim A [3] conducted a comparative study
on the effect of stop words elimination on Arabic Information
Retrieval where three stop lists viz, General Stop list, corpus
based stop-list and combined stop list were used for
comparative study. General stop-list performed better than the
rest of the two. Ashish T, et al [4] eliminated stop-word in
Gujarati language by preparing frequency list from Gujarati
corpus by analyzing popular Gujarati newspapers. Riyad A, et
al [5], used Finite State Machine (FSM) algorithm to eliminate
stop-words for Arabic Language. Basim A, et al [6] have
designed and implemented a new stop-word removal technique
for Arabic language based on dedicated list and algorithm
which compares stopwords if it fulfills desired string length
criteria. Vijayarani S, et al[7] used Zipf’s Law (Z method) for
creation of stop-words. Rakholia and Saini [8] have presented
a rule-based approach to dynamically identify stop words for
Gujarati language. They have also deployed this approach
with additional cosine similarity based Vector Space Model for
information retrieval in Gujarati language [9]. Kaur J and Saini
JR have presented the list of Punjabi stop words [10], its Partof-Speech class based classification [11] and its Gurumukhi
and Shahmukhi script versions [12]. Saini and Rakholia [13]
have presented an analytic in-depth report on continent and
script-wise divisions-based statistical measures for stopwords
lists of various international Languages."
