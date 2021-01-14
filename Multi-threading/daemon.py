import threading


def normal_operation():
    for i in range(1000000):
        print( threading.current_thread().getName() + ' - ' + str(i) + '. Normal Operation')


def daemon_operation():
    counter = 0
    while True:
        print(threading.current_thread().getName() + ' - ' + str(counter) + '. Deamon Operation')
        counter += 1


"""
    Even though the daemon function is an infinite loop, it will be terminated as soon as the 
    normal (non daemon operation is complete)
"""
t1 = threading.Thread(target=normal_operation, name="Normal Thread")
t2 = threading.Thread(target=daemon_operation, name="Deamon Thread", daemon=True)

t1.start()
t2.start()
