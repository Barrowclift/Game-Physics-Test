from globalVars import Actions
import windowManager
import gameManager
import sys

KEYS = ["Up",
		"Down",
		"Left",
		"Right",
		
		"space",
		"Escape"]

KEYS_TO_ACTIONS = {KEYS[0] : Actions.UP,
				   KEYS[1] : Actions.DOWN,
				   KEYS[2] : Actions.LEFT,
				   KEYS[3] : Actions.RIGHT,

				   KEYS[4] : Actions.SPACE,
				   KEYS[5] : Actions.QUIT}

def setupKeyBindings():
	for key in KEYS:
		windowManager.window.bind("<KeyPress-%s>" % key, keyPress)
		windowManager.window.bind("<KeyRelease-%s>" % key, keyRelease)

def keyPress(event):
	eventAction = KEYS_TO_ACTIONS.get(event.keysym)
	if eventAction == Actions.QUIT:
		windowManager.cleanupForQuit()
		sys.exit(0)
	gameManager.playerActionsForCurrentTick[eventAction] = True

def keyRelease(event):
	eventAction = KEYS_TO_ACTIONS.get(event.keysym)
	gameManager.playerActionsForCurrentTick[eventAction] = False