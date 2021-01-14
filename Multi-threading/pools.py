from concurrent.futures import ThreadPoolExecutor
import time


def operation():
    time.sleep(2)
    print('The operation is finished ...')


executor = ThreadPoolExecutor(max_workers=8)

executor.submit(operation)
executor.submit(operation)
executor.submit(operation)
executor.submit(operation)
executor.submit(operation)

executor.shutdown()

