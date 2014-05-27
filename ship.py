import gameDisplay
import windowManager
import vector
from physics import Physics
from element import Element
from vector import Vector
from globalVars import Actions

class Ship(element):

	beginningYPosition = 

	def __init__(self, x, y, width, height, color):
		self.physics = Physics(x, y)
		self.width = width
		self.height = height
		self.color = color

		STARTING_ABSOLUTE_CENTER = (windowManager.STARTING_WIDTH / 2) - (STARTING_WIDTH / 2)

		self.canvasItem = gameDisplay.display.create_rectangle(self.physics.location.x,
															   self.physics.location.y,
															   self.physics.location.x+self.width,
															   self.physics.location.y+self.height,
															   fill=self.color)
	
STARTING_ABSOLUTE_CENTER = -1

STARTING_X = -1
STARTING_Y = -1
STARTING_DIRECTION = 0;

MAX_SPEED = 10
WEIGHT = 1.03
FLOOR_IT_SPEED = 0.9

CANVAS_ITEM = None

velocity = Vector(0, 0)
location = Vector(0, 0)
acceleration = Vector(0, 0)
width = STARTING_WIDTH
height = STARTING_HEIGHT
gapFromBottom = STARTING_GAP_FROM_BOTTOM

def setupShip():
	global STARTING_ABSOLUTE_CENTER, STARTING_X ,STARTING_Y, CANVAS_ITEM
	global location, width, height, gapFromBottom

	
	STARTING_X = STARTING_ABSOLUTE_CENTER
	STARTING_Y = windowManager.STARTING_HEIGHT - STARTING_GAP_FROM_BOTTOM

	CANVAS_ITEM = gameDisplay.display.create_rectangle(STARTING_X,
													   STARTING_Y,
													   STARTING_X+STARTING_WIDTH,
													   STARTING_Y+STARTING_HEIGHT,
													   fill=SHIP_COLOR,
													   tags=SHIP_COLOR_TAG)
	location = Vector(STARTING_X, STARTING_Y)
	width = STARTING_WIDTH
	height = STARTING_HEIGHT
	gapFromBottom = STARTING_GAP_FROM_BOTTOM

def scaleShipForWindowSize():
	global location, velocity, acceleration, width, height, gapFromBottom

	location.scale (windowManager.horizontalScale, windowManager.verticalScale)
	velocity.scale (windowManager.horizontalScale, windowManager.verticalScale)
	acceleration.scale (windowManager.horizontalScale, windowManager.verticalScale)
	width = width * windowManager.horizontalScale
	height = height * windowManager.verticalScale
	gapFromBottom = gapFromBottom * windowManager.verticalScale

	gameDisplay.display.coords(CANVAS_ITEM, x, y, x+width, y+height)

def resetShipForNewGame():
	global location, velocity, acceleration, width, height, gapFromBottom

	location = Vector(STARTING_X, STARTING_Y)
	velocity = Vector(0, 0)
	acceleration = Vector(0, 0)

	width = STARTING_WIDTH
	height = STARTING_HEIGHT
	gapFromBottom = STARTING_GAP_FROM_BOTTOM

	scaleShipForWindowSize()

def executeAction(requestedActions):
	global location, velocity, acceleration

	newLocationBasedOnActions = calculateNewLocationBasedOnActions(requestedActions)
	direction = vector.subtract(newLocationBasedOnActions, location)
	direction.normalize()

	direction.multiply(FLOOR_IT_SPEED)
	acceleration = direction;

	velocity.add(acceleration)
	velocity.limit(MAX_SPEED);
	velocity.stopIfSlowEnough();
	velocity.divide(WEIGHT)
	location.add(velocity)

	gameDisplay.display.coords(CANVAS_ITEM, location.x, location.y, location.x+width, location.y+height)

def calculateNewLocationBasedOnActions(requestedActions):
	global location

	newLocationBasedOnActions = location.getCopy()
	if requestedActions[Actions.UP]:
		newLocationBasedOnActions.y -= MAX_SPEED
	if requestedActions[Actions.DOWN]:
		newLocationBasedOnActions.y += MAX_SPEED
	if requestedActions[Actions.LEFT]:
		newLocationBasedOnActions.x -= MAX_SPEED
	if requestedActions[Actions.RIGHT]:
		newLocationBasedOnActions.x += MAX_SPEED

	return newLocationBasedOnActions