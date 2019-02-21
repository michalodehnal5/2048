#!/usr/bin/env python3

GAME_SIZE = 4

BASE_START_X = 100
BASE_START_Y = 100

BLOCK_SIZE = 100

TEXT_SIZE = 30

GRID_COLOR = (50, 50, 50)

GAME_COLORS_BY_NUMBER = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}
GAME_ELSE_COLOR = (238, 228, 218)

DOWN = 0
UP = 1
LEFT = 2
RIGHT = 3
