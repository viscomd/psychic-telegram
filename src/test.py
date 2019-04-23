import library
import sample_text
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
from nltk.stem.porter import *
stemmer = PorterStemmer()

print(sample_text.election)
tokenized_election = []
for i in sample_text.election:
	tokenized_election.append(word_tokenize(i))
stop_election = []
for sentence in tokenized_election:
	sample = []
	for token in sentence:
		if token not in stop:
			sample.append(token)
	stop_election.append(sample)
stem_election = []
for sentence in stop_election:
	stem_election.append([stemmer.stem(token) for token in sentence])
		
print(tokenized_election)
print("-----------------")
print(stop_election)
print("-----------------")
print(stem_election)


