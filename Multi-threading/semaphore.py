import threading
import time
import random


semaphore = threading.Semaphore(5)
operation_counter = 0


def compute():
    global operation_counter

    semaphore.acquire()
    print("Performing computation" + ' - ' + str(operation_counter))
    operation_counter += 1
    time.sleep(random.randint(3, 8))
    print("compute operation complete")
    semaphore.release()
    operation_counter -= 1


while True:
    time.sleep(0.1)
    t = threading.Thread(target=compute)
    t.start()


