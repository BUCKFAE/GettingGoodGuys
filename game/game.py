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
