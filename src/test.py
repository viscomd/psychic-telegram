import library
import sample_text
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
from nltk.stem.porter import *
stemmer = PorterStemmer()
from prettytable import PrettyTable

def formatDatasource(stringType="null", string=[""]):
	'''
		output: print grid of changes
	'''
 	table = PrettyTable()
	final_output = []
	name_array = [stringType] * len(string)
	tokenized_election = []
	for i in string:
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
	table.add_column("Data Source",name_array)
	table.add_column("Raw Text",string)
	table.add_column("Tokenized",tokenized_election)
	table.add_column("stop words removed",stop_election)
	table.add_column("words stemmed",stem_election)
	table.format= True
	table.border=True
	return table.get_html_string()
	
html = ""
html+= formatDatasource("poll Tracker",sample_text.pollTracker)
html+= formatDatasource("Leader Query",sample_text.leaderQuery)
html+= formatDatasource("vote Compass",sample_text.voteCompass)
html+= formatDatasource("election Map",sample_text.electionMap)

f = open("output.html", "w")
f.write(html)
'''
print(tokenized_election)
print("-----------------")
print(stop_election)
print("-----------------")
print(stem_election)

'''
