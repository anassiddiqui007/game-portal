import random
from collections import Counter
class Roll:

    def __init__(self):
        self.current_dice_list = []
        self.current_kept_dice = []

    def roll_dice(self):
        self.current_kept_dice.clear()
        self.current_dice_list = [random.randint(1,6) for die in range(0,5)]
        print(f'You rolled {self.current_dice_list} !')
        return self.current_dice_list

    def keep_dice(self):
        user_input = input('Which dice do you want to keep? (comma separated: e.g. 1,1,5)? ')
        split_input = user_input.split(',')

        if user_input == '':
            return self.current_dice_list

        for item in split_input:
            value = int(item)
            if value in self.current_dice_list:
                self.current_kept_dice.append(value)
                self.current_dice_list.remove(value)

        return self.current_dice_list

    def reroll_dice(self, dice_list):
        self.current_dice_list = [random.randint(1,6) for die in range(0,(len(dice_list)))]
        print(f'You rolled {self.current_dice_list} !')
        return self.current_dice_list

    def get_current_dice(self):
        return self.current_dice_list

    def get_kept_dice(self):
        return self.current_kept_dice

    def forced_keep(self,dice_list):
        for dice in dice_list:
            self.current_kept_dice.append(dice)

    def single_values(self,dice_list,check_value):
        roll_score = 0
        for dice in dice_list:
            if dice == check_value:
                roll_score += dice
        return roll_score

    def check_one_pair(self,dice_list):
        myCounter = Counter(dice_list)
        return 2 in myCounter.values()

    def check_two_pair(self,dice_list):
        myCounter = Counter(dice_list)
        return list(myCounter.values()).count(2) == 2

    def check_three_kind(self,dice_list):
        myCounter = Counter(dice_list)
        return 3 in myCounter.values()

    def check_four_kind(self,dice_list):
        myCounter = Counter(dice_list)
        return 4 in myCounter.values()

    def check_low_straight(self,dice_list):
        return set(dice_list) == set([1,2,3,4,5])

    def check_high_straight(self,dice_list):
        return set(dice_list) == set([2,3,4,5,6])

    def check_full_house(self,dice_list):
        myCounter = Counter(dice_list)
        if len(myCounter) != 2:
            return False
        if 2 not in myCounter.values():
            return False
        return True

    def add_chance(self,dice_list):
        pass

    def check_yahtzee(self,dice_list):
        return len(set(dice_list))==1

    def get_bottom_score(self,dice_list):

        bottom_score = 0

        if self.check_yahtzee(dice_list):
            bottom_score += 30

        if self.check_full_house(dice_list):
            bottom_score += 20

        if self.check_low_straight(dice_list):
            bottom_score += 15

        if self.check_high_straight(dice_list):
            bottom_score += 15

        if self.check_four_kind(dice_list):
            bottom_score += 15

        if self.check_three_kind(dice_list):
            bottom_score += 10

        if self.check_two_pair(dice_list):
            bottom_score += 10

        if self.check_one_pair(dice_list):
            bottom_score += 5

        return bottom_score
