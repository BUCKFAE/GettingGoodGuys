import numpy as np

from game.game import Game
from game.grid import get_matching_coordinates, get_tile_info_at, set_new_game_state
from game.tictactoe.tictactoe_tile_type import TicTacToeTileType


class TicTacToeGame(Game):

    def __init__(self):
        self.grid = np.zeros((3, 3))

        self.current_move_id = 0

    def get_possible_moves(self):
        return get_matching_coordinates(self.grid, 0)

    def update(self, move):
        """Move is a tuple"""
        if get_tile_info_at(self.grid, move[0], move[1]) != TicTacToeTileType.TILE_EMPTY:
            exit(1)  # TODO: Throw meaningful message

        # Setting the new tile
        if self.current_move_id % 2 == 0:
            set_new_game_state(self.grid, move[0], move[1], TicTacToeTileType.TILE_PLAYER_1)
        else:
            set_new_game_state(self.grid, move[0], move[1], TicTacToeTileType.TILE_PLAYER_2)

        pass

    def get_grid(self):
        return self.grid

    def get_name(self):
        return "TicTacToe"

    def get_game_rows(self):
        return 3

    def get_game_columns(self):
        return 3
