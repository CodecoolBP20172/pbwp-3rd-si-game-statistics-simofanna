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


def get_selling_avg(file_name):
    games = organization(file_name)
    return sum_sold(file_name) / len(games)


def count_longest_title(file_name):
    games = organization(file_name)
    title_list = []
    for game_index in games:
        title_list.append(game_index[0])
    return len(max(title_list, key=len))


def get_date_avg(file_name):
    games = organization(file_name)
    date_list = []
    for game_index in games:
        date_list.append(game_index[2])
    return round((sum(date_list)) / (len(date_list)))


def get_game(file_name, title):
    games = organization(file_name)
    for game_index in games:
        if game_index[0] == title:
            return game_index



