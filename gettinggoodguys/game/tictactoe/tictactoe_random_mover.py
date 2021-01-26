import random

from gettinggoodguys.game.mover import Mover
from gettinggoodguys.game.player_type import PlayerType


class TicTacToeRandomMover(Mover):

    def get_player_type(self):
        return PlayerType.AI

    def get_next_move(self, game, user_inputs):
        possible_moves = game.get_possible_moves()
        return random.choice(possible_moves)
