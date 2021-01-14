import threading
from threading import Lock

x = 0
"""
    Lock () ensures that only 1 thread which has acquired the lock is able to perform operation.
    Other threads wait for the lock to be released.
"""
lock = Lock()


def increment():
    global x
    lock.acquire()
    x += 1
    lock.release()

def operation():
    for _ in range(1000000):
        increment()


t1 = threading.Thread(target=operation, name="Thread #1")
t2 = threading.Thread(target=operation, name="Thread #2")

t1.start()
t2.start()

t1.join()
t2.join()

"""
     Expected value is 2 Million
     With the help of lock, every time the program executes, same value is returned
"""
print("Value of x is : " + str(x))
