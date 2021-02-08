from lists import lst , tst


def insertion_sort(l):
    len_lst = len(l)

    tmp = l[0]
    pos = 0

    for i in range(len_lst):
        print(l)
        for j in range(len_lst):
            if l[j] < tmp:
                tmp = l[j]
                pos = j
                # print(j)
                # print(pos)
        # print(pos, i)
        l[i], l[pos] = tmp, l[i]
        if l[i] < len_lst:
            tmp = l[i + 1]

    # return l



print(insertion_sort(tst))