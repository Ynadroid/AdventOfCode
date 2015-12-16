# Advent of Code Day 14 Reindeer class

class Reindeer:
	def __init__(self,_name,_speed,_speedtime,_resttime):
		self.name = _name
		self.speed = _speed
		self.speedtime = _speedtime
		self.resttime = _resttime
		
		self.speedtimeselpased = 0
		self.resttimeelapsed = 0
		self.distance = 0
	
	def __repr__(self):
		return self.name+' at '+str(self.distance)+' km'
		
	def __str__(self):
		return self.name+' at '+str(self.distance)+' km'
	
	def tick(self):
		if self.speedtimeselpased == self.speedtime:
			if self.resttimeelapsed == self.resttime:
				self.resttimeelapsed = 0
				self.speedtimeselpased = 0
			else:
				self.resttimeelapsed += 1
		
		if self.speedtimeselpased < self.speedtime:
			self.speedtimeselpased += 1
			self.distance += self.speed
		
