from collections import deque

s1 = deque()
s2 = deque()


def insert_to_stack(num):
    for _ in range(num):
        v = input("Enter item to add to stack")
        s1.append(v)


def reverse_stack(s):
    for _ in range(len(s)):
        s2.append(s1.pop())


inp = int(input("How many items do you wish to add to the stack ? : "))

insert_to_stack(inp)

print("Original stack below: ")
print(s1)
print("\nReversed stack")
reverse_stack(s1)
print(s2)