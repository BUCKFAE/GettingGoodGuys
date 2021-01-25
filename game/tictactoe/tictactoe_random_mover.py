import random

from game.mover import Mover


class TicTacToeRandomMover(Mover):

    def get_next_move(self, game, user_inputs):
        possible_moves = game.get_possible_moves()
        return random.choice(possible_moves)
