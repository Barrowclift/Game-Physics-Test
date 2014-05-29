from math import sqrt

class Vector:
	x = 0
	y = 0

	def __init__(self, x, y,):
		self.x = x
		self.y = y

	def add(self, vector):
		self.x = self.x + vector.x
		self.y = self.y + vector.y

	def subtract(self, vector):
		self.x = self.x - vector.x
		self.y = self.y - vector.y

	def multiply(self, vector):
		self.x = self.x * vector.x
		self.y = self.y * vector.y

	# Got to be a better, more Pythonic way to do this...
	def divideByVector(self, vector):
		self.x = self.x / vector.x
		self.y = self.y / vector.y

	def divideByValue(self, value=1):
		self.x = self.x / value
		self.y = self.y / value

	def magnitude(self):
		# Pythagorean Theorem c^2 = a^2 + b^2
		return sqrt(self.x*self.x + self.y*self.y)

	def normalize(self):
		magnitude = self.magnitude()
		if magnitude > 0:
			self.divideByValue(value=magnitude)

	def limit(self, maxAccelerationVector):
		if (self.magnitude() > maxAccelerationVector.magnitude()):
			self.normalize()
			self.multiply(maxAccelerationVector)

	def stopIfSlowEnough(self):
		if (self.magnitude() < 0.15):
			nothingVector = Vector(0, 0)
			self.multiply(nothingVector)

	def scale(self, horizontalScale, verticalScale):
		self.x = self.x * horizontalScale
		self.y = self.y * verticalScale

	def getCopy(self):
		return Vector(self.x, self.y)

def add(vector1, vector2):
	newVector = Vector(vector1.x, vector1.y)
	newVector.add(vector2)
	return newVector

def subtract(vector1, vector2):
	newVector = Vector(vector1.x, vector1.y)
	newVector.subtract(vector2)
	return newVector