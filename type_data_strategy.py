from abc import ABC, abstractmethod

class TypeDataStrategy(ABC):

    @abstractmethod
    def get_data_by_file(self, path_file):
        pass

    @abstractmethod
    def insert_data_by_bd(self,df):
        pass