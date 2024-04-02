import json

from src.数据分析案例.Record import Record


class FileReader:
    def __init__(self, path):
        self.path = path

    def readFile(self):
        pass


class TextFileReader(FileReader):

    def readFile(self) -> list[Record]:
        with open(self.path, "r", encoding="UTF-8") as f:
            lines = f.readlines()
            record_list = list[Record]()
            for line in lines:
                line_content_list = line.strip().split(",")
                record = Record(line_content_list[0], line_content_list[1], int(line_content_list[2]), line_content_list[3])
                record_list.append(record)

        return record_list


class JsonFileReader(FileReader):

    def readFile(self) -> list[Record]:
        with open(self.path, "r", encoding="UTF-8") as f:
            lines = f.readlines()
            record_list = list[Record]()
            for line in lines:
                line_json = line.strip("\n")
                line_dict = json.loads(line_json)
                record: Record = Record(line_dict["date"], line_dict["order_id"], line_dict["money"], line_dict["province"])
                record_list.append(record)

        return record_list

if __name__ == '__main__':
    reader = TextFileReader("../../data/2011年1月销售数据.txt")
    print(reader.readFile())
