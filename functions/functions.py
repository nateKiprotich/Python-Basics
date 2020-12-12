# positional arguments
# arguments must be passed using the same order as defined
def name_age(name, age):
    print("Name is :" + name)
    print("Age is : {}".format(age))


print(" ----- Positional arguments ----- ")
name_age("Nate", 29)


# Passing unknown number of arguments

def names(*name):

    for i in range(len(name)):
        print(name[i])


print(" ----- Unknown number of arguments ----- ")
names("Nathan", "Washington", "Jane", "George")


# default values
def d_name(name="Nate"):
    print(name)


print(" ----- Default values ----- ")
d_name()


# unknown number of keyword arguments

def details(**params):
    # print(params["fname"])
    print(params["lname"])
    print(params["age"])
    print(params["gender"])
    print(params["marital_status"])


print(" ----- Unknown number of arguments ----- ")
details(lname="Peter", gender="Male", age=30, marital_status="Single")
