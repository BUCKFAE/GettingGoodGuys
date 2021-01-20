from abc import ABC, abstractmethod


class Mover(ABC):

    @abstractmethod
    def get_next_move(self, game, user_inputs):
        pass
