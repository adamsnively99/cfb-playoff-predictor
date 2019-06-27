import Settings

with open(Settings.data_folder_path + Settings.format_schedule_season + Settings.preformatted_schdedule_file_ending, 'r') as file:
    lines = file.readlines()

    with open(Settings.data_folder_path + Settings.format_schedule_season + Settings.schedule_file_ending, 'w') as toFile:
        for i in range(len(lines)):
            line = lines[i].split(',')
            if i in Settings.neutral_site_games:
                toFile.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[5] + ',' + line[6] + ',' + line[7] + ',' + line[8] + ',' + line[9] + ',' + line[10] + ',' + line[11])
            else:
                toFile.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[5] + ',' + line[6] + ',' + line[7] + ',' + line[8] + ',' + line[9] + ',' + line[10] + ',\n')
