#Created by Anusha Verma, April 1

import random
class Duck:
    def __init__(self,name):
        self.name = name
        self.speed = int(random.uniform(4,7))
        self.max_distance = random.uniform(6,10)
    def __str__(self):
        return self.name + ' Speed: ' + str(self.speed) + ' Max Distance ' + str(self.max_distance)
        
class Race:
    def __init__(self,distance):
        self.distance = distance
        print('Race Distance:',self.distance)
    def start_race(self,list_of_ducks):
        self.list_of_ducks = list_of_ducks
        for duck in list_of_ducks:
            print(duck)
    def winner_of_race(self):
        list_of_ducks = self.list_of_ducks
        qualified_duck_list = []
        for duck in list_of_ducks:
            if (duck.max_distance >= self.distance):
                qualified_duck_list.append(duck)
        if(len(qualified_duck_list) == 0):
            return 'No Winner'
        winner_duck = qualified_duck_list[0]
        for duck in qualified_duck_list:
            if(duck.speed > winner_duck.speed):
                winner_duck = duck
        return 'Winner: '+ winner_duck.name
    
def main():
    race = Race(7)
    duck_0 = Duck('Duck 0')
    duck_1 = Duck('Duck 1')
    duck_2 = Duck('Duck 2')
    duck_3 = Duck('Duck 3')
    duck_4 = Duck('Duck 4')
    race.start_race([duck_0,duck_1,duck_2,duck_3,duck_4])
    print(race.winner_of_race())
    duck_0 = Duck('Duck 0')
    duck_1 = Duck('Duck 1')
    duck_2 = Duck('Duck 2')
    duck_3 = Duck('Duck 3')
    duck_4 = Duck('Duck 4')
    duck_5 = Duck('Duck 5')
    duck_6 = Duck('Duck 6')
    duck_7 = Duck('Duck 7')
    race.start_race([duck_0,duck_1,duck_2,duck_3,duck_4,duck_5,duck_6,duck_7])
    print(race.winner_of_race())
if __name__=="__main__":
    main()
   

  
        
    
    
