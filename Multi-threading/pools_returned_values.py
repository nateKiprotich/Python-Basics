import time
from concurrent.futures import ThreadPoolExecutor


def square(x):
    time.sleep(2)
    # print('The result: %s\n' % str(x*x))
    return  x*x


nums = [1, 2, 3, 4, 5]

# with ThreadPoolExecutor(max_workers=5) as executor:
#     executor.map(square, nums)
#

with ThreadPoolExecutor(max_workers=5) as executor:
    for value in nums:
        rslt = executor.submit(square, value)
        print(rslt)
        # print(rslt.result())
        # print(rslt)