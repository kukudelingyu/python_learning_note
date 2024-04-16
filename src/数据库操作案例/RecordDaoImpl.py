from pymysql.cursors import Cursor

from src.数据分析案例.Record import Record
from src.数据库操作案例.RecordDao import RecordDao
from pymysql import Connection

class RecordDaoImpl(RecordDao):
    cursor: Cursor = None

    def __init__(self):
        self.conn = Connection(
            host='localhost',
            port=3306,
            user='root',
            password='l6600410',
            autocommit=True
        )

    def initDatabase(self):
        cursor = self.conn.cursor()
        cursor.execute("create database 销售数据")
        self.conn.select_db("销售数据")
        cursor.execute("create table jan(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, date varchar(20), order_id varchar(50), money float, province varchar(50))")
        cursor.execute("create table feb(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, date varchar(20), order_id varchar(50), money float, province varchar(50))")

    def selectDatabase(self):
        self.conn.select_db("销售数据")

    def insertRecord(self, record: Record, table_name):
        cursor = self.conn.cursor()
        cursor.execute(f"insert into {table_name} (date, order_id, money, province) values ('{record.date}', '{record.order_id}', {float(record.money)}, '{record.province}')")
        cursor.close()

    def queryAllRecord(self) -> list[Record]:
        record_tuple = self.cursor.execute("select * from 销售数据")
        record_list = list()
        for element in record_tuple:
            record = Record(element[0], element[1], element[2], element[3])
            record_list.append(record)
        return record_list

    def release(self):
        self.conn.close()


    def check_database_exists(self, database_name):
        cursor = self.conn.cursor()
        cursor.execute(f"show databases like '{database_name}'")
        result = cursor.fetchone()
        cursor.close()
        if result:
            return True
        else:
            return False

    def check_table_exists(self, table_name):
        cursor = self.conn.cursor()
        cursor.execute(f"show tables like '{table_name}'")
        result = cursor.fetchone()
        cursor.close()
        if result:
            return True
        else:
            return False
