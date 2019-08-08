import Settings

with open(Settings.data_folder_path + Settings.format_schedule_season + Settings.preformatted_schdedule_file_ending, 'r') as file:
    lines = file.readlines()

    with open(Settings.data_folder_path + Settings.format_schedule_season + Settings.schedule_file_ending, 'w') as toFile:
        for i in range(len(lines)):
            line = lines[i].split(',')

            for j in range(len(line) - 1):
                toFile.write(line[j] + ',')

            if i in Settings.neutral_site_games:
                toFile.write(line[len(line) - 1])
            else:
                toFile.write('\n')
