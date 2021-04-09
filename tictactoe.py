def print_game():
    print('---------')
    print('| ' + game_state[0] + ' ' + game_state[1] + ' ' + game_state[2] + ' |')
    print('| ' + game_state[3] + ' ' + game_state[4] + ' ' + game_state[5] + ' |')
    print('| ' + game_state[6] + ' ' + game_state[7] + ' ' + game_state[8] + ' |')
    print('---------')


def get_winner(row):
    if row[0] == row[1] == row[2]:
        return row[0]
    else:
        return '_'


def analyse_game():
    win_conditions = [game_state[0:3], game_state[3:6], game_state[6:9]]
    win_conditions += [[game_state[0], game_state[3], game_state[6]]]
    win_conditions += [[game_state[1], game_state[4], game_state[7]]]
    win_conditions += [[game_state[2], game_state[5], game_state[8]]]
    win_conditions += [[game_state[0], game_state[4], game_state[8]]]
    win_conditions += [[game_state[2], game_state[4], game_state[6]]]

    winners = []
    for condition in win_conditions:
        w = get_winner(condition)
        if w != '_':
            winners.append(w)

    if len(winners) == 0:
        if game_state.count('_') == 0:
            return 'Draw'
        else:
            return 'Game not finished'
    else:
        return winners[0] + ' wins'


def is_valid(i):
    return game_state[i] == '_'


def apply_move(i, c):
    return game_state[:i] + c + game_state[i + 1:]


def get_users_move():
    while True:
        s = input('Enter the coordinates (row, col):')

        if len(s) < 3:
            print('You should enter numbers!')
            continue

        if not s[0].isnumeric() or not s[2].isnumeric():
            print('You should enter numbers!')
            continue

        n1 = int(s[0])
        n2 = int(s[2])

        if not 0 < n1 < 4 or not 0 < n2 < 4:
            print('Coordinates should be from 1 to 3!')
            continue

        index = (n1 - 1) * 3 + (n2 - 1)
        if is_valid(index):
            return index
        else:
            print('This cell is occupied! Choose another one!')


game_state = '_________'
print_game()
winner = "Game not finished"
moveId = 'X'

while winner == "Game not finished":
    move = get_users_move()
    game_state = apply_move(move, moveId)
    print_game()
    winner = analyse_game()

    if moveId == 'X':
        moveId = 'O'
    else:
        moveId = 'X'

print(winner)
