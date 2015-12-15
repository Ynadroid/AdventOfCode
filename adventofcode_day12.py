# Advent of Code Day 12

import json

def analyzeObject(object, ignorewhatisred = False):
	count = 0
	if type(object) is dict:
		for k,v in object.items():
			ret = analyzeObject(v, True)
			if ret != None:
				count += ret
			else:
				print("Red element")
				return 0
	elif type(object) is list:
		for v in object:
			count += analyzeObject(v, False)
	elif type(object) is int:
		#print("INT:",object)
		count += object
	elif type(object) is str and ignorewhatisred and object == "red":
		return None
	return count

def countInJson(jsoncontent):
	totalcount = 0
	for k,v in jsoncontent.items():
		totalcount += analyzeObject(v)
		print('Inter count:',totalcount)
	return totalcount

with open('adventofcode_day12_input.txt') as f:
	input = [line.strip() for line in f]

loadedjson = json.loads(input[0])

# print(json.dumps(loadedjson, sort_keys = True, indent=4, separators=(',',': ')))

print(countInJson(loadedjson))
