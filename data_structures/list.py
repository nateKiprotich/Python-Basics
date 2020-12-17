
def show_fav_food():
    print(30*"-")
    for food in favourite_food:
        print(food)


favourite_food = ['Chapati', 'Pilau', 'Spaghetti', 'Ugali Fish', 'Chips']
drinks = ['Coca Cola', 'Mursik', 'Tea']

# print items in the list
show_fav_food()

# Update list items
favourite_food[3] = 'Ugali Matumbo'
show_fav_food()

# remove items in a list
del favourite_food[4]
show_fav_food()


# Add items to list
favourite_food.append("Chips Masala")
show_fav_food()

# Concatenate Lists
food_drinks = favourite_food + drinks
print(food_drinks)

# Lists can also be concatenated as shown below
favourite_food.extend(drinks)
print(favourite_food)


# Built in functions
favourite_food.remove('Chapati')

favourite_food.pop()
print(favourite_food)


favourite_food.reverse()
print(favourite_food)

favourite_food.sort()
print(favourite_food)
