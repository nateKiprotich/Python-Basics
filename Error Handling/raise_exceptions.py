age = 13

try:
    if age < 18:
        raise Exception("You are underage")
        # Below exception will return a tuple which can be iterated to get elements at any index
        # raise  Exception("You are underage", 18, "should be accompanied by parent")
except Exception as exception:
    print(exception)
