import threading
import time

"""
thread_obj = threading.Thread(group [, target [, name [, args [, kwargs]]]]])
- group: 暂时无用，未来功能的预留参数
- target: 执行目标任务名称
- args: 以元组的方式给执行任务传参
- swargs: 以字典的形式给执行任务传参
- name: 线程名，一般不用设置
"""

def sing(where=None, music_name=None):
    while True:
        print(f"我正在{where}唱：{music_name}")
        time.sleep(1)

def dance(who = None, dance_name=None):
    while True:
        print(f"我正在和{who}跳：{dance_name}")
        time.sleep(1)


if __name__ == '__main__':
    thread_1 = threading.Thread(target=sing, args=("卫生间", "青花瓷"))
    thread_2 = threading.Thread(target=dance, kwargs={"dance_name": "芭蕾", "who": "杨超越"})
    thread_1.start()
    thread_2.start()
