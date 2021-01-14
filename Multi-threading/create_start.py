import threading

def counter():
    for i in range(101):
        print(threading.current_thread().getName() + ' - ' + str(i))


t1 = threading.Thread(target=counter, name = 'Thread 1')
t2 = threading.Thread(target=counter, name = 'Thread 2')

t1.start()
t2.start()
