#Anusha Verma

import random
guess_number = int(input('What is your guess? '))
secret_number = random.randint(1,100)
counter = 1

while(guess_number != secret_number):
    counter +=1
    #Number is even
    if(guess_number > secret_number):
        if(guess_number % 2 == 0 and secret_number % 2 == 0):
            print(guess_number, 'is too high. But you are right that it is even!', end = ' ')
            guess_number = int(input('What is your guess? '))
        elif(guess_number % 2 != 0 and secret_number % 2 != 0):
            print(guess_number, 'is too high. But you are right that it is odd!', end = ' ')
            guess_number = int(input('What is your guess? '))
        else:
            print(guess_number, 'is too high.', end = ' ')
            guess_number = int(input('What is your guess? '))
    #Number is odd
    elif(guess_number < secret_number):
        if(guess_number % 2 == 0 and secret_number % 2 == 0):
            print(guess_number, 'is too low. But you are right that it is even!', end = ' ')
            guess_number = int(input('What is your guess? '))
        elif(guess_number % 2 != 0 and secret_number % 2 != 0):
            print(guess_number, 'is too low. But you are right that it is odd!', end = ' ')
            guess_number = int(input('What is your guess? '))
        else:
            print(guess_number, 'is too low.', end = ' ')
            guess_number = int(input('What is your guess? '))
print(guess_number, 'is correct! It took you', counter, 'guesses.')

