#Introduction
print('Welcome, chosen one, to the Tangled universe! The kingdom of Corona is searching for the lost princess, and we believe that you can help! Your future and destiny await!')
print('')
print('To begin this mission, you must choose a companion. Pascal, a mighty chameleon, is quick and versatile. Maximus, a mighty horse, is proud and loyal. Finally, Duck, though small, is wise and cautious.')
print('')
animal_companion = input('Which companion, Pascal, Maximus, or Duck, would you like to chose to have by your side during your journey?')

#First pathway (pascal)
if(animal_companion.lower() == 'pascal'):
    print('')
    print('You chose', animal_companion.lower(), 'and your task is to rescue princess Rapunzel from the tower.')
    print('')
    position_direction = input('To move forward on this journey, will you take a right or a left from your current position? Enter in the word right to go right, and left to go left.')
    #First Subpath (pascal)
    if(position_direction.lower() == 'right'):
        print('')
        print('Amazing choice! You have made it to the tower! Continue on, warrior! Use pascal\'s help to scale up the tower!')
        save_the_princess = input('Once in the tower, choose whether you will cut off the princess\'s hair or if you will fight the evil Mother Gothel. Type in \'option one\' for the first option, and \'option two\' for the second option. Dont forget to be courageous and brave in either option you choose!')
        print('')
        escape_route = input('Excellent choice - it is clear you thought well! Now, decide whether you will use the tower to escape or if you will use the seceret passageway. Enter in \'tower\' for the first choice and \'secret\' for the second choice.')
        if (save_the_princess.lower() == 'option one' or escape_route.lower() == 'tower'):
            print('')
            print('You have successfully completed your mission, wise one! Your decisions allowed the princess to be free of Mother Gothel\'s control, and to escape from the tower in a deft and swift way to return back to the kingdom. You will be greatly rewarded for your efforts! Until next time.') 
        elif(save_the_princess.lower() == 'option two' or escape_route.lower() == 'secret'):
            print('')
            print('Though dangerous and risky, your decisions have resulted in great payoffs! You, your companion Pascal, and princess Rapunzel have all safely retured to the kingdom of Corona. Congratulate yourself on your brave and valient efforts and keep fighting for good!')
        else:
            print('')
            print('Invalid response, player. You must choose a decision for this mission.')
    #Second Subpath (pascal)
    elif(position_direction.lower() == 'left'):
        print('')
        print('You decided on going', position_direction.lower(), 'but you have been led astray! Instead of the tower, you are in the valley of poisonous spiders. In order to get out, decide whether you will use the vines above you to swing over the valley, or if you will swim around the area to get to the other side.')
        valley_escape_route = input('To use the vines, type in \'vines\', and to swim in the water, type \'swim\'.')
        if(valley_escape_route.lower() == 'vines'):
            print('')
            print('Brave decision! You have succesfully swung over the deathly spiders and made it to the tower.')
            climbing_tower = input('Now, as your last step, decide whether you will use the ladder to the left to get up the tower or if you will use the picks in your pocket. Enter in \'ladder\' for the first choice and \'picks\' for the second option.')
            if(climbing_tower.lower() == 'ladder' or climbing_tower.lower() == 'picks'):
                print('')
                print('You have completed the mission! Amazing, wonderful, spectacular job! You, the princess, and Maximus will be welcomed to the kingdom of Corona with a huge celebration.')
            else:
                print('Invalid response, player.')
        elif(valley_escape_route.lower() == 'swim'):
            print('')
            desert_island = input('Though your swimming skills saved you from having to plunge through the valley of spiders, you ended up in a stranded desert island, 55 miles from the tower. Choose whether you will build a boat to sail to the tower or if you will swim to a nearby village and call for help. Enter in \'one\' for the first option, and \'two\' for the second option.')
            if(desert_island.lower() == 'one'):
                print('')
                print('With great courage and resilience, you survived these ordeals. The boat you built allowed you to quickly reach to the tower and return to the kingdom of Corona with the princess. Congratulate yourself on a job well done.')
            elif(desert_island.lower() == 'two'):
                print('')
                print('You tried hard to escape from the island and ended up on a nearby village infiltrated by pirates. Unfortunately, they took your money, belongings, and even Pascal. You were not able to complete your mission, and the kingdom of Corona continues to search for their lost princess.')
            else:
                print('Invalid response, player.')  
        else:
            print('Invalid response, player.')
    #Third Subpath (invalid input)
    else:
        print('Invalid response, player.')
        
