import vector
from vector import Vector

class Physics:

	DEFAULT_MAX_SPEED = 10
	DEFAULT_WEIGHT = 1.03
	DEFAULT_FLOOR_IT_SPEED = 0.9

	maxSpeed = None
	weight = None
	floorItSpeed = None

	location = None
	velocity = None
	acceleration = None

	def __init__(self, x, y):
		self.location = Vector(x, y)
		self.velocity = Vector(0, 0)
		self.acceleration = Vector(0, 0)

		self.maxSpeed = Vector(self.DEFAULT_MAX_SPEED, self.DEFAULT_MAX_SPEED)
		self.weight = Vector(self.DEFAULT_WEIGHT, self.DEFAULT_WEIGHT)
		self.floorItSpeed = Vector(self.DEFAULT_FLOOR_IT_SPEED, self.DEFAULT_FLOOR_IT_SPEED)

	def scale(self, horizontalScale, verticalScale):
		self.location.scale(horizontalScale, verticalScale)
		self.velocity.scale(horizontalScale, verticalScale)
		self.acceleration.scale(horizontalScale, verticalScale)

		self.maxSpeed.scale(horizontalScale, verticalScale)
		"""
		Scaling physics SEEMS to work correctly the minute we stop scaling the
		weight as well. I'm sure the concept of why this makes sense is super
		simple but it alludes me at the moment. No matter, it seems to work,
		so I'll leave it be for now and check back later when I have other
		things to check besides just the ship...
		"""
		# self.weight.scale(horizontalScale, verticalScale)
		self.floorItSpeed.scale(horizontalScale, verticalScale)

	def updateForNewLocation(self, newLocationBasedOnActions):
		direction = vector.subtract(newLocationBasedOnActions, self.location)
		direction.normalize()

		direction.multiply(self.floorItSpeed)
		self.acceleration = direction;

		self.velocity.add(self.acceleration)
		self.velocity.limit(self.maxSpeed);
		self.velocity.stopIfSlowEnough();
		self.velocity.divideByVector(vector=self.weight)
		self.location.add(self.velocity)