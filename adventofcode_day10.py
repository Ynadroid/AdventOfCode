# Advent of Code Day 10


from itertools import groupby
def lookandsay(number):
	return ''.join( str(len(list(g))) + k for k,g in groupby(number) )

numberstring = '3113322113'
for i in range(50):
	print(i, len(numberstring))
	numberstring = lookandsay(numberstring)
	
print(len(numberstring))
