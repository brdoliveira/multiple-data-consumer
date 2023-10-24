from abc import ABC, abstractmethod

class DatabaseStrategy(ABC):

    @abstractmethod
    def insert_table(self, strValues):
        pass

    @abstractmethod
    def get_inserts_table(self):
        pass