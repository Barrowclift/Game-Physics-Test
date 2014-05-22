import windowManager

class Physics:

	DEFAULT_MAX_SPEED = 10
	DEFAULT_WEIGHT = 1.03
	DEFAULT_FLOOR_IT_SPEED = 0.9

	DEFAULT_START_X = windowManager.horizontalCenter
	DEFAULT_START_Y = windowManager.verticalCenter

	maxSpeed = 0
	weight = 0
	floorItSpeed = 0

	location = None
	velocity = None
	acceleration = None

	@classmethod
	def fromDefaults(cls):
		return cls(cls.DEFAULT_START_X, cls.DEFAULT_START_Y)

	def __init__(self, x, y):
		self.maxSpeed = self.DEFAULT_MAX_SPEED
		self.weight = self.DEFAULT_WEIGHT
		self.floorItSpeed = self.DEFAULT_FLOOR_IT_SPEED

		self.location = Vector(x, y)
		self.velocity = Vector(0, 0)
		self.acceleration = Vector(0, 0)

	def scaleForWindowSize(self):
		self.location.scale (windowManager.horizontalScale, windowManager.verticalScale)
		self.velocity.scale (windowManager.horizontalScale, windowManager.verticalScale)
		self.acceleration.scale (windowManager.horizontalScale, windowManager.verticalScale)

	def update(self, newLocationBasedOnActions):
		direction = vector.subtract(newLocationBasedOnActions, self.location)
		direction.normalize()

		direction.multiply(self.floorItSpeed)
		self.acceleration = direction;

		self.velocity.add(self.acceleration)
		self.velocity.limit(maxSpeed);
		self.velocity.stopIfSlowEnough();
		self.velocity.divide(self.weight)
		self.location.add(self.velocity)