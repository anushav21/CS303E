#Team Member Names: Anusha Verma, Alyssa Capistran; Date: March 2, 2023; Group 32

#Function 1
def frame_this(list_of_words):
    print('*********')
    for word in list_of_words:
        if(len(word) == 5):
            print('* ' + word + ' *')
        elif(len(word) == 4):
            print('*  ' + word + '   *')
        elif(len(word) == 3):
            print('*  ' + word + '  *')
        elif(len(word) == 2):
            print('*   ' + word + '    *')
        elif(len(word) == 1):
            print('*    ' + word + '    *')
    print('*********')


#Function 2
def get_average(list_of_nums):
    length = len(list_of_nums)
    sum = 0
    for number in list_of_nums:
        sum+=number
    average = sum/length
    average = round(average)
    return average
  

#Function 3
def draw_three(list_of_cards):
    new_list_of_cards = []
    for i in range(3):
        new_list_of_cards.append(list_of_cards[i])
    return new_list_of_cards 

#Main Function
def main():
    my_words = ['Hello','apple','one']
    frame_this(my_words)
    my_numbers = [5,6,7,9]
    print(get_average(my_numbers))
    my_cards = ['2 of Hearts', '6 of Spades', 'Jack of Diamonds', 'Queen of Clubs', 'King of Clubs']
    print(draw_three(my_cards))
    
if __name__=='__main__':
   main()

 





