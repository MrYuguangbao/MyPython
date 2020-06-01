import threading
import time


def coding():
    for x in range(3):
        print('当前线程%s正在写代码' % threading.current_thread())
        time.sleep(1)


def drawing():
    for x in range(3):
        print('当前线程%s正在画图' % threading.current_thread())
        time.sleep(1)


def single_thread():
    coding()
    drawing()


def multi_thread():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()


if __name__ == '__main__':
    multi_thread()
    print('当前线程数:'+threading.enumerate())
