# Advent of Code Day 19

import re

molecule = ''
replacementRules = []
possibleOriginElements = set()

replacementPattern = re.compile('(.*) => (.*)')
def registerInput(input):
	global molecule
	
	for inp in input:
		matches = replacementPattern.match(inp)
		if matches:
			origin = matches.group(1)
			replacementRules.append((origin,matches.group(2)))
			if origin not in possibleOriginElements:
				possibleOriginElements.add(origin)
		else:
			print('input:#'+inp+'#')
			if inp != '':
				print('mol')
				molecule = inp

def splitMolecule(mol):
	splitted = []
	pos = 0
	while pos < len(mol):
		atom = ''
		if pos < len(mol)-1:
			if str(mol[pos+1]).islower():
				atom = mol[pos:pos+2]
				pos += 2
				splitted.append(atom)
				continue
		atom = mol[pos]
		pos += 1
		splitted.append(atom)
	return splitted

def makeNewMolecule(upToPos,replaceAtom):
	prefix = splittedMolecule[:upToPos]
	prefix.append(replaceAtom)
	postfix = splittedMolecule[upToPos+1:]
	
	print(upToPos,'pre',prefix)
	print(upToPos,'pos',postfix)
	
	return prefix+postfix

def makeMoleculeStr(mollist):
	mol = ''
	for atom in mollist:
		mol += atom
	return mol

with open('aoc_day19_input.txt') as f:
# with open('aoc_day19_test_input.txt') as f:
	input = [line.strip() for line in f]

registerInput(input)

print(replacementRules)
print(possibleOriginElements)
print(molecule)

splittedMolecule = splitMolecule(molecule)
replacedMolecule = set()

posInMol = 0
for atom in splittedMolecule:
	replaced = False
	if atom in possibleOriginElements:
		for rule in replacementRules:
			if rule[0] == atom:
				newmol = makeMoleculeStr(makeNewMolecule(posInMol,rule[1]))
				if newmol not in replacedMolecule:
					replacedMolecule.add(newmol)
	posInMol += 1

print(replacedMolecule)

print('It seems there are',len(replacedMolecule),'different molecules')

