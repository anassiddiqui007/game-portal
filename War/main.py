from Card import Card
from Deck import Deck
from Player import Player

def play():

    player_one = Player("One")
    player_two = Player("Two")

    new_deck = Deck()
    new_deck.shuffle()

    for x in range(26):
        player_one.add_cards(new_deck.deal())
        player_two.add_cards(new_deck.deal())

    game_on = True
    round_number=0
    while game_on:
        round_number += 1
        print(f"Round {round_number}")

        if len(player_one.all_cards) == 0:
            print('Player One, out of cards! Player Two Wins!')
            game_on = False
            break

        elif len(player_one.all_cards) == 0:
            print('Player One, out of cards! Player Two Wins!')
            game_on = False
            break

        player_one_cards = []
        player_one_cards.append(player_one.remove_one())
        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True

        while at_war:

            if player_one_cards[-1].value > player_two_cards[-1].value:

                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False

            elif player_one_cards[-1].value < player_two_cards[-1].value:

                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False

            else:
                print('WAR!')

                if len(player_one.all_cards) < 5:
                    print('Player One unable to declare war')
                    print('Player Two wins!')
                    game_on = False
                    break

                elif len(player_two.all_cards) < 5:
                    print('Player TWO unable to declare war')
                    print('Player One wins!')
                    game_on = False
                    break

                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

if __name__=='__main__':
    play()
