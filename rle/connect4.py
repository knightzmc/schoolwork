import colours


class Token:
    def __init__(self, symbol, colour, is_player = True):
        self.symbol = symbol
        self.colour = colour
        self.is_player = is_player

    def get_formatted(self):
        return self.colour + self.symbol + colours.RESET


EMPTY_TOKEN = Token('○', colours.RESET, False)
TOKEN = '◉'

# Board represented in x, y format. Eg board[3][4] represents the fifth row of the fourth column
board = [
    [EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN],
    [EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN],
    [EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN],
    [EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN],
    [EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN],
    [EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN],
    [EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN, EMPTY_TOKEN],
]
COLOUR_1 = Token(TOKEN, colours.RED)
COLOUR_2 = Token(TOKEN, colours.BLUE)


def output_board_state():
    for line in board:
        print('|', str.join(" | ", [token.get_formatted() for token in line]), '|')

    print('')


def apply_gravity(board):
    for index, row in enumerate(board):
        if index >= len(board) - 1:
            continue

        next_row = board[index + 1]

        for elem_index, elem in enumerate(row):
            if elem == EMPTY_TOKEN:
                continue
            if next_row[elem_index] == EMPTY_TOKEN:
                row[elem_index] = EMPTY_TOKEN
                next_row[elem_index] = elem


def play(colour, x, y):
    board[x][y] = colour
    output_board_state()


def get_highest_token(column):
    highest = EMPTY_TOKEN
    height = 0
    for row in board:
        height += 1
        tok = row[column]
        highest = tok
        if tok == EMPTY_TOKEN:
            return highest, height
    return highest, height


def play_game_round(turn):
    col = input('Which column do you want to place a counter in?\n')
    try:
        column = int(col)
    except ValueError:
        print(f'Invalid column {col}. It should be a number')
        return play_game_round(turn)

    if column not in range(1, 7):
        print(f'Invalid column {col}. It should be between 1 and 6')
        return play_game_round(turn)

    current, row = get_highest_token(column - 1)
    if current != EMPTY_TOKEN:
        print(f'Column {column} is full. Try again.')
        return play_game_round(turn)

    board[row - 1][column - 1] = turn
    apply_gravity(board)

    output_board_state()


def check_for_valid_line(board):
    """
    for each token
    if there's a token to the right, increment the count by 1 and repeat with the token on the right
    if there's a token to the bottom right, increment the count by 1 and repeat with the token on the bottom right
    if there's a token below, increment the count by 1 and repeat with the token below
    Otherwise, reset the count and check the next token
    if there are more than 4, they win.
    """
    count = 1
    for row in board:
        for index, token in enumerate(row):
            if row[index + 1] == token:
                count = count + 1

    pass


while True:
    print("Player 1's turn!")
    play_game_round(COLOUR_1)
    print("Player 2's turn!")
    play_game_round(COLOUR_2)
