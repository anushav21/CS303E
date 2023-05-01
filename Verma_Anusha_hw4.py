def add_space_and_capitalize(word):
  new_word = '' #TODO: create a variable called new_word which starts as an empty string
  for letter in word: #TODO: write a for-loop that loops through each letter of the word passed as a parameter
    new_word = new_word + letter.upper() + ' ' #TODO: for each letter, make it uppercase using .upper() and then add that letter to the new_word variable and add a space after it
  return new_word #TODO: return the new_word variable...do not print anything here, only return
   
  
def accrue_interest(loan_amount):
  loan_balance = loan_amount #TODO: create a variable called loan_balance which starts with a value equal to the loan_amount parameter
  loan_interest = 0.06*loan_amount #TODO: create a variable called loan_interest which is 6% of the loan_amount (ie. multiply loan_amount by .06)
  loan_balance = loan_balance + loan_interest#TODO: update the loan_balance variable by adding the loan_interest to it
  return loan_balance #TODO: return the loan_balance variable (do not print anything here, only return)
  
def make_payment(loan_balance,payment_amount):
  remaining_balance = 0#TODO: create a variable called remaining_balance which starts as 0
  if(loan_balance <= payment_amount):#TODO: write an if-statement to check if the loan balance is less than or equal to the payment amount
    print('Paid off!')#TODO: if the loan balance is less than or equal to the payment amount that means the loan is paid off, so print "Paid Off!"
  else:#TODO: write an else to handle the other case (meaning the loan was not paid off)
   remaining_balance = loan_balance - payment_amount #TODO: inside the else, update the remaining_balance variable by setting it to the loan_balance minus the payment_amount
   print('Paid ${0:.2f}'.format(payment_amount))#TODO: still inside the else, print "Paid $__" using .format to fill in the amount that was paid, using two decimals
  return remaining_balance #TODO: now return the remaining_balance variable (make sure this is outside the if-else block)
  
def display_balance(loan_balance):
  print('Current Balance: ${0:.2f}'.format(loan_balance))#TODO: print "Current Balance: $__" using .format to fill in the loan_balance with two decimals
  
#### DO NOT CHANGE ANYTHING BELOW THIS LINE###
def main():
  big_text = 'finance'
  print(add_space_and_capitalize(big_text))
  loan = 12000
  display_balance(loan)
  loan = accrue_interest(loan)
  display_balance(loan)
  loan = make_payment(loan,2000)
  display_balance(loan)
  loan = accrue_interest(loan)
  display_balance(loan)
  loan = make_payment(loan,12000)
  display_balance(loan)
  
if(__name__=="__main__"):
  main()