#Second pathway (maximus)              
elif(animal_companion.lower() == 'maximus'):
    print('')
    print('Wise choice. You and your trusty steed will now need to help Flynn Rider escape from the palace guards.')
    route_choice = input('Which route do you wish to go on - your options are one of the following: \'Treacherous Tower\' or the \'Garden of the Snakes\'.')
    #First Subpath (maximus)
    if(route_choice.lower() == 'treacherous tower'):
        print('')
        print('This pathway is filled with pirates. Proceed with caution, and make sure you and Maximus keep your belongings safe.')
        pirate_path = input('You must now choose whether you will use go around this path, through the forest, to avoid the pirates or if you will blend in with the crowd and go through this path. Type in \'first option\' or \'second option\' for what you choose.')
        print('')
        time_of_journey = input('You must also decide whether you will start now or in 5 hours, when the sun comes up. Type in \'now\' for the first option and type in \'sun\' for the second choice.')
        if(pirate_path.lower() == 'first option' and time_of_journey.lower() == 'sun'):
            print('')
            print('You successfully took advantage of the light that the sun provided and used your surroundings to tactfully dodge the pirates. You made it to the castle, and helped Flynn Rider escape. Congratulations!')
        elif(pirate_path.lower() == 'second option' or time_of_journey.lower() == 'now'):
            print('')
            print('Unfortunately, you failed to complete the task and were attacked by the pirates. You were not able to rescue Flynn Rider from the castle :(.')
        else:
            print('Invalid response, player.')
    #Second Subpath (maximus)
    elif(route_choice.lower() == 'garden of the snakes'):
        print('')
        snake_color = input('This route is deadly and tricky. It splits off into two paths. One has red snakes and one has purple, with one type having a poisonous venom and one being harmless. Type in \'purple\' to chose the purple snake route and type in \'red\' for the red snake route.')
        if(snake_color.lower() == 'purple'):
            print('')
            palace_entrance = input('You have made it through the gardern succesfully. The purple snakes were not venomous, and you made it out uninjured. Now, you are at the palace entrance. Choose whether you will enter from the top ceiling or if you will pretend to be a guard to sneak into the palace. Type in the number 1 for the first option and the number 2 for the second option.')
            if(palace_entrance.lower() == '1'):
                print('')
                print('This was a stealthy and well thought out choice. You succesfully made it inside the castle without being caught and helped Flynn Rider escape from the clutches of the palace guards. You will earn 5 gold coins for this mission. Well done, chosen one!')
            elif(palace_entrance.lower() == '2'):
                print('')
                print('Unfortunately, you were caught by the guards as someone suspected your efforts to infiltrate the castle. You have failed your mission!')
            else:
                print('Invalid response, player.')
        elif(snake_color.lower() == 'red'):
            print('')
            medicinal_flower = input('Unfortunately, the red snakes turned out to be poisonous. You have hit a major snag in your journey to the castle. However, there are two plants near you. One is the white loutus, medicinal flower that can cure your snake bites. The other is the purple hibiscus, which will cause the injuries to worsen. Type in either \'white lotus\' or \'purple hibiscus\'.')
            if(medicinal_flower.lower() == 'white lotus'):
                print('')
                print('Very wise choice! Your injuries healed, and the magic in the flower allowed you to gain strength to make to to the castle and rescue Flynn Rider! Hooray!')
            elif(medicinal_flower.lower() == 'purple hibiscus'):
                print('')
                print('Unfortunately, this flower only caused your injuries to worsen. You were not able to make to the castle in time to save Flynn Rider from the palace:(.')
            else:
                 print('Invalid response, player.')
    #Third Subpath (maximus)
    else:
        print('Invalid response, player.')
      
