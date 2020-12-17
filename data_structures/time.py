import time

nums = []


start_time = time.time()

for i in range(100000):
    nums.append(i)

print("Append time is : %s" %(time.time() - start_time))

start_time = time.time()
nums = []

for i in range(100000):
    nums.insert(0,i)

print("Insert to start of list time is : %s " %(time.time() - start_time))