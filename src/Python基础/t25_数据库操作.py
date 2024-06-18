from pymysql import Connection

# 连接数据库
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="l6600410",
    autocommit=True
)
info = conn.get_server_info()
print(info)

# 获取游标对象
cursor = conn.cursor()
# 创建数据库
# cursor.execute("create database goski")
# 选择数据库
conn.select_db("goski")
# 删除表
# cursor.execute("drop table tech")
# 创建表
# cursor.execute("create table tech(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(20), language varchar(20), age INT)")
cursor.execute("insert into tech (name, language, age) values ('段凌宇', 'android', 33)")
cursor.execute("insert into tech (name, language, age) values ('戴志强', 'ios', 35)")
cursor.execute("insert into tech (name, language, age) values ('张峰', 'python', 38)")
conn.close()
