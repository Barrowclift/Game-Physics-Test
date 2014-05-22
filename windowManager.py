import globalVars
import gameManager
import gameDisplay
from globalVars import Actions
from tkinter import * # TODO Only import what I need, this is greedy

TITLE = "Trench Wars"
MIN_WIDTH = 500
MIN_HEIGHT = 500
STARTING_WIDTH = 500
STARTING_HEIGHT = 500
BACKGROUND_COLOR = "black"

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

rootWindow = None
width = STARTING_WIDTH
height = STARTING_HEIGHT
scale = 1

def init():
	setupWindow()
	setupKeyBindings()
	gameDisplay.setupDisplay()
	gameManager.setupGame()

def setupWindow():
	global rootWindow

	rootWindow = Tk()
	rootWindow.protocol("WM_DELETE_WINDOW", rootWindow.quit())
	rootWindow.wm_title(TITLE)
	# Window aspect ratio support:
	#   OS X..........YES
	#   Windows	7.....NO
	rootWindow.wm_aspect(1, 1, 1, 1)
	rootWindow.minsize(MIN_WIDTH,
					   MIN_HEIGHT)
	rootWindow.configure(background=BACKGROUND_COLOR)
	# rootWindow.resizable(0,0) # Not resizable

def setupKeyBindings():
	for key in KEYS:
		rootWindow.bind("<KeyPress-%s>" % key, keyPress)
		rootWindow.bind("<KeyRelease-%s>" % key, keyRelease)

def keyPress(event):
	eventAction = KEYS_TO_ACTIONS.get(event.keysym)
	if eventAction == Actions.QUIT:
		cleanupForQuit()
		sys.exit(0)
	gameManager.actionsForCurrentTick[eventAction] = True

def keyRelease(event):
	eventAction = KEYS_TO_ACTIONS.get(event.keysym)
	gameManager.actionsForCurrentTick[eventAction] = False

def run():
	# Remember, mainloop() is a blocking call that freezes the flow of
	# logic here until the user closes the window. This is why we have our
	# game update logic in it's own thread.
	# 
	# Once this returns control back to us, that means the user closed the
	# window and we should clean up anything that needs it.
	rootWindow.after(gameManager.GAME_SLEEP_TIME, gameManager.gameLoop)
	rootWindow.mainloop()

	cleanupForQuit()

def updateScale(event):
	global horizontalScale, verticalScale, width, height
	horizontalScale = event.width / width
	verticalScale = event.height / height
	width = event.width
	height = event.height
	
	gameManager.scaleAllResources()

def cleanupForQuit():
	rootWindow.quit()
	# TODO Do I need to cleaup more? Make sure