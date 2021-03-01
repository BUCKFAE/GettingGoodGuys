import pygame
import pygame_gui
import json

import custom_colors
import settings
from game.tictactoe.tictactoe_game import TicTacToeGame
from gettinggoodguys.game.player_type import PlayerType
from gettinggoodguys.game.snake.snake_game import SnakeGame
from gettinggoodguys.game.tictactoe.tictactoe_human_mover import TicTacToeHumanMover
from gettinggoodguys.game.tictactoe.tictactoe_tile_type import TicTacToeTileType
from settings import Settings

pygame.init()

window_surface = pygame.display.set_mode((Settings.WINDOW_X, Settings.WINDOW_Y))
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

manager = pygame_gui.UIManager((Settings.WINDOW_X, Settings.WINDOW_Y), "game/themes/theme.json")

window_game_settings = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect((640, Settings.GAP),
                              (Settings.WINDOW_X - Settings.GAME_WIDTH - 60, Settings.GAME_HEIGHT)),
    starting_layer_height=1,
    visible=False,
    manager=manager)

window_start = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 0), (Settings.WINDOW_X, Settings.WINDOW_Y)),
                                           starting_layer_height=1,
                                           manager=manager)

button_TicTacToe = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((250, 250), (100, Settings.WINDOW_GAME_SETTINGS_HEIGTH)),
    text='TicTacToe',
    object_id='button',
    container=window_start,
    manager=manager)

button_Snake = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((250, 500), (100, Settings.WINDOW_GAME_SETTINGS_HEIGTH)),
    text='Snake',
    container=window_start,
    manager=manager)

button_back = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (Settings.WINDOW_GAME_SETTINGS_WIDTH, Settings.WINDOW_GAME_SETTINGS_HEIGTH)),
    text='back',
    container=window_game_settings,
    manager=manager)

button_start = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 530), (Settings.WINDOW_GAME_SETTINGS_WIDTH, Settings.WINDOW_GAME_SETTINGS_HEIGTH)),
    text='start',
    container=window_game_settings,
    manager=manager)

window_game_infos = pygame_gui.elements.UITextBox(html_text="This is normal text.",
                                                  relative_rect=pygame.Rect((Settings.GAP, Settings.GAME_HEIGHT + 40),
                                                                            (Settings.GAME_WIDTH, 250)),
                                                  visible=False,
                                                  object_id='aaa',
                                                  manager=manager)


class MainLoop:
    run = True

    def __init__(self):
        self.list_with_all_drop_down_menus = []
        self.game_is_running = False
        self.game = None
        self.current_game = None
        self.movers = []
        # window_TicTacToe.hide()
        # self.game = TicTacToeGame()
        # self.game = SnakeGame(50,80)

        print("Initializing MainLoop...")

        self.current_player = 0

    def start_main_loop(self):
        while self.run:
            self.loop()

    def handle_back_button(self):
        # background.fill(pygame.Color('#000000'))
        self.game_is_running = False
        for i in self.list_with_all_drop_down_menus:
            i.kill()

        window_surface.subsurface(
            pygame.draw.rect(window_surface, ('#000000'), (0, 0, Settings.WINDOW_X, Settings.WINDOW_X)))
        window_game_settings.hide()
        window_game_infos.hide()
        window_start.show()

    # window_start.show()

    def handle_button_start(self):
        if self.game_is_running:
            self.create_game()
        for i in self.list_with_all_drop_down_menus:
            self.movers.append(Settings.AlGOS.get(self.current_game).get(i.selected_option))
        # Todo ein player type für alle spiele?
        self.playerList = [TicTacToeTileType.TILE_PLAYER_1, TicTacToeTileType.TILE_PLAYER_2]

        self.game_is_running = not self.game_is_running

    def build_gui(self):
        # create the drop down menu for the algorithm selection
        for i in range(self.game.get_number_of_players()):
            self.list_with_all_drop_down_menus.append(pygame_gui.elements.UIDropDownMenu(options_list=[],
                                                                                         starting_option='choose player x'.replace(
                                                                                             'x', str(i + 1)),
                                                                                         relative_rect=pygame.Rect(
                                                                                             (10, 100 + (i * 50)), (
                                                                                                 Settings.WINDOW_GAME_SETTINGS_WIDTH,
                                                                                                 Settings.WINDOW_GAME_SETTINGS_HEIGTH)),
                                                                                         container=window_game_settings,
                                                                                         manager=manager))
        # fill the drop down menu with right content
        for i in range(self.list_with_all_drop_down_menus.__len__()):
            l = self.list_with_all_drop_down_menus.__getitem__(i)
            for algo in Settings.AlGOS.get(self.current_game).keys():
                l.options_list.append(algo)

        window_game_infos.show()
        window_game_infos.html_text = self.current_game
        window_game_infos.rebuild()

    def create_game(self):
        window_start.hide()
        window_game_settings.show()
        if self.current_game == "TicTacToe":
            self.game = TicTacToeGame()
            print("create game")
        if self.current_game == "SnakeGame":
            self.game = SnakeGame(20, 20)

        self.compute_tile_size()
        self.list_with_all_drop_down_menus = []
        self.build_gui()
        self.gamef = pygame.Rect(Settings.GAP, Settings.GAP, 600, 600)
        self.gamef = window_surface.subsurface(self.gamef)
        self.gamef.fill('#beb8a8')
        self.draw_game_board()

    def loop(self):

        # Drawing the game_board
        # self.draw_game_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_back:
                        self.handle_back_button()
                    if event.ui_element == button_start:
                        self.handle_button_start()
                    if event.ui_element == button_Snake:
                        self.current_game = "SnakeGame"
                        self.create_game()
                    if event.ui_element == button_TicTacToe:
                        self.current_game = "TicTacToe"
                        self.create_game()

            if self.game_is_running:
                active_mover = self.movers[self.current_player % len(self.movers)]
                if active_mover.get_player_type() == PlayerType.HUMAN:
                    # Getting the next move for HUMAN
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        check = active_mover.get_next_move(self.game, pygame.mouse.get_pos())
                        # if user input is valid
                        if check:
                            self.game_is_running = self.game.update(check)[0]
                            self.current_player += 1
                            self.draw_game_board()

                else:
                    # Getting the next move for AI
                    self.game_is_running = self.game.update(active_mover.get_next_move(self.game, event))[0]
                    self.current_player += 1
                    self.draw_game_board()

                if not self.game_is_running:
                    text = "asdfads \n wins"
                    window_game_infos.html_text = window_game_infos.html_text + "<br /> winner is: "
                    window_game_infos.rebuild()

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
                self.gamef.blit(X, (column * 200, row * 200))

            if self.game.get_grid()[row][column] == TicTacToeTileType.TILE_PLAYER_2:
                self.gamef.blit(O, (column * 200, row * 200))
