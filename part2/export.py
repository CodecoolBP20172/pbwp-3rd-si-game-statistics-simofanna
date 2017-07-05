import reports


def judy_answers_part2():
    file = open("game_stat_judy_answers_2.txt", "w")
    file.write(str(reports.get_most_played("game_stat.txt")))
    file.write("\n")
    file.write(str(reports.sum_sold("game_stat.txt")))
    file.write("\n")
    file.write(str(reports.get_selling_avg("game_stat.txt")))
    file.write("\n")
    file.write(str(reports.count_longest_title("game_stat.txt")))
    file.write("\n")
    file.write(str(reports.get_date_avg("game_stat.txt")))
    file.write("\n")
    file.write(str(reports.get_game("game_stat.txt", "Minecraft")))

judy_answers_part2()