import numpy as np

from game.game import Game


class SnakeGame(Game):

    def __init__(self, game_size_x, game_size_y):
        self.grid = np.zeros((20, 20))

    def get_grid(self):
        pass

    def update(self, move):
        pass

    def get_possible_moves(self):
        pass
