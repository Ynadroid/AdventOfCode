# AdventOfCode Day7 Wire Class
import re

def createWire(name):
	wireNamePattern = re.compile('[a-z]{1,}')

	if not wireNamePattern.match(name):
		#print(name,'is an invalid wire name')
		return
	
	if name not in Wire.AllWires:
		newwire = Wire(name)
		#print('Created wire',newwire.name)
	# else:
		# print('Wire',name,'already registered')

class Wire:
	"""Represents a Wire"""
	
	AllWires = {}
	
	def __init__(self,_name):
		self.name = _name
		self.signal = None
		Wire.AllWires[self.name] = self
	
	def signalDefined(self):
		return (self.signal != None)
