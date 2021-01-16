nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda num: num % 2 == 0, nums))

print(even_numbers)

odd_numbers = list(filter(lambda num: num % 2 != 0, nums))

print(odd_numbers)

names = ['Anna', 'Ben', 'Jane', 'Joe', 'Peter', 'Dan']

filtered_names = list(filter(lambda n: n[0] == 'J', names))

print(filtered_names)

filtered_names_1 = list(filter(lambda n: len(n) < 5, names))

print(filtered_names_1)
