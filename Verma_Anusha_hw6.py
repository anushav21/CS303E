#Created by Anusha Verma, March 4 2023
def get_average(list_of_num):
  total = 0
  for i in list_of_num:
    total = total + i
  avg = total
  try:
    avg = avg/len(list_of_num)
  except ZeroDivisionError as err:
    print('Error message: ',err) 
  avg = round(avg)
  return avg
  
def main():
  numbers = ['one','two','three']
  try:
    print(get_average(number))
  except NameError as err:
    print('Error message: ',err)
  greeting = 'Hello World'
  for i in range(len(greeting)+1):
    try:
      print(greeting[i])
    except IndexError as err:
      print('Error message: ', err)
  numbers = []
  print(get_average(numbers))
  try:
    print(numbers[10])
  except IndexError as err:
    print('Error message: ', err)
  try:
    color = int(input('Enter your favorite color: '))
  except ValueError as err:
    print('Error message: ', err)
  
if __name__=="__main__":
  main()
