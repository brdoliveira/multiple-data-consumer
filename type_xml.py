from type_data_strategy import TypeDataStrategy
import pandas as pd

class TypeXml(TypeDataStrategy):

    def get_data_by_file(self, path_file):
        return pd.read_excel(path_file,header=0,index_col=0)

    def insert_data_by_bd(self,df):
        list_df_to_string = []

        for row in df.iterrows():
            stringRow = f'{row[1][0]},{row[1][1]},{row[1][2]},{row[1][3]},{row[1][4]},{row[1][5]},{row[1][6]}'
            list_df_to_string.append(stringRow)
        
        return list_df_to_string