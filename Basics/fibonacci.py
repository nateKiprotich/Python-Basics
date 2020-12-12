"""
    Fibonacci numbers are numbers whose value is the sum of
    2 previous values.
    1 1 2 3 5 8 13 21 34 55 89

    Below implementation is fibonacci between 1 - 100
"""

# base values

a, b = 0, 1

# underscore operator is used when we do not need to use the counter
# Prints first 9 values of fibonacci
for _ in range(9):
    print(a)
    a, b = b, a +b

print('----------------------')
# Fibonacci numbers with value less than 150
a, b = 0, 1
while a < 150:
    print(a)
    a, b = b, a + b