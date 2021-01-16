from functools import reduce

nums = [1, 5, 6, 15, 10]

rd = reduce(lambda x, y: x + y, nums)

print(rd)


rds = reduce(lambda x, y: x + y, range(1,100,1))

print(rds)