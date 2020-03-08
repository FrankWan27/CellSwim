from enum import Enum

DISPLAY_W = 1200
DISPLAY_H = 600
GAME_W = 600
GAME_H = 600
FPS = 30
START_ENERGY = 10
DIAG = 0.70710678118
POP_SIZE = 50

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