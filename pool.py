from multiprocessing import *
import time
def worker(msg):
    time.sleep(2)
    print(msg)

pool = Pool()
for i in range(20):
    msg = 'hello %d'%i
    pool.apply_async(func=worker,args=(msg,))

pool.close()

pool.join()