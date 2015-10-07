from abc import ABCMeta
from abc import abstractmethod
from globalVars import Actions
from physics import Physics

class Element(object):
	__metaclass__ = ABCMeta

	color = ""
	ORIGINAL_WIDTH = 0
	width = 0
	ORIGINAL_HEIGHT = 0
	height = 0

	ORIGINAL_X = 0
	startX = 0
	ORIGINAL_Y = 0
	startY = 0

	canvasItem = None
	physics = None

	def resetElementForNewGame(self):
		self.physics = Physics(self.startX, self.startY)
		self.drawShip()

	def scale(self, horizontalScale, verticalScale):
		self.physics.scale(horizontalScale, verticalScale)
		self.width = self.ORIGINAL_WIDTH * horizontalScale
		self.height = self.ORIGINAL_HEIGHT * verticalScale
		self.startX = self.ORIGINAL_X * horizontalScale
		self.startY = self.ORIGINAL_Y * verticalScale
		self.drawElement()

	def executeAction(self, requestedActions):
		newLocationBasedOnActions = self.calculateNewLocationBasedOnActions(requestedActions)
		self.physics.updateForNewLocation(newLocationBasedOnActions)
		self.drawElement()

	def calculateNewLocationBasedOnActions(self, requestedActions):
		newLocationBasedOnActions = self.physics.location.getCopy()
		if requestedActions[Actions.UP]:
			newLocationBasedOnActions.y -= self.physics.maxSpeed.y
		if requestedActions[Actions.DOWN]:
			newLocationBasedOnActions.y += self.physics.maxSpeed.y
		if requestedActions[Actions.LEFT]:
			newLocationBasedOnActions.x -= self.physics.maxSpeed.x
		if requestedActions[Actions.RIGHT]:
			newLocationBasedOnActions.x += self.physics.maxSpeed.x

		return newLocationBasedOnActions

	def drawElement(self):
		pass