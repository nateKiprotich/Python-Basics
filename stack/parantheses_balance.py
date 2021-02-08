from collections import deque

bracket_list = ['{', '}', '[', ']', '(', ')']

brackets = deque()

while True:
    inp = input("Enter parentheses randomly. ")

    c = 'x'
    if inp not in bracket_list:
        c = input("Press Y to continue adding items. N to stop")

    if c.lower() == 'n':
        break

    brackets.append(inp)

print(brackets)

