from random import randrange

class fighter():

	def __init__(self,file,name):
		a,b = name.split(".")
		self.name = a
		self.strength = int(file.readline())
		self.agility = int(file.readline())
		self.toughness = int(file.readline())
		self.initiative = int(file.readline())
		self.health = int(file.readline())
		self.turn = 0
		self.damage = 0
		self.mitigated = 0
		self.dodged = 0

	
	def takeDamage(self,damage):
		if (self.agility + randrange(8)) < 10:
			self.mitigated = self.toughness - randrange(5)
			print self.name, "mitigated",self.mitigated
			self.damage = (damage + randrange(3) - self.mitigated)				
			self.health -= self.damage
			print self.name,"had ",self.damage,"damage done:"
			self.damage = 0
			if self.health <= 0:
				print self.name , "is dead"
				return True
		else:
			self.dodged = self.dodged + 1
			print self.name , "dodged the attack",self.dodged
	
	
	def setTurn(self,tturn):
		turn = tturn
