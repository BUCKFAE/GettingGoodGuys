import numpy as np

from gettinggoodguys.game.game import Game
from gettinggoodguys.game.grid import get_matching_coordinates, set_new_game_state, get_tile_info_at
from gettinggoodguys.game.tictactoe.tictactoe_tile_type import TicTacToeTileType


class TicTacToeGame(Game):

    def __init__(self):
        self.grid = np.full((3, 3), TicTacToeTileType.TILE_EMPTY)
        self.current_move_id = 0

    def get_possible_moves(self):
        return get_matching_coordinates(self.grid, 0)

    def update(self, move):
        """Move is a tuple"""

        #        if get_tile_info_at(self.grid, move[0], move[1]) != TicTacToeTileType.TILE_EMPTY:
        #          exit(1)  # TODO: Throw meaningful message

        if self.get_possible_moves():
            print("tie")
        print(self.get_possible_moves())


        # Setting the new tile
        if self.current_move_id % 2 == 0:
            set_new_game_state(self.grid, move[0], move[1], TicTacToeTileType.TILE_PLAYER_1)
        else:
            set_new_game_state(self.grid, move[0], move[1], TicTacToeTileType.TILE_PLAYER_2)

        self.current_move_id += 1
        if self.check_for_win():
            print(self.current_move_id % 2)

    def check_for_win(self):
        # vertical win check
        for col in range(3):
            if self.get_grid()[0][col] == self.grid[1][col] == self.get_grid()[2][col] != TicTacToeTileType.TILE_EMPTY:
                return True
        # horizontal win check
        for row in range(3):
            if self.get_grid()[row][0] == self.get_grid()[row][1] == self.get_grid()[row][2] != TicTacToeTileType.TILE_EMPTY:
                return True
        # diagonal win check
        if self.get_grid()[0][0] == self.get_grid()[1][1] == self.get_grid()[2][2] != TicTacToeTileType.TILE_EMPTY:
            return True
        # diagonal win check
        if self.get_grid()[2][0] == self.get_grid()[1][1] == self.get_grid()[0][2] != TicTacToeTileType.TILE_EMPTY:
            return True
        return False

    def get_grid(self):
        return self.grid

    def get_name(self):
        return "TicTacToe"

    def get_game_rows(self):
        return 3

    def get_game_columns(self):
        return 3
