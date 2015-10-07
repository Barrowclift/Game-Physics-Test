import vector
from vector import Vector

class Physics:

	DEFAULT_MAX_SPEED = 10
	DEFAULT_WEIGHT = 1.03
	DEFAULT_FLOOR_IT_SPEED = 0.9

	ORIGINAL_MAX_SPEED = None
	maxSpeed = None
	ORIGINAL_WEIGHT = None
	weight = None
	ORIGINAL_FLOOR_IT_SPEED = None
	floorItSpeed = None

	ORIGINAL_LOCATION = None
	location = None
	ORIGINAL_VELOCITY = None
	velocity = None
	ORIGINAL_ACCELERATION = None
	acceleration = None

	def __init__(self, x, y):
		self.ORIGINAL_LOCATION = Vector(x, y)
		self.location = Vector(x, y)
		self.ORIGINAL_VELOCITY = Vector(0, 0)
		self.velocity = Vector(0, 0)
		self.ORIGINAL_ACCELERATION = Vector(0, 0)
		self.acceleration = Vector(0, 0)

		self.ORIGINAL_MAX_SPEED = Vector(self.DEFAULT_MAX_SPEED, self.DEFAULT_MAX_SPEED)
		self.maxSpeed = Vector(self.DEFAULT_MAX_SPEED, self.DEFAULT_MAX_SPEED)
		self.ORIGINAL_WEIGHT = Vector(self.DEFAULT_WEIGHT, self.DEFAULT_WEIGHT)
		self.weight = Vector(self.DEFAULT_WEIGHT, self.DEFAULT_WEIGHT)
		self.ORIGINAL_FLOOR_IT_SPEED = Vector(self.DEFAULT_FLOOR_IT_SPEED, self.DEFAULT_FLOOR_IT_SPEED)
		self.floorItSpeed = Vector(self.DEFAULT_FLOOR_IT_SPEED, self.DEFAULT_FLOOR_IT_SPEED)

	def scale(self, horizontalScale, verticalScale):
		self.location.scaleWithRespectTo(self.ORIGINAL_LOCATION, horizontalScale, verticalScale)
		self.velocity.scaleWithRespectTo(self.ORIGINAL_VELOCITY, horizontalScale, verticalScale)
		self.acceleration.scaleWithRespectTo(self.ORIGINAL_ACCELERATION, horizontalScale, verticalScale)

		self.maxSpeed.scaleWithRespectTo(self.ORIGINAL_MAX_SPEED, horizontalScale, verticalScale)
		"""
		Scaling physics SEEMS to work correctly the minute we stop scaling the
		weight as well. I'm sure the concept of why this makes sense is super
		simple but it alludes me at the moment. No matter, it seems to work,
		so I'll leave it be for now and check back later when I have other
		things to check besides just the ship...
		"""
		self.weight.scaleWithRespectTo(self.ORIGINAL_WEIGHT, horizontalScale, verticalScale)
		self.floorItSpeed.scaleWithRespectTo(self.ORIGINAL_FLOOR_IT_SPEED, horizontalScale, verticalScale)

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