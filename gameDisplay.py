import globalVars
import windowManager
from tkinter import * # TODO Only import what I need, this is greedy
# from code import interact

display = None

def setupDisplay():
	global display

	display = Canvas(windowManager.rootWindow,
					 width=windowManager.width,
					 height=windowManager.height,
					 highlightthickness=0,
					 background=windowManager.BACKGROUND_COLOR)
	display.pack(fill="both", expand=1) # Resize with window
	display.bind("<Configure>", scaleCanvasContents)

def updateObject(objectID, *newPoints):
	display.coords(objectID, newPoints)

def scaleCanvasContents(event):
	windowManager.updateScale(event)
	# interact()