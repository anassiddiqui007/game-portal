import random
from Card import Card
from Deck import Deck
from Chips import Chips
from Hand import Hand

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have: {}'.format(chips.total))
            else:
                break

def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand,playing):

    while True:
        x = input('Hit or Stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry, I did not understand that, please enter h or s only!")
            continue
        break
    return playing

def show_some(player,dealer):

    print('DEALERS HAND:')
    print('one card hidden!')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND')
    for card in player.cards:
        print(card)

def show_all(player,dealer):

    print('DEALERS HAND:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(card)

def player_busts(player,dealer,chips):
    print("BUST Play")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('PLAYER WINS')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('PLAYER WINS! DEALER BUSTED!')

def dealer_wins(playwr,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and player tie! PUSH')


def play():

    while True:
        playing = True
        print('Welcome to Blackjack')

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chips()

        take_bet(player_chips)

        show_some(player_hand,dealer_hand)

        while playing:

            playing = hit_or_stand(deck,player_hand,playing)
            show_some(player_hand,dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break

            if player_hand.value <= 21:

                while dealer_hand.value < 17:
                    hit(deck,dealer_hand)

                show_all(player_hand,dealer_hand)

                if dealer_hand.value > 21:
                    dealer_busts(player_hand,dealer_hand,player_chips)
                elif dealer_hand.value > player_hand.value:
                    dealer_wins(player_hand,dealer_hand,player_chips)
                elif dealer_hand.value < player_hand.value:
                    player_wins(player_hand,dealer_hand,player_chips)
                else:
                    push(player_hand,dealer_hand)

            print('\n Player total chips are at {}'.format(player_chips.total))

        new_game = input("Would you like to play another hand? y/n")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print('Thank you for playing!')
            break

if __name__=='__main__':
    play()
