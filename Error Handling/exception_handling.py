result = 0

while True:
    try:
        inp = int(input('Enter your age : '))
        break
    except ValueError:
        print("Please enter a number")

print(result)
