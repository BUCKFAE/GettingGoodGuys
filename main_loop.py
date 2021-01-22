import pygame

from game.grid import get_tile_count_x
from game.tictactoe.tictactoe_game import TicTacToeGame
from game.tictactoe.tictactoe_human_mover import TicTacToeHumanMover


class MainLoop:
    def __init__(self):
        self.game = TicTacToeGame()
        self.movers = [TicTacToeHumanMover(), TicTacToeHumanMover()]

        print("Initializing MainLoop...")

        self.current_player = 0

    def start_main_loop(self):
        while True:
            self.loop()

    def loop(self):
        # Getting all events
        events = pygame.event.get()

        active_mover = self.movers[self.current_player % len(self.movers)]

        # Getting the next move
        next_move = active_mover.get_next_move(self.game, events)

        self.current_player += 1

        # Executing the next move
        self.game.update(next_move)

        # Drawing the game_board
        self.draw_game_board()

    def draw_game_board(self):
        # TODO: Drawing all lines between tiles
        pass
