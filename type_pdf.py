from type_data_strategy import TypeDataStrategy
import pandas as pd

# pip install tabula-py
import tabula

class TypePdf(TypeDataStrategy):

    def get_data_by_file(self, path_file):
        tables = tabula.read_pdf(path_file,pages='1')
        tables = tables[0]
        tables = pd.DataFrame(tables)
        return tables

    def insert_data_by_bd(self):
        pass

typePdf = TypePdf()

va = typePdf.get_data_by_file(path_file='./files-examples/excel_registros.pdf')
print(va.head(va))