from database_strategy import DatabaseStrategy
from credentials import *
import pyodbc

class useOdbc(DatabaseStrategy):
    def insert_table(self, strValues):
        conn = pyodbc.connect(conexao)
        try:
            cursor = conn.cursor()

            sql_query = f'INSERT INTO {database}.dados(temperature,umidity,vibration,noise,proximity,weight,latitude,created_at,fk_truck,fk_route) VALUES ({strValues},getdate(),1,1)'
            print(sql_query)

            cursor.execute(sql_query)
            cursor.commit()
        except pyodbc.ProgrammingError as e:
            print("Erro ao conectar com o MySQL: ", e)
        finally:
            cursor.close()

    def get_inserts_table(self):
        pass