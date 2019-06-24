import Settings


# Returns schedule of CFB games in season
def load_schedule(teams):
    schedule = []
    with open(Settings.season + 'Schedule.csv', 'r') as schedule_file:
        lines = schedule_file.readlines()
        for line in lines:
            game = line.split(',')
            name_a = game[5]
            name_b = game[8]
            name_a = format_name(name_a)
            name_b = format_name(name_b)
            if name_a in teams and name_b in teams:  # TODO: Fix neutral site calculations for seasons 2018 and before
                schedule.append({'home_team': name_b, 'visiting_team': name_a, 'week': game[1],
                             'neutral_site': bool(len(game[11]) > 0)})
            else:
                if name_a in teams:
                    name_b = name_a
                schedule.append({'home_team': name_b, 'visiting_team': 'FCS', 'week': game[1],
                                 'neutral_site': bool(len(game[11]) > 0)})
    return schedule


def format_name(name):
    for c in "()1234560789":
        name = name.replace(c, '')
    return name.strip()
