with open('2016SchedulePreformat.csv', 'r') as file:
    lines = file.readlines()
    neutral_site_games = {0, 21, 34, 42, 44, 82, 45, 30, 86, 149, 275, 284, 325, 382, 436, 529, 604}

    with open('2016Schedule.csv', 'w') as toFile:
        print(type(lines))
        for i in range(len(lines)):
            line = lines[i].split(',')
            if i in neutral_site_games:
                toFile.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[5] + ',' + line[6] + ',' + line[7] + ',' + line[8] + ',' + line[9] + ',' + line[10] + ',' + line[11] + '\n')
            else:
                toFile.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[5] + ',' + line[6] + ',' + line[7] + ',' + line[8] + ',' + line[9] + ',' + line[10] + ',\n')