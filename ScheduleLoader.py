def load_schedule(teams):
    schedule = []
    with open('2019Schedule.csv', 'r') as schedule_file:
        lines = schedule_file.readlines()
        for line in lines:
            game = line.split(',')
            if game[8] in teams and game[5] in teams:
                schedule.append({'home_team': game[8], 'visiting_team': game[5], 'week': game[1],
                             'neutral_site': bool(len(game[11]) > 0)})
            #else:
                #print('game not entered')
                #print(game[8])
                #print(game[5])
    return schedule
