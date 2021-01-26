from typing import Tuple

from gettinggoodguys.game.mover import Mover
from gettinggoodguys.game.player_type import PlayerType


class TicTacToeHumanMover(Mover):

    def get_next_move(self, game, user_inputs) -> Tuple[int, int]:
        print(user_inputs)

        # pressed_location = user_inputs[0] / 300
        return user_inputs[0] / 200, user_inputs[1] / 200
        pass

    def get_player_type(self):
        return PlayerType.HUMAN
