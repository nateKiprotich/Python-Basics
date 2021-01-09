"""
    Enumerate returns the index and value when looping
    It eliminates the use of an additional variable to keep track of indexes
"""

food = ['Pilau', 'Githeri', 'Managu', 'White Rice']


for index, value in enumerate(food):
    print(str(index) + " " + str(value))
