class Algorithm:
    a_msg = "All algorithms should be optimized"


class Sort(Algorithm):
    s_msg = "Sort your issues"


s_v = Sort()

print(s_v.s_msg)

# We are able to use variables
print(s_v.a_msg)