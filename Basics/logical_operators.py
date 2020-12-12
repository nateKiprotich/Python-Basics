"""
    and - Both to be true
    or - Either to be true
    not - Reverse actual logical state
"""

a = 5
b = 15

if a <= 10 and a > 0:
    print(a, " is between [0,10]")

if a < 10 or b > 12:
    print("Logical operator evaluates to true is a is less than 10 or b is greater than 12")

c = True

# Prints opposite of the current boolean logical state
print(not c)