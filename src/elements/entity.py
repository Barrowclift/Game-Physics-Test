import globalVars
from element import Element
from globalVars import Actions

class Entity(Element):

	health = globalVars.FULL_HEALTH

	def adjustHealthBy(self, p):
		self.health = self.health + p
		if self.health > globalVars.FULL_HEALTH:
			self.health = globalVars.FULL_HEALTH
		ratio = self.health / globalVars.FULL_HEALTH

		self.color.r = 255 * (1 - ratio)
		self.color.g = 255 * ratio