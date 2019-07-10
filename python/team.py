class Team:

    def __init__(self, name, rating):
        self.name = name
        self.conference = 'IND'
        self.rating = rating
        self.wins = 0
        self.losses = 0
        self.conf_wins = 0
        self.conf_losses = 0
        self.strength_of_record = 1.0
        self.wins_over = []
        self.losses_to = []

    def update_record(self, opponent, top_team_odds, win):
        old_sor = self.strength_of_record
        if win:
            self.wins_over.append(opponent.name)
            self.strength_of_record *= top_team_odds
            self.wins += 1
            if self.conference != 'IND' and opponent.conference == self.conference:
                self.conf_wins += 1
        else:
            self.strength_of_record = old_sor / top_team_odds + old_sor * top_team_odds
            self.losses_to.append(opponent.name)
            self.losses += 1
            if self.conference != 'IND' and opponent.conference == self.conference:
                self.conf_losses += 1

        print(self.name + ' record before playing ' + opponent.name + ': ' + str(old_sor))
        print(self.name + ' record after playing ' + opponent.name + ': ' + str(self.strength_of_record))
        print(win)

    def reset(self):
        self.wins = 0
        self.losses = 0
        self.conf_wins = 0
        self.conf_losses = 0
        self.strength_of_record = 1
        self.wins_over = []
        self.losses_to = []