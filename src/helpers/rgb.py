class RGB:
	r = 0
	g = 0
	b = 0

	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b

	def hex(self):
		return '#%02x%02x%02x' % (self.r, self.g, self.b)