#Created by Anusha Verma & Alyssa Capistran, April 8 2023

import random
class Card:
    def __init__(self,suit,value):
        self.value = value
        self.suit = suit
    def __str__(self):
        return str(self.value) + ' of ' + self.suit
    def get_value(self):
        if(self.value == 'Ace'):
            return 11
        elif(self.value == 'Jack' or self.value == 'Queen' or self.value == 'King'):
            return 10
        else:
            return int(self.value)
            
class DeckOfCards:
    def __init__(self):
        self.deck = []
        suits = ['Clubs','Spades','Diamonds','Hearts']
        for suit in suits:
            for number in range(2,11):
                card = Card(suit,str(number))
                self.deck.append(card)
            jack = Card(suit,'Jack')
            self.deck.append(jack)
            queen = Card(suit,'Queen')
            self.deck.append(queen)
            king = Card(suit,'King')
            self.deck.append(king)
            ace = Card(suit,'Ace')
            self.deck.append(ace)
    def print(self):
        for card in self.deck:
            print(card)
    def shuffle(self):
        self.draw_next = -1
        random.shuffle(self.deck)
    def draw_card(self):
        self.draw_next+=1
        return self.deck[self.draw_next]
        
class Dealer:
     def __init__(self):
         self.name = 'Dealer'
         self.hand = []
     def __str__(self):
        return self.name + ': ' + str(self.hand[0]) + '; ' + str(self.hand[1]) + ';'
class Player:
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.hand = []
    def __str__(self):
        return self.name + ': ' + str(self.hand[0]) + '; ' + str(self.hand[1]) + ';'
   

def deal_round(players,dealer,card_deck):
    card_deck.shuffle()
    for player in players:
        player.hand = []
    dealer.hand = []
    for i in range(2):
        for player in players:
            player.hand.append(card_deck.draw_card())
        dealer.hand.append(card_deck.draw_card())
    print(dealer)
    for player in players:
        print(player)
    
def get_winners(players,dealer):
    dealer_score = dealer.hand[0].get_value() + dealer.hand[1].get_value()
    for player in players:
        player_score = player.hand[0].get_value() + player.hand[1].get_value()
        if player_score>dealer_score:
            player.money +=5
            print(player.name + ' won! ' + player.name + ' now has $' + str(player.money))
        elif player_score<dealer_score:
            player.money -=5
            print(player.name + ' lost...' + player.name + ' now has $' + str(player.money))
    
def main():
    deck = DeckOfCards()
    list_of_players = []
    new_dealer = Dealer()
    player_1 = Player('Sonia',100)
    player_2 = Player('Alex',50)
    player_3 = Player('Anusha',200)
    player_4 = Player('Alyssa',200)
    list_of_players.extend([player_1,player_2,player_3,player_4])
    deal_round(list_of_players,new_dealer,deck)
    get_winners(list_of_players,new_dealer)
    deal_round(list_of_players,new_dealer,deck)
    get_winners(list_of_players,new_dealer)
    
if __name__=="__main__":
    main()
