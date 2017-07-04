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


def get_most_played(file_name):
    games = organization(file_name)
    max = 0
    for game_index in range(len(games)):
        if games[game_index][1] > games[max][1]:
            max = game_index
    return games[game_index][0]


