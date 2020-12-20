# Sets are un-ordered data dictionaries that remove deuplicates

my_set = {'Jan', 5, False, 'Daniella'}


print(type(my_set))
print(my_set)

# # remove() returns an error when item to be removed is not found
# my_set.remove('Oct')
# print(my_set)

# discard() does not return any error when item to be discarded is not found
my_set.discard('Oct')
print(my_set)


for item in my_set:
    print(item)


# Adding items
my_set.add('Age')

print(my_set)


# Add multiple values
my_set.update(['Gergioa', 'Washington', 'Nairobi'])
print(my_set)

# remove items.
# pop() removes items randomly
my_set.pop()
print(my_set)