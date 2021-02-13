import threading
import time


def sleaper(sec):
    print(f'sleep {sec} sec')
    time.sleep(sec)
    print('no sleep')


def mult(x, y):
    print(x*y)


if __name__ == "__main__":
    th_1_list, th_2_list = [], []
    for i in range(5):
        thread_1 = threading.Thread(target=sleaper, args = (i,))
        thread_2 = threading.Thread(target=mult, args=(i, i+1,))
        thread_1.start()
        thread_2.start()
        th_1_list.append(thread_1)
        th_2_list.append(thread_2)
    for x in th_1_list:
        x.join()
    for x in th_2_list:
        x.join()
    print('Всё, поспал полностью!')