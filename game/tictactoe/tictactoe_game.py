import numpy as np

from game.game import Game


class TicTacToeGame(Game):

    def __init__(self):
        self.grid = np.zeros((3, 3))

    def get_possible_moves(self):
        pass

    def update(self, move):
        pass

    def get_grid(self):
        pass


