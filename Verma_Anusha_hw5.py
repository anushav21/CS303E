#Created by Anusha Verma, Feb 22 2023

#Lists
chicken_soup = ['chicken','chicken broth','carrots','celery','noodles']
lasagna = ['lasagna noodles','pasta sauce','ricotta']
grilled_cheese = ['bread','butter','cheese']
garden_salad = ['lettuce','tomatoes','carrots','olives']
anusha_special = ['feta','croutons','kale','onions','tofu']
recipe_names = 'Chicken Soup, '+'Lasagna, '+'Grilled Cheese, '+ 'Garden Salad, ' + 'Anusha\'s Special'    
grocery_list = []

#Chosen Recipe Function
def get_user_input(question,recipe_names):
    chosen_recipe = input(question + ' (Choose: ' + recipe_names + ') ',)
    return chosen_recipe

#Recipe Names Function
def get_recipe_list(chosen_recipe):
    if (chosen_recipe == 'Chicken Soup'):
        return chicken_soup
    elif (chosen_recipe == 'Lasagna'):
        return lasagna
    elif (chosen_recipe == 'Grilled Cheese'):
        return grilled_cheese
    elif (chosen_recipe == 'Garden Salad'):
        return garden_salad
    elif (chosen_recipe == 'Anusha\'s Special'):
        return anusha_special
print()

#First Ask With User Input Function
def first_ask():
    chosen_recipe = get_user_input('What would you like to make?',recipe_names)
    recipe_list = get_recipe_list(chosen_recipe)
    print()
    print(chosen_recipe + ': ', end = ' ')
    for ingredient in recipe_list:
        len_list = len(recipe_list)
        if(ingredient == recipe_list[len_list-1]):
            print(ingredient, end = ' ')
        else:
            print(ingredient + ', ', end = ' ') 
        grocery_list.append(ingredient)
first_ask()
print()
print()

#Main Function (Second Ask & User Grocery Choices)
def main():
    chosen_recipe = get_user_input('What else would you like to make?',recipe_names)
    print()
    recipe_list = get_recipe_list(chosen_recipe)
    print(chosen_recipe + ': ',end = ' ')
    for ingredient in recipe_list:
        len_list = len(recipe_list)
        if(ingredient == recipe_list[len_list-1]):
            print(ingredient, end = ' ')
        else:
            print(ingredient + ', ', end = ' ')
        grocery_list.append(ingredient)
    print()
    print()
    print('Grocery List:', end = ' ')
    len_glist = len(grocery_list)
    for i in range(len_glist):
        grocery = grocery_list[i]
        if(i == len_glist-1):
            print(grocery, end = '')
        else:
            print(grocery + ', ', end = ' ')
    print()
    print()
    #User's Customized Grocery List
    choose_ingredient = ''
    while (choose_ingredient != 'Done'):
        choose_ingredient = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished) ')
        if (choose_ingredient != 'Done'):
            grocery_list.append(choose_ingredient)
        print()
    print('Grocery List:', end = ' ')
    len_list = len(grocery_list)
    for i in range(len_list):
        grocery = grocery_list[i]
        if(i == len_list-1):
            print(grocery, end = '')
        else:
            print(grocery + ', ', end = ' ')

if __name__=='__main__':
    main()

    

