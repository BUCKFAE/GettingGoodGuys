from game.tictactoe.tictactoe_game import TicTacToeGame
from game.tictactoe.tictactoe_tile_type import TicTacToeTileType

import pygame

from main_loop import MainLoop


def main():
    print("Hello, World!")

    tic_tac_toe_game = TicTacToeGame()
    pygame.init()
    pygame.font.init()

    main_loop = MainLoop()
    main_loop.start_main_loop()



if __name__ == "__main__":
    main()
