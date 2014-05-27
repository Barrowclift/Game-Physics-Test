from abc import ABCMeta
from abc import abstractmethod
from globalVars import Actions
from physics import Physics

class Element(object):
	__metaclass__ = ABCMeta

	canvasItem = None
	color = ""

	physics = None
	width = 0
	height = 0

	@abstractmethod
	def scaleForWindowSize(self):
		physics.scaleForWindowSize()
		pass

	@abstractmethod
	def reset(self):
		pass

	def executeAction(self, requestedActions):
		newLocationBasedOnActions = calculateNewLocationBasedOnActions(requestedActions)
		self.physics.update(newLocationBasedOnActions)
		gameDisplay.display.coords(self.canvasItem,
								   self.physics.location.x,
								   self.physics.location.y,
								   self.physics.location.x+self.width,
								   self.physics.location.y+self.height)

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