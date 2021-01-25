import numpy as np

from game.grid import get_matching_coordinates
from game.tictactoe.tictactoe_game import TicTacToeGame
from game.tictactoe.tictactoe_tile_type import TicTacToeTileType

import pygame

from main_loop import MainLoop


def main():
    print("Hello, World!")

    test_grid = np.array([[1, 0, 0], [1, 1, 1], [0, 1, 1]])
    print(test_grid)

    print(get_matching_coordinates(test_grid, 1))

    tic_tac_toe_game = TicTacToeGame()
    pygame.init()
    pygame.font.init()

    main_loop = MainLoop()
    main_loop.start_main_loop()



if __name__ == "__main__":
    main()
