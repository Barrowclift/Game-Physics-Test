import canvasManager
import windowManager
import vector
from physics import Physics
from element import Element
from vector import Vector
from globalVars import Actions

class Ship(Element):

	color = ""
	width = 20
	height = 20

	halfShipWidth = width / 2
	startGapFromBottom = 40

	startX = windowManager.width - halfShipWidth
	startY = windowManager.height - 40

	canvasItem = None
	physics = None

	def __init__(self, color):
		self.physics = Physics(self.startX, self.startY)
		self.color = color

		self.canvasItem = canvasManager.canvas.create_polygon(self.physics.location.x,
															 self.physics.location.y,
															 self.physics.location.x+self.halfShipWidth,
															 self.physics.location.y-self.height,
															 self.physics.location.x+self.width,
															 self.physics.location.y,
															 fill=self.color)

	def scaleForWindowSize(self):
		self.startGapFromBottom = self.startGapFromBottom * windowManager.verticalScale
		self.halfShipWidth = self.halfShipWidth * windowManager.horizontalScale
		super(Ship, self).scaleForWindowSize()

	def drawElement(self):
		canvasManager.canvas.coords(self.canvasItem,
									 self.physics.location.x,
									 self.physics.location.y,
									 self.physics.location.x+self.halfShipWidth,
									 self.physics.location.y-self.height,
									 self.physics.location.x+self.width,
									 self.physics.location.y)