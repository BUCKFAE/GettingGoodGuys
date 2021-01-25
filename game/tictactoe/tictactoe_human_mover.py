from game.mover import Mover
from game.player_type import PlayerType


class TicTacToeHumanMover(Mover):

    def get_next_move(self, game, user_inputs):
        print(user_inputs)
        # pressed_location = user_inputs[0] / 300
        # game.update(pressed_location)

    def get_player_type(self):
        return PlayerType.HUMAN
