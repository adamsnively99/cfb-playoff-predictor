import Settings
import string_formatter

# Returns schedule of CFB games in season
def load_schedule(teams):
    schedule = []
    with open(Settings.data_folder_path + Settings.format_schedule_season + Settings.schedule_file_ending, 'r') \
            as schedule_file:
        lines = schedule_file.readlines()
        for line in lines:
            game = line.split(',')
            if len(game[7]) > 0 and game[7] != '\n':
                name_a = game[5]
                name_b = game[8]
            else:
                name_a = game[8]
                name_b = game[5]
            name_a = string_formatter.format_team_name(name_a, "()1234560789")
            name_b = string_formatter.format_team_name(name_b, "()1234560789")
            if name_a in teams and name_b in teams:
                schedule.append({'home_team': name_b, 'visiting_team': name_a, 'week': game[1],
                             'neutral_site': bool(len(game[11]) > 0)})
            else:
                if name_a in teams:
                    name_b = name_a
                schedule.append({'home_team': name_b, 'visiting_team': 'FCS', 'week': game[1],
                                 'neutral_site': bool(len(game[11]) > 0)})
    return schedule




