from abc import ABCMeta
from abc import abstractmethod
from globalVars import Actions
from physics import Physics

class Element(object):
	__metaclass__ = ABCMeta

	color = ""
	width = 0
	height = 0

	startX = 0
	startY = 0

	canvasItem = None
	physics = None

	def resetElementForNewGame(self):
		self.physics = Physics(self.startX, self.startY)
		self.drawShip()

	def scale(self, horizontalScale, verticalScale):
		self.physics.scale(horizontalScale, verticalScale)
		self.width = self.width * horizontalScale
		self.height = self.height * verticalScale
		self.startX = self.startX * horizontalScale
		self.startY = self.startY * verticalScale
		self.drawElement()

	def executeAction(self, requestedActions):
		newLocationBasedOnActions = self.calculateNewLocationBasedOnActions(requestedActions)
		self.physics.updateForNewLocation(newLocationBasedOnActions)
		self.drawElement()

	def calculateNewLocationBasedOnActions(self, requestedActions):
		newLocationBasedOnActions = self.physics.location.getCopy()
		if requestedActions[Actions.UP]:
			newLocationBasedOnActions.y -= self.physics.maxSpeed
		if requestedActions[Actions.DOWN]:
			newLocationBasedOnActions.y += self.physics.maxSpeed
		if requestedActions[Actions.LEFT]:
			newLocationBasedOnActions.x -= self.physics.maxSpeed
		if requestedActions[Actions.RIGHT]:
			newLocationBasedOnActions.x += self.physics.maxSpeed

		return newLocationBasedOnActions

	def drawElement():
		pass