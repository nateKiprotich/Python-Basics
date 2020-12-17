"""
    Immutables types:
        1. Numbers
        2. Floats
        3. Boolean
        4. Tuples

    Mutable objects:
        1. Lists
        2. Sets
        3. Dictionaries
"""

# immutable types example
x = 500

# print memory location of the variable

print(id(x))

# Update variable
x += 150

# memory location changes after the variable has been ammended
print(id(x))


# Mutable data types check

names = ['Pete', 'Jane', 'Andrew', 'Alice']

print(id(names))

names[0] = 'Derrick'

print(id(names))
