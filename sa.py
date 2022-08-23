import json
import random


# setting the target or the price in our case
target = 95

# reading the data from the JSON file
data = ''
with open('data.json') as json_file:
	data = json.load(json_file)

"""
	function to select the nearst or the exact value from the data
	it takes three params
	1 - the firs one is the target or the needed value
	2 - the second one is the random phones that selected
	3 - the third is our data set
"""
def selectTheBest(target, random_phones, data):
	currentPrice = 0
	currentName = ''
	for phone in random_phones:
		if abs(data[phone] - target) < abs(currentPrice - target):
			currentPrice = data[phone]
			currentName = phone
	print(currentName, currentPrice)


# selecting random phones from the data set
random_phones = [random.choice(list(data)) for i in range(10)]


# calling the function to do the job
selectTheBest(target, random_phones, data)

