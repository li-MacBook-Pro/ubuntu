import threading
a = 0
b = 1000000
lock = threading.Lock()
def jia0():
    lock.acquire()  #  加锁
    for i in range(b):
        global a
        a += 1
    print('first:',a)
    lock.release() # 解锁
def jia1():
    lock.acquire()  #  加锁
    for i in range(b):
        global a
        a += 1
    print('second:{}'.format(a))
    lock.release() # 解锁
def foo():
    while 1:
        print(threading.current_thread().getName())
def main():
    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=foo)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__ == '__main__':
    # first = threading.Thread(target=jia0)
    # second = threading.Thread(target=jia1)
    # first.start()
    # first.join() # 线程等待
    # second.start()
    main()