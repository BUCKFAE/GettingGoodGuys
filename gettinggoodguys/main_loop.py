import pygame
import pygame_gui

import custom_colors
import settings
from game.tictactoe.tictactoe_game import TicTacToeGame
from game.tictactoe.tictactoe_human_mover import TicTacToeHumanMover
from gettinggoodguys.game.player_type import PlayerType
from gettinggoodguys.game.tictactoe.tictactoe_tile_type import TicTacToeTileType
from settings import Settings

pygame.init()

window_surface = pygame.display.set_mode((Settings.WINDOW_X, Settings.WINDOW_Y))
current_window = window_surface
background = pygame.Surface((Settings.WINDOW_X, Settings.WINDOW_Y))
background.fill(pygame.Color('#000000'))

# gamef = pygame.Rect(0, 0, 600, 600)
# gamef = window_surface.subsurface(gamef)
# gamef.fill('#beb8a8')

O = pygame.image.load('images/O.png')
O = pygame.transform.scale(O, (190, 190))
O.set_colorkey(('#FFFFFF'))

X = pygame.image.load('images/X.png')
X = pygame.transform.scale(X, (190, 190))
X.set_colorkey(('#FFFFFF'))

back = pygame.image.load('images/back.png')
back = pygame.transform.scale(back, (100, 100))
back.set_colorkey(('#FFFFFF'))

# button_layout_rect = pygame.Rect(400, 400, 100, 20)

manager = pygame_gui.UIManager((Settings.WINDOW_X, Settings.WINDOW_Y))
#game_is_chosen = False

TicTacToe_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 500), (100, 50)),
                                                text='TicTacToe',
                                                manager=manager)


window_TicTacToe = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 0), (Settings.WINDOW_X, Settings.WINDOW_Y)),
                                              starting_layer_height=0,
                                              manager=manager)


TicTacToe_button_back = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 0), (100, 100)),
                                            text='back',
                                            container=window_TicTacToe,
                                            manager=manager)








class MainLoop:
    run = True

    def __init__(self):
        self.game_is_chosen = False
        self.game = None
        window_TicTacToe.hide()
       # self.game = TicTacToeGame()
        #self.game = SnakeGame(50,80)




        print("Initializing MainLoop...")

        self.current_player = 0

    def start_main_loop(self):
        while self.run:
            self.loop()

    def handle_back_button(self):

        TicTacToe_button.show()


    def handle_TictacToe_button(self):
        window_TicTacToe.show()


        self.game_is_chosen = True
        self.game = TicTacToeGame()
        self.compute_tile_size()
        self.movers = [TicTacToeHumanMover(), TicTacToeHumanMover()]
        self.playerList = [TicTacToeTileType.TILE_PLAYER_1, TicTacToeTileType.TILE_PLAYER_2]
        self.gamef = pygame.Rect(0, 0, 600, 600)
        self.gamef = window_surface.subsurface(self.gamef)
        self.gamef.fill('#beb8a8')
        self.draw_game_board()
        window_TicTacToe.set_image(self.gamef)
        TicTacToe_button.hide()



    def loop(self):

        # Drawing the game_board
        #self.draw_game_board()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == TicTacToe_button:
                        self.handle_TictacToe_button()
                    if event.ui_element == TicTacToe_button_back:
                        print("hide")
                        self.handle_back_button()
            if self.game_is_chosen:
                active_mover = self.movers[self.current_player % len(self.movers)]
                if active_mover.get_player_type() == PlayerType.HUMAN:
                    # Getting the next move for HUMAN
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        check = active_mover.get_next_move(self.game, pygame.mouse.get_pos())
                        # if user input is valid
                        if check:
                            self.game.update(check)
                            self.current_player += 1
                            self.draw_game_board()
                            window_TicTacToe.set_image(self.gamef)

                else:
                    # Getting the next move for AI
                    # Todo entscheidet sich die AI immer richtig und wenn nein wie gehen wir damit um?
                    active_mover.get_next_move(self.game, event)
                    self.current_player += 1
                    self.draw_game_board()












            manager.process_events(event)

        manager.update(60)
        manager.draw_ui(window_surface)
        pygame.display.update()

    def compute_tile_size(self):
        if self.game.get_game_rows() == self.game.get_game_columns():
            Settings.TILE_SIZE = Settings.GAME_WIDTH / self.game.get_game_rows()
        else:
            Settings.TILE_SIZE = int(Settings.GAME_WIDTH / max(self.game.get_game_rows(), self.game.get_game_columns()))

    def draw_game_board(self):

        for current_row in range(self.game.get_game_rows()):
            # horizontal line
            pygame.draw.line(self.gamef, custom_colors.LINE_COLOR,
                             (Settings.TILE_SIZE + current_row *
                              Settings.TILE_SIZE, 0),
                             (Settings.TILE_SIZE + current_row *
                              Settings.TILE_SIZE,
                              Settings.TILE_SIZE * self.game.get_game_columns()),
                             settings.settings[self.game.get_name()]['thickness'])

            for current_column in range(self.game.get_game_columns()):
                # vertical line
                pygame.draw.line(self.gamef, custom_colors.LINE_COLOR,
                                 (0,
                                  Settings.TILE_SIZE + current_column *
                                  Settings.TILE_SIZE),
                                 (Settings.TILE_SIZE * self.game.get_game_rows(),
                                  Settings.TILE_SIZE + current_column *
                                  Settings.TILE_SIZE),
                                 settings.settings[self.game.get_name()]['thickness'])
                self.draw_object(current_row, current_column)

    def draw_object(self, row, column):
        if self.game.get_name() == "TicTacToe":
            if self.game.get_grid()[row][column] == TicTacToeTileType.TILE_PLAYER_1:
                # window_surface.blit(X,(20,20))
                self.gamef.blit(X, (column * 200, row * 200))

            # self.draw_X(row, column)
            if self.game.get_grid()[row][column] == TicTacToeTileType.TILE_PLAYER_2:
                self.gamef.blit(O, (column * 200, row * 200))
                # self.draw_O(row, column)
