import vector
from vector import Vector

class Physics:

	maxSpeed = 10
	weight = 1.03
	floorItSpeed = 0.9

	location = None
	velocity = None
	acceleration = None

	def __init__(self, x, y):
		self.location = Vector(x, y)
		self.velocity = Vector(0, 0)
		self.acceleration = Vector(0, 0)

	def scaleForWindowSize(self, horizontalScale, verticalScale):
		self.location.scale (horizontalScale, verticalScale)
		self.velocity.scale (horizontalScale, verticalScale)
		self.acceleration.scale (horizontalScale, verticalScale)

	def updateForNewLocation(self, newLocationBasedOnActions):
		direction = vector.subtract(newLocationBasedOnActions, self.location)
		direction.normalize()

		direction.multiply(self.floorItSpeed)
		self.acceleration = direction;

		self.velocity.add(self.acceleration)
		self.velocity.limit(self.maxSpeed);
		self.velocity.stopIfSlowEnough();
		self.velocity.divide(self.weight)
		self.location.add(self.velocity)