num = [15, 16, -3, 98, 126, 78, 36, 3, -2, 18]

# sort
num = sorted(num)
print(num)

# sort Descending
num = sorted(num, reverse=True)
print(num)

names = ['Pete', 'Doe', 'Jane', 'Mercy', 'Grace', 'Harry', 'Potter']

# Same sort as above applies.

# sorting based on length of string


def name_sorter(x):
    return len(x)


names = sorted(names, key=name_sorter)

print(names)


# Dictionaris

details = {'Pete': 98, 'Doe': 78, 'Jane': 88, 'Mercy':96, 'Grace': 73, 'Harry': 87, 'Potter': 100}

# sort function based on marks i.e. value of dictionary
def value_sorter(x):
    return x[1]


sort_dict = sorted(details.items(), key=value_sorter)

print(sort_dict)

sort_dict = sorted(details.items(), key=value_sorter, reverse=True)

print(sort_dict)


def key_sorter(x):
    return x[0]


sort_dict = sorted(details.items(), key=key_sorter)

print(sort_dict)

sort_dict = sorted(details.items(), key=key_sorter, reverse=True)

print(sort_dict)