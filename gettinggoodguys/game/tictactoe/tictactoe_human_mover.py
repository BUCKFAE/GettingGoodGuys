from typing import Tuple

from gettinggoodguys.game.mover import Mover
from gettinggoodguys.game.player_type import PlayerType


class TicTacToeHumanMover(Mover):

    def get_next_move(self, game, user_inputs) -> Tuple[int, int]:
        return int(user_inputs[1] / 200), int(user_inputs[0] / 200)

    def get_player_type(self):
        return PlayerType.HUMAN
