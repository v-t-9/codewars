def points(games):
    total = 0
    for game in games:
        if int(game[0])>int(game[2]):
            total = total + 3
        if int(game[0])<int(game[2]):
            total = total
        if int(game[0])==int(game[2]):
            total = total + 1
    return total