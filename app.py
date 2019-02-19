import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def ans(word):
	word=word.lower()
	if word in data:
		return data[word]

	elif word.title() in data:
		return data[word.title()]

	elif word.upper() in data:
		return data[word.upper()]
		
	elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
		yn=input("Did you mean %s instead ? Enter Y if Yes or N if No: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
		if yn == "Y":
			return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
		elif yn == "N":
			return "The word doesn't exist. Please double check it."
		else:
			return "Sorry, we didn't understand your Entry."
	
	else:
		return "The word doesn't exist. Please double check it."

word=input("Enter the word : ")

output=ans(word)

if type(output)==list:
	for i in output:
		print(i)

else:
	print(output)