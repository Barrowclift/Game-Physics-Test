import canvasManager
import gameManager
import vector
import globalVars
from standardBullet import StandardBullet
from physics import Physics
from entity import Entity
from vector import Vector
from rgb import RGB
from globalVars import Actions

class Ship(Entity):

	halfShipWidth = -1
	bulletPath = {Actions.UP : True,
				  Actions.DOWN : False,
				  Actions.LEFT: False,
				  Actions.RIGHT: False,

				  Actions.SPACE: False,
				  Actions.QUIT: False}
	bulletTimer = 0
	BULLET_WAIT_TIME = 5
	ORIGINAL_HALF_SHIP_WIDTH = 0 

	def __init__(self, x, y):
		self.ORIGINAL_WIDTH = 20
		self.width = 20
		self.ORIGINAL_HEIGHT = 20
		self.height = 20
		self.ORIGINAL_HALF_SHIP_WIDTH = self.width / 2
		self.halfShipWidth = self.width / 2
		self.ORIGINAL_X = x - self.halfShipWidth
		self.startX = x - self.halfShipWidth
		self.ORIGINAL_Y = y - 40
		self.startY = y - 40
		self.physics = Physics(self.startX, self.startY)
		self.color = RGB(0, 255, 0) # Green
		self.adjustHealthBy(0)
		self.canvasItem = canvasManager.canvas.create_polygon(self.physics.location.x,
															  self.physics.location.y,
															  self.physics.location.x+self.halfShipWidth,
															  self.physics.location.y-self.height,
															  self.physics.location.x+self.width,
															  self.physics.location.y,
															  fill=self.color.hex())

	# Override
	def calculateNewLocationBasedOnActions(self, requestedActions):
		if self.bulletTimer < self.BULLET_WAIT_TIME:
			self.bulletTimer += 1
		if requestedActions[Actions.SPACE]:
			if self.bulletTimer >= self.BULLET_WAIT_TIME:
				newBullet = StandardBullet(self.physics.location.x+self.halfShipWidth, self.physics.location.y-self.height)
				newBullet.bulletPath = self.bulletPath
				gameManager.bullets.append (newBullet)
				self.bulletTimer = 0
		return super(Ship, self).calculateNewLocationBasedOnActions(requestedActions)

	# Override
	def scale(self, horizontalScale, verticalScale):
		self.halfShipWidth = self.ORIGINAL_HALF_SHIP_WIDTH * horizontalScale
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