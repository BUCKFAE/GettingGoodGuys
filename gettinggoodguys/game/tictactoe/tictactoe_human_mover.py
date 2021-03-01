from typing import Tuple, Union

from gettinggoodguys.game.mover import Mover
from gettinggoodguys.game.player_type import PlayerType



class TicTacToeHumanMover(Mover):


    # return position from the user input only if correct otherwise return false
    def get_next_move(self, game, user_inputs) -> Union[Tuple[int, int], bool]:
        #Todo +20 ist Settings.GAP -> klappt nicht weil sonst ein zyklischer import entsteht
        x = int((user_inputs[1] + 20) / 200)
        y = int((user_inputs[0] + 20) / 200)
        if x < 3 and y < 3:
            return x,y
        return False



    def get_player_type(self):
        return PlayerType.HUMAN


