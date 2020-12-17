numbers = [5, 15, 9, 10, 96, 58, 66, 27, 47, 63]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# the above loop can be replaced by the line below
even_num = [num for num in numbers if num % 2 == 0]

print(even_num)


names = ['Peter', 'George', 'Daniel', 'Billy', 'Anna', 'Edgar', 'Dan', 'Daniella']

name_d = [name for name in names if name.startswith('D')]
print(name_d)

name_5_chars = [name for name in names if len(name) == 5]
print(name_5_chars)
