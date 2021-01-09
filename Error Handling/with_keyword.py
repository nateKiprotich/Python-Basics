
try:
    with open('test.txt', 'r') as file:
        for line in file:
            print(line)
except FileExistsError as err:
    print('File does not exists')