from random import randint

DEAD = "."
LIVE = "#"
EDGE_CELL = "*"


def generate_board(size):
    board = []
    for row in range(size):
        cells = []
        for column in range(size):
            chance_of_life = randint(0,1)
            if chance_of_life == 1 :
                cells.append(LIVE)
            else:
                cells.append(DEAD)
        board.append(cells)
    return board


def expand_board(board):

    def add_column(index_):
        for cells in board:
            cells.insert(index_, DEAD)
        board[0][index_] = EDGE_CELL
        board[-1][index_] = EDGE_CELL

    def add_row(index_):
        edge_row = EDGE_CELL + " " + \
            ((DEAD + " ") * (len(board[0]) - 2)) + EDGE_CELL
        board.insert(index_, edge_row.split())

    if LIVE in board[1]:
        add_row(1)
    if LIVE in board[-2]:
        add_row(len(board) - 1)

    for cells in board:
        if cells[1] == LIVE:
            add_column(1)
        if cells[-2] == LIVE:
            add_column(len(cells)-1)

    return board


def display_board(board):
    for cells in board:
        print(" ".join(cells))
    print("\n")


def set_sentinels(board):
    for cells in board:
        cells.append(EDGE_CELL)
        cells.insert(0, EDGE_CELL)

    edge_rows = ((EDGE_CELL + " ") * (len(board) + 2)).strip()

    board.insert(0, edge_rows.split())
    board.insert(len(board) + 1, edge_rows.split())
    return board


def check_live_neighbours(x, y, board):
    num_live_cells = 0
    locations = [(1, 0), (1, 1), (0, 1), (-1, 1),
                 (1, -1), (-1, 0), (0, -1), (-1, -1)]
    for location in locations:
        if board[x + location[0]][y + location[1]] == LIVE:
            num_live_cells += 1
    return num_live_cells


def update_board_status(board):

    def update_cell_status():
        if board[x][y] == LIVE:
            if live_neighbours < 2 or live_neighbours > 3:
                board[x][y] = DEAD
                display_board(board)
        elif live_neighbours == 3:
            board[x][y] = LIVE
            display_board(board)

    for cells in board:
        for cell in cells:
            if cell != EDGE_CELL:
                x, y = board.index(cells), cells.index(cell)
                live_neighbours = check_live_neighbours(x, y, board)
                update_cell_status()
    return board


def run_game_of_life(num_of_times, default_board_size):
    default_board = generate_board(default_board_size)
    board = set_sentinels(default_board)
    display_board(default_board)

    for i in range(num_of_times):
        print("GENERATION ", i)
        board = update_board_status(board)
        board = expand_board(board)
        display_board(board)
        
    return board

display_board(run_game_of_life(5, 4))