import Settings

def load_schedule(teams):
    schedule = []
    with open(Settings.season + 'Schedule.csv', 'r') as schedule_file:
        lines = schedule_file.readlines()
        for line in lines:
            game = line.split(',')
            name_a = game[5]
            name_b = game[8]
            for c in "()1234560789":
                name_a = name_a.replace(c, '')
                name_b = name_b.replace(c, '')
            name_a = name_a.strip()
            name_b = name_b.strip()
            if name_a in teams and name_b in teams:
                schedule.append({'home_team': name_b, 'visiting_team': name_a, 'week': game[1],
                             'neutral_site': bool(len(game[11]) > 0)})
            else:
                if name_a in teams:
                    name_b = name_a
                schedule.append({'home_team': name_b, 'visiting_team': 'FCS', 'week': game[1],
                                 'neutral_site': bool(len(game[11]) > 0)})
    return schedule
