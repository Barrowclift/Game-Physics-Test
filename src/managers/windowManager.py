import gameManager
import inputManager
import canvasManager
from tkinter import * # TODO Only import what I need, this is greedy

"""
windowManager.py Developer Notes:

	Contraining window aspect ratio support (as of Python 3.4.0):
	- Windows 7...NO
	- OS X........YES
"""

TITLE = "Trench Wars"
BACKGROUND_COLOR = "black"
MIN_WIDTH = 500
MIN_HEIGHT = 500
STARTING_WIDTH = 500
STARTING_HEIGHT = 500

window = None
width = STARTING_WIDTH
height = STARTING_HEIGHT
horizontalCenter = -1
verticalCenter = -1
horizontalScale = 1
verticalScale = 1

def init():
	setupWindow()
	inputManager.setupKeyBindings()
	canvasManager.setupCanvas()
	gameManager.setupGame()

def setupWindow():
	global window, horizontalCenter, verticalCenter

	window = Tk()
	window.protocol("WM_DELETE_WINDOW", window.quit())
	window.wm_title(TITLE)
	# "Sublime Text" fullscreen
	# window.wm_attributes('-fullscreen', 1)

	# Borderless window
	# window.overrideredirect(True)

	# Simply maxing out the window to fit the screen (without "Sublime Text" fullscreen). Respects aspect ratio.
	# window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
	window.wm_aspect(1, 1, 1, 1) # See developer note above
	window.minsize(MIN_WIDTH,
				   MIN_HEIGHT)
	window.configure(background=BACKGROUND_COLOR)

	horizontalCenter = width / 2
	verticalCenter = height / 2

def run():
	"""
	Remember, mainloop() is a blocking call that freezes the flow of logic
	here until the user closes the window.

	This is why we have our game update logic in it's own thread. Once this
	returns control back to us, that means the user closed the window and we
	should clean up anything that needs it.
	"""
	window.after(gameManager.GAME_SLEEP_TIME, gameManager.gameLoop)
	window.mainloop()

	cleanupForQuit()

def scaleWindowAndAllResources(event):
	global horizontalScale, verticalScale, horizontalCenter, verticalCenter, width, height
	horizontalScale = event.width / STARTING_WIDTH
	verticalScale = event.height / STARTING_HEIGHT
	horizontalCenter = width / 2
	verticalCenter = height / 2
	width = event.width
	height = event.height
	
	gameManager.scaleAllResources(horizontalScale, verticalScale)

def cleanupForQuit():
	window.quit()
	# TODO Do I need to cleaup more? Make sure