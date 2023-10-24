import os

from type_json import TypeJson
from type_excel import TypeExcel
from type_pdf import TypePdf
from type_xml import TypeXml

def get_type_data(type: str):
    typeFile = type.upper()
    if typeFile == ".JSON":
        return TypeJson()
    elif typeFile == ".PDF":
        return TypePdf()
    elif typeFile == ".XLSX":
        return TypeExcel()
    elif typeFile == ".XML":
        return TypeXml()
    else:
        raise Exception("Extensão inválida!")

def init(path_file):
    _, file_extension = os.path.splitext(path_file)
    typeData = get_type_data(file_extension)
    data = typeData.get_data_by_file(path_file)
    stringToInsert = typeData.insert_data_by_bd(data)
    print(stringToInsert)


init("./files-examples/excel_registros.pdf")