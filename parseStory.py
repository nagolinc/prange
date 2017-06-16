import random


def parseDescriptions(text):
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
	
def getProperties(text):
	out=[]
	t=0
	while "[" in text:
		start=text.index("[")
		stop=text.index("]")
		l=text[start+1:stop].split(":")
		propName=l[0]
		if "." in propName:
			propName=propName[:propName.index(".")]
		if len(l)>1:
			propType=l[1]
		else:
			propType=propName
		if len(l)>2:
			overrides=l[2].split(",")
		else:
			overrides=[]
		out+=[(propName,propType,overrides)]
		text=text[stop+1:]
		#print(t,start,stop)
	return out
	
	
class DescriptionRule:
	def __init__(self,name,descriptions):
		self.name=name
		self.descriptions=descriptions
		self.outputs=["description"]
	def canAct(self,obj,rules):
		return obj["name"]==self.name
	def act(self,obj,rules):
		description=random.choice(self.descriptions)
		#print("generating description",description)
		obj["description"]=description
		
class PropertyRule:
	def __init__(self,name,propName,propType,overrides):
		self.name=name
		self.propName=propName
		self.propType=propType
		self.overrides=overrides
		self.outputs=[propName]
	def canAct(self,obj,rules):
		return obj["name"]==self.name
	def act(self,obj,rules):
		child={"parent":obj,"name":self.propType}
		#print("adding child",child)
		obj[self.propName]=child
		
def getDescriptionRules(text):
	out=[]
	namesAndDescriptions=parseDescriptions(text)
	for name,descriptions in namesAndDescriptions.items():
		out+=[DescriptionRule(name,descriptions)]
		properties=getProperties("\n".join(descriptions))
		for propName,propType,overrides in properties:
			out+=[PropertyRule(name,propName,propType,overrides)]
	return out

	
	
def expandDescription(obj,rules):
	'''
	Replaces a generic name with a specific one
	e.g. "animal" -> "lion"
	'''
	if isinstance(obj,str):
		return obj
	
	try:
		description=getProperty("description",obj,rules)
	except:
		#return obj["name"]
		raise AttributeError
	#look for []'s
	while "[" in description:
		start=description.index("[")
		stop=description.index("]")
		propName=description[start+1:stop].split(":")[0]
		#print("getting property",propName,"in",obj)
		child=getProperty(propName,obj,rules)		
		description=description[:start]+\
			expandDescription(child,rules)+\
			description[stop+1:]
	return description

	
def getProperty(propName,obj,rules):
	assert isinstance(obj,dict)
	#handle .
	if "." in propName:
		i=propName.index(".")
		#print("getting",propName[:i],"in",obj)
		obj1=getProperty(propName[:i],obj,rules)
		return getProperty(propName[i+1:],obj1,rules)
	#check existing properties
	if propName in obj:
		return obj[propName]
	#try to generate using rules
	else:
		for rule in rules:
			if propName in rule.outputs and rule.canAct(obj,rules):
				rule.act(obj,rules)
				obj1=obj[propName]
				return obj1
	#fail
	raise AttributeError
	


class GrammarRule:
	def __init__(self,name,function):
		self.name=name
		self.function=function
		self.outputs=[name]
	def canAct(self,obj,rules):
		try:
			description=getProperty("description",obj,rules)
			return True
		except:
			return False
	def act(self,obj,rules):
		description=getProperty("description",obj,rules)
		obj1={"description":self.function(description)}
		obj[self.name]=obj1
		
		
def plural(s):
	if s[-1]=="s":
		return s+"es"
	elif s[-1]=="y":
		return s[:-1]+"ies"
	return s+"s"
	
def aAn(s):
	if s[0].lower() in "aeiou":
		return "an "+s
	return "a "+s
	
grammar=[GrammarRule("aAn",aAn),GrammarRule("plural",plural)]


#this code runs on import
import os
this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "data", "adventure.txt")
text=open(DATA_PATH).read()
adventureRules=getDescriptionRules(text)+grammar



	
	
