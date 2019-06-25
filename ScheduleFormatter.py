with open('2017SchedulePreformat.csv', 'r') as file:
    lines = file.readlines()
    neutral_site_games = {29, 58, 4, 22, 77, 54, 52, 90, 91, 440, 683, 270, 534, 706}

    with open('2017Schedule.csv', 'w') as toFile:
        print(type(lines))
        for i in range(len(lines)):
            line = lines[i].split(',')
            if i in neutral_site_games:
                toFile.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[5] + ',' + line[6] + ',' + line[7] + ',' + line[8] + ',' + line[9] + ',' + line[10] + ',' + line[11] + '\n')
            else:
                toFile.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[5] + ',' + line[6] + ',' + line[7] + ',' + line[8] + ',' + line[9] + ',' + line[10] + ',\n')