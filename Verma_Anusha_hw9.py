#Created by Anusha Verma, April 8 2023

#Check if a number is prime or not using a function and passing a 'num' parameter
def is_prime(num):
  #If the number is less than 2 return False
  if num < 2:
      return False
  #Use a counter variable and set it to one less than num
  counter = num-1
  #Loop through the counter while it is greater than 1 and until it is equal to the counter value 
  while(counter > 1):
    #If the counter value divides the number evenly, it is not a prime number. If it is not prime, return false
    if num % counter == 0:
      return False
    #Decrement the counter variable by 1
    counter -= 1
  #If no number less than num is a factor then num is prime. Return true if this is the case.
    return True

#Count the number of primes by passing a list called list_of_primes as the parameter
def count_primes(list_with_primes):
    #Set a variable called primes to 0
    primes = 0
    #Loop through list_of_primes to count the primes
    for x in list_with_primes:
        #Call on the is_prime function to check if x is prime
        if(is_prime(x)):
            #Increment the primes variable by 1 if x is prime
            primes += 1
    #Return the total number of primes in the list
        return primes

#Sort the sorting_list using bubble sort to increasing order
def bubble_sort(sorting_list):
  #Set the length of sortin_list to the variable n
  n = len(sorting_list)
  #Loop through the range of the length of the sorting list minus 1
  for i in range(n-1):
    #For number at position i, loop through the range from 0 to one minus the number at position i
    for j in range(0, n-i-1):
      #Check if the value in the sorting list at j is greater than the number to the right
      if sorting_list[j] > sorting_list[j + 1] :
        #Swap the numbers at position j and j+1
        sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]

#Get the average of the numbers in the list of numbers called list_to_average
def get_average(list_to_average):
  #Set a variable called total to 0 
  total = 0
  #Loop through the numbers in list_to_average
  for i in list_to_average:
    #Increment the total variable by one
    total = total + i
  #Return the total divided by the length of the list_to_average and round this to the nearest whole number
  return round(total/len(list_to_average))
  
#Main function in the program
def main():
  #Initialize a list called user_list to an empty list
  user_list = []
  #Set a variable called user_num to ask for the user's input. Ask them to input a number and to enter 'Done' when finished
  user_num = input('Enter a number (type "Done" when finsished): ')
  #Loop through the user's input while the input is not equal to 'done'
  while(user_num.lower() != 'done'):
    #Use a 'try' to deal with non-numerical input from the user
    try:
      #Convert the user's input to an integer
      user_num = int(user_num)
      #Append the user_num value to the list called user_list
      user_list.append(user_num)
    #Handle value error while converting user input to an integer using 'except'
    except ValueError as err:
      #Handle the value error by printing the error 
      print(err,'That was not a number!')
    #Set a variable called user_num equal to the user's input. Ask them to enter numbers and enter 'done' when finished
    user_num = input('Enter another number (type "Done" when finsished): ')
    
  #Print out the list called user_list
  print('Your list:',user_list)
  #Print out the number of primes in the user_list by calling on the count_primes function and passing in user_list as an argument
  print('Your list has',count_primes(user_list),'primes')
  #Print out the average of the numbers in user_list by calling on the get_average function and passing in user_list as an argument
  print('Average:',get_average(user_list))
  #Call on the bubble_sort function and pass in user_list as an argument
  bubble_sort(user_list)
  #Print out the sorted version of user_list
  print('Your list sorted:',user_list)

#check if this is the main module
if __name__=="__main__":
  #run the main function (which should always run first)
  main()
