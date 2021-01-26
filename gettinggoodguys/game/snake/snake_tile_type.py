from enum import Enum


class SnakeTileType(Enum):
    TILE_EMPTY = 0
    SNAKE_TILE = 1
    FOOD_TILE = 2
    WALL_TILE = 3

    def describe(self):
        return self.name