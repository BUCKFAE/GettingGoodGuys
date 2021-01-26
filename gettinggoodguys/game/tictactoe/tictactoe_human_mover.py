from typing import Tuple

from gettinggoodguys.game.mover import Mover
from gettinggoodguys.game.player_type import PlayerType


class TicTacToeHumanMover(Mover):

    def get_next_move(self, game, user_inputs) -> Tuple[int, int]:
        print(user_inputs)

        # pressed_location = user_inputs[0] / 300
        return 0, 0
        pass

    def get_player_type(self):
        return PlayerType.HUMAN
