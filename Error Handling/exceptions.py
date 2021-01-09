try:
    a = "Peter is my name"
    b = 45

    a +b
except TypeError as err:
    # err is a class and thus functions within it can be called i.e. err.with_traceback()
    print(err)
finally:
    # This block will be executed regardless of the status of the above
    print('Finally block')


# Test division by zero
try:
    a = 0
    b = 45

    b/0
except ZeroDivisionError as err:
    # err is a class and thus functions within it can be called i.e. err.with_traceback()
    print(err)
finally:
    # This block will be executed regardless of the status of the above
    print('Finally block')