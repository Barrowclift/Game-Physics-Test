import canvasManager
import windowManager
from element import Element
from vector import Vector
from physics import Physics
from rgb import RGB
from bullet import Bullet

class StandardBullet(Bullet):

	def __init__(self, x, y):
		self.ORIGINAL_WIDTH = 2 * windowManager.horizontalScale
		self.width = 2 * windowManager.horizontalScale
		self.ORIGINAL_HEIGHT = 15 * windowManager.verticalScale
		self.height = 15 * windowManager.verticalScale
		self.ORIGINAL_X = x - (self.width / 2)
		self.startX = x - (self.width / 2)
		self.ORIGINAL_Y = y
		self.startY = y
		self.physics = Physics(self.startX, self.startY)
		self.physics.maxSpeed = Vector(15*windowManager.horizontalScale, 15*windowManager.verticalScale)
		self.physics.weight = Vector(0, 0)
		self.physics.floorItSpeed = Vector(15*windowManager.horizontalScale, 15*windowManager.verticalScale)
		self.color = RGB(255, 0, 255) # Pink
		self.canvasItem = canvasManager.canvas.create_rectangle(self.physics.location.x,
																self.physics.location.y,
																self.physics.location.x+self.width,
																self.physics.location.y+self.height,
																fill=self.color.hex())