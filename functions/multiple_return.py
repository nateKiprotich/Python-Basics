def total_avg(*num):
    s = 0
    l = len(num)

    for i in range(l):
        s += num[i]

    return s, (s/l)

# total function takes in any number of arguments


total, avg = total_avg(2, 3, 6, 48)

print(total)
print(avg)

rslt = total_avg(2, 3, 6, 48, 78)

print(rslt[0])
print(rslt[1])
