lambda_function = lambda x=10, y=5: x + y

print(lambda_function())


lambda_function_1 = lambda  x, y: x + y

print(lambda_function_1(y=5, x=10))


# It can take any number of arguments
lambda_function_2 = lambda *args: sum(args)

print(lambda_function_2(2, 3, 5, 15, 90))


lambda_function_3 = lambda **args: sum(args.values())

print(lambda_function_3(one=1, two=2, eleven=11, fifty=50))