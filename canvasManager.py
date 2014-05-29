import globalVars
import windowManager
from tkinter import * # TODO Only import what I need, this is greedy

canvas = None

def setupCanvas():
	global canvas

	canvas = Canvas(windowManager.window,
					 width=windowManager.width,
					 height=windowManager.height,
					 highlightthickness=0,
					 background=windowManager.BACKGROUND_COLOR)
	canvas.pack(fill="both", expand=1) # Resize with window
	canvas.bind("<Configure>", windowManager.scaleWindowAndContents)