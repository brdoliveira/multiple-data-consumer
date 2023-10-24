from type_data_strategy import TypeDataStrategy
import pandas as pd

class TypeJson(TypeDataStrategy):

    def get_data_by_file(self, path_file):
        return pd.read_json(path_file)     

    def insert_data_by_bd(self,df):
        list_df_to_string = []

        for row in df.iterrows():
            stringRow = f'{row[1].temperatura},{row[1].umidade},{row[1].vibracao},{row[1].ruido},{row[1].proximidade},{row[1].peso},{row[1].latitude}'
            list_df_to_string.append(stringRow)
        
        return list_df_to_string