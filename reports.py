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