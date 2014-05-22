import globalVars
import windowManager
import ship
from globalVars import Actions
from enum import Enum

GAME_SLEEP_TIME = 17 # 1000 milliseconds / 60 frames per second

class State(Enum):
	WAITING = 0
	PLAYING = 1
	GAME_OVER = 2

state = State.WAITING
actionsForCurrentTick = {Actions.UP : False,
						 Actions.DOWN : False,
						 Actions.LEFT: False,
						 Actions.RIGHT: False,

						 Actions.SPACE: False,
						 Actions.QUIT: False}

def setupGame():
	ship.setupShip()

def gameLoop():
	if state == State.WAITING:
		waitingStep()
	elif state == State.PLAYING:
		playingStep()
	elif state == State.GAME_OVER:
		gameOverStep()

	windowManager.rootWindow.after(GAME_SLEEP_TIME, gameLoop)

def waitingStep():
	if actionsForCurrentTick[Actions.SPACE]:
		global state
		state = State.PLAYING

def playingStep():
	# if isPlayerDead():
	# 	global state
	# 	state = State.GAME_OVER
	# 	return

	ship.executeAction(actionsForCurrentTick)
	# TODO Update wall data
	# TODO Update display (Needed???????)

def gameOverStep():
	print ("Game over")
	# TODO Do animation step
	# TODO Reset everything on last animation step

def resetVariablesForNewGame():
	global actionsForCurrentTick
	clearInputForNextTick()
	# TODO add them all

def clearInputForNextTick():
	global actionsForCurrentTick
	actionsForCurrentTick[Actions.UP] = False
	actionsForCurrentTick[Actions.DOWN] = False
	actionsForCurrentTick[Actions.LEFT] = False
	actionsForCurrentTick[Actions.RIGHT] = False
	actionsForCurrentTick[Actions.SPACE] = False
	actionsForCurrentTick[Actions.QUIT] = False

def isPlayerDead():
	print ("Checking player status...")
	# TODO check coordinates

def scaleAllResources():
	ship.scaleShipForWindowSize()