#Third pathway (duck)
elif(animal_companion.lower() == 'duck'):
    print('')
    print('Thoughtful choice. Your task at hand is to retrieve the golden crown.')
    print('')
    infiltration_option = input('Now, choose whether you will infiltrate the palace through the ceiling or the secret back door. For the first option, enter the number 1 and for the second option, enter the number 2.')
    #First Subpath (duck)
    if(infiltration_option.lower() == '1'):
        print('')
        steal_the_crown = input('Excellent decision. You succesfully lowered yourself to the golden crown. Now, you must decide whether you will pick the lock of the box the crown is locked in, or if you will use a hammer to smash it. Type in \'pick lock\' or \'smash with hammer\'.')
        if(steal_the_crown.lower() == 'pick lock'):
            print('')
            print('You chose', steal_the_crown.lower(), 'and you have opened up the box without being caught!')
            real_or_fake_crown = input('However, the castle has 2 crowns - one is the real golden crown, and one is a fake. Will you choose to take the crown in front of you or do you think this one is the fake? Type in \'option one\' for the first option, and \'option two\' for the second option.')
            if(real_or_fake_crown.lower() == 'option one'):
                print('')
                print('Unfortunately, this crown was a fake. You have failed the mission.')
            elif(real_or_fake_crown.lower() == 'option two'):
                print('')
                print('Wise choice. You spotted the fake crown and were able to take the real crown! Congrats!')
            else:
                print('Invalid response, player.')
        elif(steal_the_crown.lower() == 'smash with hammer'):
            print('')
            escape_from_the_guards =  input('You managed to open the box, but smashing it alerted the guards. Now, will you escape through the back door or will you hide behind the curtains on the left. Enter in \'option one\' for the first choice and \'option two\' for the second choice.')
            if(escape_from_the_guards.lower() == 'option one'):
                print('')
                print('Congrats! You swiftly grabbed the crown and deftly escaped through the back door without being seen by the guards. Awesome job, player!')
            elif(escape_from_the_guards.lower() == 'option two'):
                print('')
                print('Unfortunately, your cover was blown and the guards caught you - you have failed to complete your mission.')
            else:
                print('Invalid response, player.')
        else:
            print('Invalid response, player.')
    #Second Subpath (duck)
    elif(infiltration_option.lower() == '2'):
        print('')
        tunnel_direction = input('The secret back door led you to a tunnel within the walls of the castle. The crown is nearby somewhere, but you must choose if you will take a right or a left. Type in \'right\' or \'left,\' and choose wisely. The palace guards are on the lookout!')
        if(tunnel_direction.lower() == 'right'):
            print('')
            door_to_crown = input('You managed to dodge the guards so far! There are two large doors in front of you, and behind one is the coveted golden crown. You must decide whether you will open the red door or the yellow door. Type in either \'red\' or \'yellow\'.')
            if(door_to_crown.lower() == 'yellow'):
                print('')
                print('Amazing job! You have completed your mission. The crown was behind the yellow door, and you managed to get it! Congrats!')
            elif(door_to_crown.lower() == 'red'):
                print('')
                print('Unfortunately, the crown was not behind the red door. You have been captured by the guards and did not manage to complete the mission.')
            else:
                print('Invalid response, player')
        if(tunnel_direction.lower() == 'left'):
           print('')
           lost_in_the_tunnels = input('Oh no! You are now lost in the tunnels! Will you keep moving forward or will you climb up the stairs to the left? Type in \'move forward\' or \'climb the stairs\'.')
           if(lost_in_the_tunnels.lower() == 'move forward'):
               print('')
               print('You have failed to complete your mission. Moving forward made you even more lost within the tunnels and you were not able to steal the golden crown :(.')
           elif(lost_in_the_tunnels.lower() == 'climb the stairs'):
               print('')
               print('Excellent choice! You made it up the stairs and right to the location of the crown. You managed to take the crown and escape without being seen! Hooray!')
           else:
               print('Invalid response, player.')
    #Third Subpath (invalid input)
    else:
        print('Invalid response, player.')
        
#Fourth pathway (invalid input)        
else:
    print('Invalid response, player. You must choose a companion for this mission.')



    
          
    


    
    

