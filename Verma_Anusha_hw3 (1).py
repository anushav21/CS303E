#Task One
favorite_animal = input('Favorite animal? ')
for letter in favorite_animal:
    print(letter)
print("")

#Task Two
chosen_number = input('Pick a number: ')
chosen_number = int(chosen_number)
i = 0
while (i <= chosen_number):
    print(i, end = " ") 
    i += 1
print("")

#Task Three
print("")
food_of_choice = input('Pick an option of soup, salad, or sandwich: ')
while (food_of_choice.lower() != 'soup' and food_of_choice.lower() != 'sandwich' and food_of_choice.lower() != 'salad'):
    food_of_choice = input('Sorry that\'s not an option!')
print('Ok, you picked ', food_of_choice, '!', sep = '')




