from abc import ABC, abstractmethod


class AnonymousBoardService(ABC):

    @classmethod
    @abstractmethod
    def create(self, title: str, content: str):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def read(self, board_id: str):
        pass
