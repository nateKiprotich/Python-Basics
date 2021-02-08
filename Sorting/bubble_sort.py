from lists import lst, tst


# Implementation using for loop
def bubble_sort(l):
    list_length = len(l)

    for i in range(list_length):
        for j in range(0, list_length - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l



sorted_lst = bubble_sort(lst)

print(sorted_lst)
