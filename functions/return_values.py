
def total(*num):
    s = 0

    for i in range(len(num)):
        s += num[i]
    return s

# total function takes in any number of arguments


t = total(2, 3, 6, 48)

print(t)
