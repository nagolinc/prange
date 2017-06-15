import random


def parseRules(text):
	'''
	Parse a text file into a bunch of rules
	'''	
	
	lines=text.split("\n")
	
	rules={}
	
	currentRule={"name":"","descriptions":[]}
	
	def newObject():
		if len(currentRule["name"])==0 or len(currentRule["descriptions"])==0:
			return
		rules[currentRule["name"]]=currentRule["descriptions"]
		currentRule["name"]=""
		currentRule["descriptions"]=[]
	
	
	for line in lines:
		if len(line.strip())==0:
			#empty lines start a new object
			newObject()
		elif line[0] in " 	":
			#whitespace starts a new description
			currentRule["descriptions"]+=[line.strip()]
		else:
			currentRule["name"]=line.strip()
	
	return rules
	
	
	
	
def expandDescription(name,rules):
	'''
	Replaces a generic name with a specific one
	e.g. "animal" -> "lion"
	'''
	#fallback
	if name not in rules:
		return name
		
	description=random.choice(rules[name])
	#look for []'s
	while "[" in description:
		start=description.index("[")
		stop=description.index("]")
		description=description[:start]+\
			expandDescription(description[start+1:stop],rules)+\
			description[stop+1:]
	return description
	
	
import os
this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "data", "adventure.txt")
text=open(DATA_PATH).read()
adventureRules=parseRules(text)



	
	
