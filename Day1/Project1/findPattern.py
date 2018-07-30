import re
a = "Hi, My name is anjali hore"
b= "no"
myobject = re.search(b,a)
if myobject:
	print "match found"
else:
	print "no match"
