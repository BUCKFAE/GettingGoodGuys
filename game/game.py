from abc import ABC, abstractmethod


class Game(ABC):

    @abstractmethod
    def get_grid(self):
        pass

    @abstractmethod
    def update(self, move):
        pass

    @abstractmethod
    def get_possible_moves(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_game_rows(self):
        pass

    @abstractmethod
    def get_game_columns(self):
        pass

