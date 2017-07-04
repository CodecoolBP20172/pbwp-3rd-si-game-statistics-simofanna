from statistics import mean


def organization(file_name):
    game_properties = []
    file = open(file_name, 'r')
    all_content = file.read().split('\n')
    for line in all_content:
        game = line.split('\t')
        if len(game) == 5:
            game[1] = float(game[1])
            game[2] = int(game[2])
            game_properties.append(game)
    file.close()
    return game_properties


def get_most_played(file_name):
    games = organization(file_name)
    max_played = 0
    for game_index in range(len(games)):
        if games[game_index][1] > games[max_played][1]:
            max_played = game_index
    return games[max_played][0]


def sum_sold(file_name):
    games = organization(file_name)
    sold_sum_list = []
    for game_index in range(len(games)):
        sold_sum_list.append(games[game_index][1])
    sold_sum_list = list(map(float, sold_sum_list))
    total_sold = sum(sold_sum_list)
    return total_sold


# eladott példányszámok átlaga return number
def get_selling_avg(file_name):
    games = organization(file_name)
    return sum_sold(file_name) / len(games)


def count_longest_title(file_name):
    pass


def get_date_avg(file_name):
    pass


def get_game(file_name, title):
    pass



