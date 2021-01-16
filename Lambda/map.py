nums = [1, 2, 3, 4, 5, 6, 7, 8]

square = list(map(lambda num: num * num, nums))

print(square)

names = ['Peter', 'Jane', 'Daniella', 'Augustine', 'Anna']

upper_names = list(map(lambda name: str.upper(name), names))

print(upper_names)

num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

add_list = list(map(lambda x, y : x + y, num1, num2))

print(add_list)