# for loop
# prints numbers from 0 - 9. 10 is not inclusive
print('-----***********--------')
for num in range(10):
    print(num)

print('-----***********--------')

# prints 1 - 9
for num in range(1,10):
    print(num)

print('-----***********--------')

# prints 1,4,7
# step value of 3 has been used in this case
for num in range(1,10,3):
    print(num)

print('-----***********--------')

name  = 'doormaker'

idx = 0

while idx < len(name):
    print(name[idx])
    idx += 1