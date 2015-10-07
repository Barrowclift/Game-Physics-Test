from enum import Enum

class Actions(Enum):
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3

	SPACE = 4
	QUIT = 5

FULL_HEALTH = 100

PLAYER_BULLET_ACTION = {Actions.UP : True,
						Actions.DOWN : False,
						Actions.LEFT: False,
						Actions.RIGHT: False,

						Actions.SPACE: False,
						Actions.QUIT: False}