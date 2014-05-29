import canvasManager
import vector
from physics import Physics
from element import Element
from vector import Vector
from globalVars import Actions

class Ship(Element):

	halfShipWidth = -1
	startGapFromBottom = 40

	startX = -1
	startY = -1

	def __init__(self, color, x, y):
		self.width = 20
		self.height = 20
		self.halfShipWidth = self.width / 2
		self.startX = x - self.halfShipWidth
		self.startY = y - 40
		self.physics = Physics(self.startX, self.startY)
		self.color = color

		self.canvasItem = canvasManager.canvas.create_polygon(self.physics.location.x,
															  self.physics.location.y,
															  self.physics.location.x+self.halfShipWidth,
															  self.physics.location.y-self.height,
															  self.physics.location.x+self.width,
															  self.physics.location.y,
															  fill=self.color)

	# Override
	def scale(self, horizontalScale, verticalScale):
		self.startGapFromBottom = self.startGapFromBottom * verticalScale
		self.halfShipWidth = self.halfShipWidth * horizontalScale
		super(Ship, self).scale(horizontalScale, verticalScale)

	# Override
	def drawElement(self):
		canvasManager.canvas.coords(self.canvasItem,
									self.physics.location.x,
									self.physics.location.y,
									self.physics.location.x+self.halfShipWidth,
									self.physics.location.y-self.height,
									self.physics.location.x+self.width,
									self.physics.location.y)