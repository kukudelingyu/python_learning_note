import multiprocessing
import time


def coding(num, name):
    for index in range(num):
        print(f"{name} is coding...")
        time.sleep(0.2)

def music(count):
    for index in range(count):
        print("music..")
        time.sleep(0.2)


if __name__ == '__main__':
    # 元组传参，按照顺序依次给参数赋值
    coding_process = multiprocessing.Process(target=coding, args=(3,"zhangsan"))
    # 字典传参，key需要与参数名保持一致，value为实际参数值
    music_process = multiprocessing.Process(target=music, kwargs={"count": 2})

    coding_process.start()
    music_process.start()
