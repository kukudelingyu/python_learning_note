from src.数据分析案例.File_Reader import TextFileReader
from src.数据分析案例.File_Reader import JsonFileReader
from src.数据库操作案例.RecordDaoImpl import *

file_reader = TextFileReader("../../data/2011年1月销售数据.txt")
json_reader = JsonFileReader("../../data/2011年2月销售数据JSON.txt")

text_list = file_reader.readFile()
json_list = json_reader.readFile()

dao = RecordDaoImpl()
if not dao.check_database_exists("销售数据"):
    dao.initDatabase()
else:
    dao.selectDatabase()

for ele in text_list:
    dao.insertRecord(ele, "jan")

for ele in json_list:
    dao.insertRecord(ele, "feb")

dao.release()
