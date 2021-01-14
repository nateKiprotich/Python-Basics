import threading

x = 0

def increment():
    global x

    x += 1


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
     Because there is no synchronization, the value of x will be less than 2M
     Its non-deterministic (i.e. The value changes with each execution)
"""
print("Value of x is : " + str(x))
