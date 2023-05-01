#Created by Anusha Verma & Alyssa Capistran; March 24, 2023

def max_word_length(words_list):
  longest_word = words_list[0]
  for i in range(1,len(words_list)):
    word = words_list[i]
    if len(word)>len(longest_word):
      longest_word=word
  return len(longest_word)

def frame_this(list_of_words):
  longest_word_len = max_word_length(list_of_words)
  for i in range(longest_word_len+4):              
    print('*',end='')
  print()
  for word in list_of_words:
    number_of_spaces = (longest_word_len+2)-len(word)
    number_of_spaces_before_word = int(number_of_spaces/2)
    number_of_spaces_after_word = (number_of_spaces-number_of_spaces_before_word)
    print('*',end='')
    for j in range(number_of_spaces_before_word):
      print(' ',end='')
    print(word,end='')
    for j in range(number_of_spaces_after_word):
      print(' ',end='')
    print('*')
  for i in range(longest_word_len+4):
    print('*',end='')
  print('')  

def is_prime(num):
  if(num < 2):
    return False
  i=2
  while(i<=num-1):
    if(num % i == 0):
     return False
    i+=1
  return True

def count_primes(list_of_numbers):
  i=0
  for number in list_of_numbers:
    if is_prime(number):
      i+=1
  return i  
  
def make_list(string_of_text):
  new_list = string_of_text.split(', ') 
  return new_list  

def main():
  list_of_names = ['Anusha','Alyssa']
  frame_this(list_of_names)
  
  words_to_split = 'one, two, three, four hundred'
  words_list = make_list(words_to_split)
  frame_this(words_list)
  numbers = [1,9,0,2,3,17,6,25,4,5,11,14]
  print('The list of numbers',numbers,'has',count_primes(numbers),'primes.')
  
if __name__=="__main__":
  main()
