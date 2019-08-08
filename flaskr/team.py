class Team:

    def __init__(self, name, rating):
        self.name = name
        self.conference = 'IND'
        self.division = 'IND'
        self.rating = rating
        self.wins = 0
        self.losses = 0
        self.conf_wins = 0
        self.conf_losses = 0
        self.playoff_berths = 0.0
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
            self.strength_of_record = self.strength_of_record / top_team_odds + self.strength_of_record * top_team_odds
            self.losses_to.append(opponent.name)
            self.losses += 1
            if self.conference != 'IND' and opponent.conference == self.conference:
                self.conf_losses += 1

    def reset(self):
        self.wins = 0
        self.losses = 0
        self.conf_wins = 0
        self.conf_losses = 0
        self.strength_of_record = 1
        self.wins_over = []
        self.losses_to = []

    def update_playoff_berths(self):
        self.playoff_berths += 1

    def get_playoff_odds(self, simulation_count):
        return self.playoff_berths / simulation_count

    def __str__(self):
        return 'Name: ' + self.name + ', Conf.:' + self.conference + ', Wins over: ' + str(self.wins_over) \
               + ', losses to: ' + str(self.losses_to) + ', SOR: ' + str(self.strength_of_record) + '\n'
