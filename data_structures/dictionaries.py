
def line_break():
    print(60*'-')

person_details = {"name": "Pete", "gender": "male", "age": 35}

# the above variable initialization can be also done as below
#  person_details = dict("name": "Pete", "gender": "male", "age": 35)

print(person_details)

# Lenght of a dictionary
print(len(person_details))

# update values of dictionary
person_details["name"] = "Peter Daniel"
print(person_details)

# Add key values pair
person_details["children"] = 10
print(person_details)

# remove key values pair
del person_details["gender"]
print(person_details)

line_break()

# Iterate though the dictionary

# get keys
for key in person_details.keys():
    print(key)

line_break()

# Iterate values
for values in person_details.values():
    print(values)

line_break()

# iterate values and keys
for key, values in person_details.items():
    print(key + ": " + str(values))

line_break()

# Iterate key values with zip function
for key, values in zip(person_details.keys(), person_details.values()):
    print(key + ": " + str(values))

line_break()

# Dictionaries can also have dictionaries

person_details = {"name": {"first_name": "John", "last_name" : "Doe"}, "gender": "male", "age": 35}

print(person_details)

print(person_details["name"]["last_name"])