# Settings for TicTacToe

from gettinggoodguys.game.tictactoe.tictactoe_random_mover import TicTacToeRandomMover
from gettinggoodguys.game.tictactoe.tictactoe_human_mover import TicTacToeHumanMover

settings = {'TicTacToe': {'thickness': 10, 'space': 20},
            'SnakeGame': {'thickness': 1, 'space': 5}}


class Settings:
    # window
    WINDOW_X = 900
    WINDOW_Y = 900

    # game_field
    GAME_HEIGHT = 600
    GAME_WIDTH = 600

    # length from all elements in window_game_setting
    WINDOW_GAME_SETTINGS_WIDTH = WINDOW_X - GAME_WIDTH - 90

    # heigth from all elements in window_game_setting
    WINDOW_GAME_SETTINGS_HEIGTH = 50

    # gap game_field
    GAP = 20

    # always n x n
    TILE_SIZE = 0

    # list with all Algos
    AlGOS = {'TicTacToe': {"Random": TicTacToeRandomMover(), "HUMAN": TicTacToeHumanMover()},
             'SnakeGame': {"RandomS": TicTacToeRandomMover(), "HUMAN": "asd"}}

    a = AlGOS.get("TicTacToe").get("HUMAN")
    print(a.get_player_type())



