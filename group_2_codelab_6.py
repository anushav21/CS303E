#Created by Anusha Verma and Alyssa Capistran, April 13 2023

class Animal(): 
  def __init__(self, color, height):
    self.color = color
    self.height = height
    
  def __str__(self):
    return 'The ' + self.color + ' animal is ' + str(self.height) + ' inches tall.'

class Cat(Animal):
  def meow(self):
    print('The', self.color, 'cat is meowing.')
    
  def __str__(self):
    return super().__str__() + ' (Cat)'
    
class Dog(Animal): 
  def bark(self):
    if self.height > 15:
      print('The big' , self.color, 'dog says woof.')
    else:
      print('The small', self.color, 'dog says yip.')
  
  def __str__(self):
    return super().__str__() + ' (Dog)'

class Fish(Animal):
  def swim(self):
    print('The', self.color, 'fish is swimming.')
    
  def __str__(self):
    return super().__str__() + ' (Fish)'

class Rabbit(Animal):
  def hop(self):
    print('The', self.color, 'rabbit is hopping.')
    
  def __str__(self):
    return super().__str__() + ' (Rabbit)'
    
def main():
  garfield = Cat('orange', 12)
  garfield.meow()
  print(garfield)
  
  skip = Cat('white', 10)
  skip.meow()
  print(skip)

  buddy = Dog('golden', 14)
  buddy.bark()
  print(buddy)
  
  rex = Dog('grey', 16)
  rex.bark()
  print(rex)
  
  poseidon = Fish('blue', 2)
  poseidon.swim()
  print(poseidon)
  
  nemo = Fish('lavender', 3)
  nemo.swim()
  print(nemo)
  
  hopper = Rabbit('purple', 5)
  hopper.hop()
  print(hopper)
  
  sparkle = Rabbit('green', 11)
  sparkle.hop()
  print(sparkle)
  
if __name__ == '__main__':
  main()
