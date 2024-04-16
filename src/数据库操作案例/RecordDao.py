from src.数据分析案例.Record import Record
from abc import ABCMeta
from abc import abstractmethod

class RecordDao(metaclass=ABCMeta):

    @abstractmethod
    def insertRecord(self, record: Record, table_name):
        pass

    @abstractmethod
    def queryAllRecord(self) -> list[Record]:
        pass
