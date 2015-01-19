from sys import argv
import sys
import time

from random import randrange
import fighterClass
import battleClass

matrix = [["0" for i in range(15)] for j in range(15)]
mapString = ""
numTurns = 0
fighterFileOne = argv[1]
fighterFileTwo = argv[2]

txtFighterOne = open(fighterFileOne)
txtFighterTwo = open(fighterFileTwo)

fighterOne = fighterClass.fighter(txtFighterOne,str(sys.argv[1]))
fighterTwo = fighterClass.fighter(txtFighterTwo,str(sys.argv[2]))
print 'Fighters: ', fighterOne.name ,'VS', fighterTwo.name
battle = battleClass.battle(fighterOne,fighterTwo)

firstTurn = battle.start()
battle.fight(firstTurn)

death = False

while death != True:
	death = battle.attack()
	numTurns = numTurns + 1
	#time.sleep(1)
	
print "in ",numTurns

for i in range (0,15):
	for j in range(0,15):
		mapString = mapString+matrix[i][j]
	
	print mapString
	mapString = ""
	