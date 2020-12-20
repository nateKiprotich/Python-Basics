# Collections holds implementation of data structures
import collections

# Double linked list variable
linked_list = collections.deque([])

# Append values to the linked list variable. Appends to end of list
linked_list.append('56')
linked_list.append('John')
linked_list.append(5)

print(linked_list)

# Append values to the start of the list

linked_list.appendleft('Test')

print(linked_list)

print("\n Values of linked list after items have been removed \n")

"""
    pop function removes last item while popleft removes first item
"""

linked_list.pop()
print(linked_list)
linked_list.popleft()
print(linked_list)


# Though linked list cannot be accesssed by index, python abstracts this.

print(linked_list[1])
