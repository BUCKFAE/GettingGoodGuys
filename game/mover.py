from abc import ABC, abstractmethod
from player_type import *


class Mover(ABC):


    @abstractmethod
    def get_next_move(self, game, user_inputs):
        pass

    @abstractmethod
    def get_player_type(self):
        pass
