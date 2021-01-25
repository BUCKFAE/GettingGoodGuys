import pygame

import custom_colors
import settings
from game.player_type import PlayerType
from game.tictactoe.tictactoe_game import TicTacToeGame
from game.tictactoe.tictactoe_human_mover import TicTacToeHumanMover
from settings import Settings
from game.snake.snake_game import SnakeGame

window_surface = pygame.display.set_mode((Settings.WINDOW_X, Settings.WINDOW_Y))
background = pygame.Surface((Settings.WINDOW_X, Settings.WINDOW_Y))
background.fill(pygame.Color('#000000'))


class MainLoop:
    def __init__(self):
        self.game = TicTacToeGame()
        #self.game = SnakeGame(12, 7)

        self.movers = [TicTacToeHumanMover(), TicTacToeHumanMover()]


        print("Initializing MainLoop...")

        self.current_player = 0

    def start_main_loop(self):
        self.compute_tile_size()
        while True:
            self.loop()

    def loop(self):

        active_mover = self.movers[self.current_player % len(self.movers)]
        # Getting all events
        events = pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()




        # Getting the next move
        next_move = active_mover.get_next_move(self.game, events)

        self.current_player += 1

        # Executing the next move
        self.game.update(next_move)

        # Drawing the game_board
        self.draw_game_board()
        pygame.display.update()

    def compute_tile_size(self):
        if self.game.get_game_rows() == self.game.get_game_columns():
            Settings.TILE_SIZE = Settings.GAME_WIDTH / self.game.get_game_rows()
        else:
            Settings.TILE_SIZE = int(Settings.GAME_WIDTH/max(self.game.get_game_rows(), self.game.get_game_columns()))

    def draw_game_board(self):

        for current_row in range(self.game.get_game_rows()):
            # horizontal line
            pygame.draw.line(window_surface, custom_colors.LINE_COLOR,
                             (Settings.TILE_SIZE + current_row *
                              Settings.TILE_SIZE, 0),
                             (Settings.TILE_SIZE + current_row *
                              Settings.TILE_SIZE,
                              Settings.TILE_SIZE*self.game.get_game_columns()),
                             settings.settings[self.game.get_name()]['thickness'])

            for current_column in range(self.game.get_game_columns()):
                # vertical line
                pygame.draw.line(window_surface, custom_colors.LINE_COLOR,
                                 (0,
                                  Settings.TILE_SIZE + current_column *
                                  Settings.TILE_SIZE),
                                 (Settings.TILE_SIZE*self.game.get_game_rows(),
                                  Settings.TILE_SIZE + current_column *
                                  Settings.TILE_SIZE),
                                 settings.settings[self.game.get_name()]['thickness'])
