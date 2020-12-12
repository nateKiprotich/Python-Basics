"""
    compare two numbers
"""

a = 19
b = 20

if a < b:
    output_str = "{} is greater than {}"
    print(output_str.format(b, a))
elif a > b:
    output_str = "{} is less than {}"
    print(output_str.format(b, a))
else:
    output_str = "{} is equals to {}"
    print(output_str.format(b, a))

# Even numbers

a = 9

if a % 2 == 0:
    print(a, " is even number")
else:
    print(a, " is not even number")


# Largest number when all the values compared are not equal to one another
# a simple implementation
a = 6
b = 15
c = 3

if a > b and a > c:
    print(a, " is the largest number")
elif b > a and b > c:
    print(b, " is the largest number")
else:
    print(c, " is the largest number")