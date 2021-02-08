"""
    program accepts two parameters.
        1. List of numbers
        2. target number - Any sum of values should from list (1 above)
            should give the target

    return value should be index of 2 numbers
"""


def get_target(l, t):

    list_length = len(l)

    for i in range(list_length):
        for j in range(list_length):
            if l[j] == t - l[i]:
                return i, j


def main():

    lst = [2, 11, 7, 15, 7]
    target = 9

    a, b = get_target(lst, target)

    print(a, b)


if __name__ == "__main__":
    main()


