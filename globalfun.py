#-*- encoding: utf-8 -*-

def sanitize(data):
	""" returns better names for lists """
	escapes =["/",";","#","\n"]
	mess = ""
	lol = 0
	lbuffer = 0
	for cur in data:
		if cur == " " and lbuffer !=0:
			mess += "_"
		elif cur in escapes or cur ==" " and lbuffer ==0:
			lol +=1
		else:
			mess += cur
		lbuffer +=1
	return mess


