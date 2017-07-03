def organization(file_name):
    game_properties = []
    file = open(file_name, 'r')
    all_content = file.read().split('\n')
    for line in all_content:
        game = line.split('\t')
        if len(game) == 5:
            game_properties.append(game)
    file.close()
    return game_properties


def count_games(file_name):
    games = organization(file_name)
    return(len(game))


def decide(file_name, year):
    games = organization(file_name)
    for game_index in range(len(games)):
        if games[game_index][2] == year:
            return True
    return False


def get_latest(file_name):
    games = organization(file_name)
    latest_game_index = 0
    for game_index in range(len(games)):
        if games[game_index][2] > games[latest_game_index][2]:
            latest_game_index = game_index
        return(games[latest_game_index][0])


def count_by_genre(file_name, genre):
    genre_sum = 0
    games = organization(file_name)
    for game_index in range(len(games)):
        if games[game_index][3] == genre:
            genre_sum += 1
    return(genre_sum)


def get_line_number_by_title(file_name, title):
    games = organization(file_name)
    title_index_number = 0
    for game_index in range(len(games)):
        if title == games[game_index][0]:
            return game_index + 1
    raise ValueError('game not in the file')


def sort_abc(file_name):
    game_title_list = []
    for game_index in games:
        game_title_list.append(game_index[0])
    game_title_list.sort()
    return game_title_list


def get_genres(file_name):
    pass


def when_was_top_sold_fps(file_name):
    pass
