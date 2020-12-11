s = '1598761254'

# string slicing

"""
    prints characters from index 0 to 5. NB. Character at index 5 will not be printed
    Expected output: 15987
"""
print(s[0:5])

"""
    Slicing can be done from any index i.e.
    The below print starts fom index 5 upto end of the string
"""
print(s[5:])


"""
    Slicing can be done from any index i.e.
    The below print starts fom index 0 and ends on index 5 (5 is not inclusive)
    Similar to s[0:5
"""
print(s[:5])
