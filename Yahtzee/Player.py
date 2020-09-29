class Player:

    def __init__(self,name):

        self.name = name
        self.scoreboard = {}

        self.top_score = 0
        self.bottom_score = 0
        self.top_bonus = 0
        self.bottom_bonus = 0
        self.total_score = 0

    def add_rolled(self, rolled_type, value):
        self.scoreboard[rolled_type] = value

    def add_top_score(self,value):
        self.top_score += value

    def add_bottom_score(self,value):
        self.bottom_score += value

    def add_top_bonus(self):

        needed_score_for_bonus = 63

        if self.get_top_score() >= needed_score_for_bonus:
            self.scoreboard['topbonus'] = 50
        else:
            self.scoreboard['top_bonus'] = 0

        self.top_bonus = self.scoreboard['top_bonus']

    def add_bottom_bonus(self):

        needed_score_for_bonus = 63

        if self.get_top_score() >= needed_score_for_bonus:
            self.scoreboard['bottombonus'] = 50
        else:
            self.scoreboard['bottom_bonus'] = 0

        self.bottom_bonus = self.scoreboard['bottom_bonus']

    def get_top_score(self):
        return self.top_score

    def get_bottom_score(self):
        return self.get_bottom_score

    def add_total_score(self):
        self.total_score = self.top_score + self.top_bonus + self.bottom_score + self.bottom_bonus

    def get_total_score(self):
        return self.total_score

    def print_scoreboard(self):
        for key, value in self.scoreboard.items():
            print(f'{key} : {value}')
