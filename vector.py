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

	def multiply(self, n):
		self.x = self.x * n
		self.y = self.y * n

	def divide(self, n):
		self.x = self.x / n
		self.y = self.y / n

	def magnitude(self):
		# Pythagorean Theorem c^2 = a^2 + b^2
		return sqrt(self.x*self.x + self.y*self.y)

	def normalize(self):
		magnitude = self.magnitude()
		if magnitude > 0:
			self.divide(magnitude)

	def limit(self, maxAcceleration):
		if (self.magnitude() > maxAcceleration):
			self.normalize()
			self.multiply(maxAcceleration)

	def stopIfSlowEnough(self):
		if (self.magnitude() < 0.15):
			self.multiply(0)

	def scale(self, horizontal, vertical):
		self.x = self.x * horizontal
		self.y = self.y * vertical

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