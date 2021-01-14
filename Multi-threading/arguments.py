import threading


def counter(x):
    for i in range(x):
        print(threading.current_thread().getName() + ' - ' + str(i))


"""
    parameters in args has to be a tuple. If the function takes only 1 argument,
    add a comma after the value i.e. (50, ) in the example below.
    Without the comma, the variable will be casted to string and it will cause
    TypeError.
"""

t1 = threading.Thread(target=counter, name="Thread #1", args=(50,))
t2 = threading.Thread(target=counter, name="Thread #2", args=(200,))

t1.start()
t2.start()
