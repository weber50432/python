import multiprocessing as mp
import time


def job(v, num):
    for _ in range(10):
        time.sleep(0.1)  # 暫停0.1秒，增加辨識度
        v.value += num  # v.value 取得共享變數
        print(v.value)


def multicore():
    v = mp.Value('i', 0)  # 定義共享變數
    p1 = mp.Process(target=job, args=(v, 1))
    p2 = mp.Process(target=job, args=(v, 3))  # 設定不同數字檢視共享變數的爭奪
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()
