def fib(num):
    a, b = 0, 1

    for _ in range(num):
        print(a)
        a, b = b, a + b


number = int(input("How many fibonacci number do you require ? "))
fib(number)