import windowManager
import globalVars
from ship import Ship
from globalVars import Actions
from enum import Enum

GAME_SLEEP_TIME = 17 # 1000 milliseconds / 60 frames per second
BULLET_WAIT_TIME = 10
curBulletWaitTime = 0

class State(Enum):
	WAITING = 0
	PLAYING = 1
	GAME_OVER = 2

state = State.WAITING
playerActionsForCurrentTick = {Actions.UP : False,
							   Actions.DOWN : False,
							   Actions.LEFT: False,
							   Actions.RIGHT: False,

							   Actions.SPACE: False,
							   Actions.QUIT: False}
ship = None
bullets = []

def setupGame():
	global ship
	ship = Ship(windowManager.horizontalCenter, windowManager.height)
	bullets = []

def gameLoop():
	if state == State.WAITING:
		waitingStep()
	elif state == State.PLAYING:
		playingStep()
	elif state == State.GAME_OVER:
		gameOverStep()

	windowManager.window.after(GAME_SLEEP_TIME, gameLoop)

def waitingStep():
	if playerActionsForCurrentTick[Actions.SPACE]:
		global state
		state = State.PLAYING

def playingStep():
	# if isPlayerDead():
	# 	global state
	# 	state = State.GAME_OVER
	# 	return

	ship.executeAction(playerActionsForCurrentTick)
	for bullet in bullets:
		bullet.executeAction(bullet.bulletPath)
		if (itemOffScreen(bullet)):
			bullets.remove(bullet)
	# TODO Update wall data

def gameOverStep():
	print("Game over")
	# TODO Do animation step
	# TODO Reset everything on last animation step

def resetVariablesForNewGame():
	global playerActionsForCurrentTick
	clearInputForNextTick()
	# TODO add them all

def clearInputForNextTick():
	global playerActionsForCurrentTick
	playerActionsForCurrentTick[Actions.UP] = False
	playerActionsForCurrentTick[Actions.DOWN] = False
	playerActionsForCurrentTick[Actions.LEFT] = False
	playerActionsForCurrentTick[Actions.RIGHT] = False
	playerActionsForCurrentTick[Actions.SPACE] = False
	playerActionsForCurrentTick[Actions.QUIT] = False

def isPlayerDead():
	print("Checking player status...")
	# TODO check coordinates

def scaleAllResources(horizontalScale, verticalScale):
	ship.scale(horizontalScale, verticalScale)
	for bullet in bullets:
		bullet.scale(horizontalScale, verticalScale)

def itemOffScreen(item):
	return item.offScreen()