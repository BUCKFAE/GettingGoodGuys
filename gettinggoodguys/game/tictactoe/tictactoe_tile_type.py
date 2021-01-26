from enum import Enum


class TicTacToeTileType(Enum):
    TILE_EMPTY = 0
    TILE_PLAYER_1 = 1
    TILE_PLAYER_2 = 2

    def describe(self):
        return self.name

