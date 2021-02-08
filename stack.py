from collections import deque

stk = deque()

stk.append('a')
stk.append('b')
stk.append('c')

print(stk)

# for _ in range(len(stk)):
stk.pop()

print(type(stk))

deque(stk)

print(stk)