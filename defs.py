from enum import Enum
import math

DISPLAY_W = 1200
DISPLAY_H = 600
GAME_W = 600
GAME_H = 600
FPS = 30
START_ENERGY = 10
DIAG = 0.70710678118
POP_SIZE = 50
MUTATION_CHANCE = 0.2
GENE_MUTATION_CHANCE = 0.2
PI = 3.1415
MAX_FOOD_SIZE = 5

class Dir(Enum):
    W = (-1, 0)
    E = (1, 0)
    N = (0, -1)
    S = (0, 1)
    NW = (-DIAG, -DIAG)
    NE = (DIAG, -DIAG)
    SE = (DIAG, DIAG)
    SW = (-DIAG, DIAG)
    NONE = (0, 0)

class State(Enum):
	IDLE = 0
	ACTIVE = 1

#Colors
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (173,230,187)
LIGHT_PINK = (230,173,216)
LIGHT_ORANGE = (230,187,173)

def dirToDegree(dir):
	if dir == Dir.W:
		return 90
	if dir == Dir.E:
		return -90
	if dir == Dir.N:
		return 0
	if dir == Dir.S:
		return 180
	if dir == Dir.NW:
		return 45
	if dir == Dir.NE:
		return -45
	if dir == Dir.SE:
		return -135
	if dir == Dir.SW:
		return 135
	if dir == Dir.NONE:
		return 0

#returns distance (flaot) from 2 position tuples
def getDistance(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
