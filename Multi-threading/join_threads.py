"""
    Thread joins are used to pause MainThread until the threads with joins
    have completed execution
"""

import threading


def counter():
    for i in range(100):
        print(threading.current_thread().getName() + ' - ' + str(i))


t1 = threading.Thread(target=counter, name="Thread #1")
t2 = threading.Thread(target=counter, name="Thread #2")

t1.start()
t2.start()

t1.join()
t2.join()

# Without the joins above, the below print() executes before both threads are complete
print("\n Thread execution complete")
