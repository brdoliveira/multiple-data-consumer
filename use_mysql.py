from database_strategy import DatabaseStrategy
from credentials import *
import mysql.connector

mydb = mysql.connector.connect(
    host= host,
    user=usr,
    password= pswd,
    database= database
)

class useMySql(DatabaseStrategy):
    def insert_table(self, strValues):
        mydb.connect()
        try:
            if mydb.is_connected():
                mycursor = mydb.cursor()

                sql_query = f'INSERT INTO {database}.dados(temperature,umidity,vibration,noise,proximity,weight,latitude,created_at,fk_truck,fk_route) VALUES ({strValues},now(),1,1)'

                mycursor.execute(sql_query)
                mydb.commit()
        except mysql.connector.Error as e:
            print("Erro ao conectar com o MySQL: ", e)
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

    def get_inserts_table(self):
        pass