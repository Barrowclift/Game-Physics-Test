import windowManager
import canvasManager
from globalVars import Actions
from element import Element

class Bullet(Element):

	bulletPath = None

	# Override
	def scale(self, horizontalScale, verticalScale):
		super(Bullet, self).scale(horizontalScale, verticalScale)
		print(self.width)

	# Override
	def drawElement(self):
		canvasManager.canvas.coords(self.canvasItem,
									self.physics.location.x,
									self.physics.location.y,
									self.physics.location.x+self.width,
									self.physics.location.y+self.height)

	"""
	Note to developers, not smart to ignore drawing bullets that
	are anything BUT north of the top horizontal line of the game

	Basically if a bullet somehow gets beyond the width or below
	the bottom of the window it will cease to be updated. This is
	particularly bad if the player increases the window size as
	a stagnant bullet will then be visible and not go away.
	"""
	def offScreen(self):
		if self.physics.location.y+self.height < 0:
			return True
		else:
			return False