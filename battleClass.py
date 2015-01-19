import fighterClass

class battle():

	def __init__(self,fighterOne,fighterTwo):
		self.fighterOne = fighterOne
		self.fighterTwo = fighterTwo
		
	def fight(self,order):
		if order == 1:
			self.fighterOne.setTurn(order)
			print self.fighterOne.name ," goes first"
		else:
			self.fighterTwo.setTurn(order)
			print self.fighterTwo.name ," goes first"
	
		
	def start(self):
	
		def checkInitiative():
			if self.fighterOne.initiative > self.fighterTwo.initiative:
				return 1
			else:
				return 2
		
		print "OK"
		return checkInitiative()
		
	def attack(self):
		if self.fighterOne.turn > self.fighterTwo.turn:
			if self.fighterTwo.takeDamage(self.fighterOne.strength) != True:
				return self.fighterOne.takeDamage(self.fighterTwo.strength)
			else:
				return True
		else:
			if self.fighterOne.takeDamage(self.fighterTwo.strength) != True:
				return self.fighterTwo.takeDamage(self.fighterOne.strength)
			else:
				return True
				
		return False
		
	
		
		
