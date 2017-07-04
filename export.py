import reports


def judy_answers():
    file = open("game_stat_answers.txt", "w")
    file.write(str(reports.count_games("game_stat.txt")))
    file.write("\n")
    file.write(str(reports.decide("game_stat.txt", "1999")))
    file.write("\n")
    file.write(str(reports.get_latest("game_stat.txt")))
    file.write("\n")
    file.write(str(reports.count_by_genre("game_stat.txt", "Real-time strategy")))
    file.write("\n")
    file.write(str(reports.get_line_number_by_title("game_stat.txt", "Counter-Strike: Condition Zero")))
    file.write("\n")
    file.write(str(reports.sort_abc("game_stat.txt")))
    file.write("\n")
    file.write(str(reports.get_genres("game_stat.txt")))
    file.write("\n")

judy_answers()
