import multiprocessing as mp


def job(x):
    return x*x #使用pool時所處理的工作可以有回傳值

def multicore():
    pool = mp.Pool(processes=2) #processes 可以指定使用核心數，預設為全部核心
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    print(res.get())
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])


if __name__ == '__main__':
    multicore()
