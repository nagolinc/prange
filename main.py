from parseStory import expandDescription,adventureRules,getProperty

import sys

if __name__=="__main__":
	
	if len(sys.argv)>1:
		n=int(sys.argv[2])
	else:
		n=100

	event={"name":"event"}
	
	for i in range(n):
		s=expandDescription({"name":"event"},adventureRules)
		print s
		event=getProperty("event",event,adventureRules)
	





