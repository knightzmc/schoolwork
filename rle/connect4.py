import colours
from connect4_token import Token

EMPTY_TOKEN = Token("EMPTY", '○', colours.RESET, False)
FILLED_TOKEN_SYMBOL = '◉'
WIDTH = 6
HEIGHT = 7

# Board represented in x, y format. Eg board[3][4] represents the fifth row of the fourth column
# Fancy list comprehension :)
board = [[EMPTY_TOKEN for _ in range(WIDTH)] for _ in range(HEIGHT)]

RED_TOKEN = Token("RED", FILLED_TOKEN_SYMBOL, colours.RED)
BLUE_TOKEN = Token("BLUE", FILLED_TOKEN_SYMBOL, colours.BLUE)


def output_board_state():
    """
    Outputs each line of the board in a pretty format
    """
    for line in board:
        print('|', str.join(" | ", [token.get_formatted() for token in line]), '|')

    print('')


def apply_gravity():
    """
    Applies gravity to all tokens, bringing them down to their minimum possible y axis
    """
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


def get_highest_token(column) -> tuple:
    highest = EMPTY_TOKEN
    height = 0
    for row in board:
        height += 1
        tok = row[column]
        highest = tok
        if tok == EMPTY_TOKEN:
            return highest, height
    return highest, height


def play_game_round(turn) -> bool:
    col = input('Which column do you want to place a counter in?\n')
    try:
        column = int(col)
    except ValueError:
        print(f'Invalid column {col}. It should be a number')
        return play_game_round(turn)

    if column not in range(1, WIDTH + 1):
        print(f'Invalid column {col}. It should be between 1 and {WIDTH}')
        return play_game_round(turn)

    current, row = get_highest_token(column - 1)
    if current != EMPTY_TOKEN:
        print(f'Column {column} is full. Try again.')
        return play_game_round(turn)

    board[row - 1][column - 1] = turn

    apply_gravity()

    output_board_state()
    winner = check_for_valid_line()
    if winner is not None:
        print("Game Over!")
        print(f'{winner.identifier} is the winner!')
        return True

    return False


def check_for_valid_line():
    """
    for each token
    if there's a token to the right, increment the count by 1 and repeat with the token on the right
    if there's a token to the bottom right, increment the count by 1 and repeat with the token on the bottom right
    if there's a token below, increment the count by 1 and repeat with the token below
    Otherwise, reset the count and check the next token
    if there are more than 4, they win.
    """
    for row in range(0, HEIGHT):
        for col in range(0, WIDTH):
            token, length = check_for_lines_at(row, col)
            if length >= 4:
                return token
    return None


def check_for_lines_at(row, col, count=1, compare_to=None, direction=None) -> tuple:
    """
    This function is a bit of a hack, mainly because of the recursion.
    If calling from another function, all the default parameters should be used

    @type row: int
    @param row: The row to start checking for lines
    @type col: int
    @param col: The column to start checking for lines
    @param count: How long the line is so far
    @param compare_to: What each token should be compared to. Eg [BLUE_TOKEN] to check for lines of blue tokens
    @param direction: The current direction that we are travelling in to check
    """

    # Default value at the current slot
    if compare_to is None:
        compare_to = board[row][col]

    # No need to check for sequences of empty tokens
    if compare_to == EMPTY_TOKEN:
        return compare_to, 0

    if direction == 'right' or direction is None:
        # Check token to the right
        if col < WIDTH - 1:
            to_right = board[row][col + 1]
            if to_right == compare_to:
                return check_for_lines_at(row, col + 1, count + 1, compare_to, 'right')

    if direction == 'below' or direction is None:
        # Check token below
        if row < HEIGHT - 1:
            below = board[row + 1][col]
            if below == compare_to:
                return check_for_lines_at(row + 1, col, count + 1, compare_to, 'below')

    if direction == 'bottom_right' or direction is None:
        # Check token to the bottom right
        if col < WIDTH - 1 and row < HEIGHT - 1:
            bottom_right = board[row + 1][col + 1]
            if bottom_right == compare_to:
                return check_for_lines_at(row + 1, col + 1, count + 1, compare_to, 'bottom_right')

    if direction == 'top_right' or direction is None:
        # Check token to the top right
        if col < WIDTH and row > 0:
            bottom_right = board[row - 1][col + 1]
            if bottom_right == compare_to:
                return check_for_lines_at(row - 1, col + 1, count + 1, compare_to, 'top_right')
    return compare_to, count


def play():
    won = False
    while not won:
        print("Player 1's turn!")
        won = play_game_round(RED_TOKEN)
        if won:
            break
        print("Player 2's turn!")
        won = play_game_round(BLUE_TOKEN)


play()
