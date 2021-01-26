import numpy as np

from gettinggoodguys.game.game import Game


class SnakeGame(Game):
    rows = 0
    columns = 0

    def __init__(self, rows: int, columns: int):
        self.grid = np.zeros((rows, columns))
        self.rows = rows
        self.columns = columns

    def get_grid(self) -> np.array:
        pass

    def update(self, move):
        pass

    def get_possible_moves(self):
        pass

    def get_name(self):
        return "SnakeGame"

    def get_game_rows(self):
        return self.rows

    def get_game_columns(self):
        return self.columns
