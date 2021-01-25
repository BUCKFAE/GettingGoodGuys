from game.mover import Mover, PlayerType


class TicTacToeHumanMover(Mover):

    def get_next_move(self, game, user_inputs):

        pressed_location = user_inputs[0] / 300

        game.update(pressed_location)
        pass

    def get_player_type(self):
        return PlayerType.HUMAN