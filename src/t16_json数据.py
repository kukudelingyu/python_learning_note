import json


data = [{"name": "张三", "age": 14}, {"name": "李四", "age": 22}]

json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

new_data = json.loads(json_str)
print(type(new_data))
print(new_data)