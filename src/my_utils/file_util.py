
def print_file_info(file_name):
    try:
        f = open(file_name, "r", encoding="utf-8")
        print(f.read())
    except:
        print("文件不存在")
    finally:
        if f:
            f.close()
        print("结束")


def append_to_file(s, file_name):
    try:
        f = open(file_name, "a", encoding="utf-8")
        f.write(f"\n{s}")
        f.flush()
    except Exception as e:
        print(f"程序出现异常{e}")
    finally:
        if f:
            f.close()
        print("结束")


if __name__ == '__main__':
    # print_file_info("../../data/fileLearning.txt")
    append_to_file("追加数据", "../../data/abc.txt")
