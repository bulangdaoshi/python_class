import threading
import time

globals_nums = 0

lock = threading.RLock()#实例化一个线程锁

def fun():

    lock.acquire()#获得线程锁

    global globals_nums

    globals_nums += 1

    time.sleep(1)

    print(globals_nums)

    lock.release()#释放线程锁

for i in range(10):
    t = threading.Thread(target=fun)#用for循环创建10个线程
    t.start()#线程启动