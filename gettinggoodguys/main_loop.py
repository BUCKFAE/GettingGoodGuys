import pygame

import custom_colors
import settings

from game.tictactoe.tictactoe_game import TicTacToeGame
from game.tictactoe.tictactoe_human_mover import TicTacToeHumanMover
from gettinggoodguys.game.player_type import PlayerType
from settings import Settings


window_surface = pygame.display.set_mode((Settings.WINDOW_X, Settings.WINDOW_Y))
background = pygame.Surface((Settings.WINDOW_X, Settings.WINDOW_Y))
background.fill(pygame.Color('#000000'))


class MainLoop:
    run = True

    def __init__(self):
        self.game = TicTacToeGame()
        # self.game = SnakeGame(50,80)

        self.movers = [TicTacToeHumanMover(), TicTacToeHumanMover()]

        print("Initializing MainLoop...")

        self.current_player = 0

    def start_main_loop(self):
        self.compute_tile_size()
        while self.run:
            self.loop()

    def loop(self):

        # Drawing the game_board
        self.draw_game_board()
        pygame.display.update()

        active_mover = self.movers[self.current_player % len(self.movers)]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if active_mover.get_player_type() == PlayerType.HUMAN:
                # Getting the next move for HUMAN
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # TODO: active_mover should return false if user input is not valid
                    active_mover.get_next_move(self.game, pygame.mouse.get_pos())
            else:
                active_mover.get_next_move(self.game, event)




        self.current_player += 1

    def compute_tile_size(self):
        if self.game.get_game_rows() == self.game.get_game_columns():
            Settings.TILE_SIZE = Settings.GAME_WIDTH / self.game.get_game_rows()
        else:
            Settings.TILE_SIZE = int(Settings.GAME_WIDTH / max(self.game.get_game_rows(), self.game.get_game_columns()))

    def draw_game_board(self):

        for current_row in range(self.game.get_game_rows()):
            # horizontal line
            pygame.draw.line(window_surface, custom_colors.LINE_COLOR,
                             (Settings.TILE_SIZE + current_row *
                              Settings.TILE_SIZE, 0),
                             (Settings.TILE_SIZE + current_row *
                              Settings.TILE_SIZE,
                              Settings.TILE_SIZE * self.game.get_game_columns()),
                             settings.settings[self.game.get_name()]['thickness'])

            for current_column in range(self.game.get_game_columns()):
                # vertical line
                pygame.draw.line(window_surface, custom_colors.LINE_COLOR,
                                 (0,
                                  Settings.TILE_SIZE + current_column *
                                  Settings.TILE_SIZE),
                                 (Settings.TILE_SIZE * self.game.get_game_rows(),
                                  Settings.TILE_SIZE + current_column *
                                  Settings.TILE_SIZE),
                                 settings.settings[self.game.get_name()]['thickness'])
