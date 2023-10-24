from type_data_strategy import TypeDataStrategy
import pandas as pd

class TypeExcel(TypeDataStrategy):

    def get_data_by_file(self, path_file):
        return pd.read_excel(path_file,header=0,index_col=0)

    def insert_data_by_bd(self):
        pass