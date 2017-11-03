#Draughts.py
#40167459
#27/10/2017
GRID_HEIGHT = 10
GRID_WIDTH = 10
#White Draught
WD = "%"
#White King
WK = '£'
#Empty Cell
EC = ' '
#Black Draught
BD = "&"
#Black King
BK = '$'
#players
PLAYERS = Enum("Players". "White Black")
#END OF CONSTANTS SECTION

def init_grid():
    """Initialize the new game grid"""
    grid = [[EC, BD, EC, BD, EC, BD, EC, BD, EC, BD],
            [BD, EC, BD, EC, BD, EC, BD, EC, BD, EC],
            [EC, BD, EC, BD, EC, BD, EC, BD, EC, BD],
            [BD, EC, BD, EC, BD, EC, BD, EC, BD, EC],
            [EC, EC, EC, EC, EC, EC, EC, EC, EC, EC],
            [EC, EC, EC, EC, EC, EC, EC, EC, EC, EC],
            [EC, WP, EC, WP, EC, WP, EC, WP, EC, WP],
            [WP, EC, WP, EC, WP, EC, WP, EC, WP, EC],
            [EC, WP, EC, WP, EC, WP, EC, WP, EC, WP],
            [WP, EC, WP, EC, WP, EC, WP, EC, WP, EC]]
    return grid
            
def move(value_package):
    """This function moves the pieces according to the player's wish"""
    print("Turn : ", value_package["turn_count"])
    if value_package["cur_turn"] == PLAYERS.White:
        print("White's turn :\n")
        print_board(value_package["board"])
        #Ask for command until the syntax is correct
        while True:
            print("Enter movement :", end="")
            if interpret_response(value_package["board"], input()) == True:
                value_package["cur_turn"] = PLAYERS.Black
                value_package["turn_count"] += 1
                break
    else:
        print("Black's turn :\n")
        #print_board(value_package["board"])
        #DO THE AI ACTION
        value_package["cur_turn"] = PLAYERS.White
        #value_package["turn_count"] += 1

def interpret_response(board, response):
    """This functon interprets the response"""
    if check_response_syntax(response):
        tuples = transform_response_into_tuples(response)
        if check_move_legality(board, tuples):
            return True
    else:
        print("Syntax Error")
    return False

def check_response_syntax(response):
    """This function checks if the syntax of the response is correct"""
    #Example of correct syntax: 7A6B OR 9F9F (Which is not a legal move !)
    return False if re.match("^([0-9][A-J]){2}$", response) == None else True

def transform_response_into_tuples(response):
    """This function decompose the response into tuples"""
    match = re.findall("([0-9][A-J]){1}", response)
    # -65 because ASCII A-Z to integers (remember A == 0 ...)
    # -48 because ASCII 1-9 to integers (remember 0 == 0 ...)
    l_val1 = ord(match[0][0]) - 48
    r_val1 = ord(match[0][1]) - 65
    l_val2 = ord(match[1][0]) - 48
    r_val2 = ord(match[1][1]) - 65
    return ((l_val1, r_val1), (l_val2, r_val2))

def check_move_legality(board, tuples):
    """This function checks if the move is legal"""
    return True

def print_board(board):
    """This function is drawing the board"""
    print("      A B C D E F G H I J\n")
    for i in range(GRID_HEIGHT):
        print(i, "   |", end="")
        for j in range(GRID_WIDTH):
            current_cell = board[i][j]
            print(current_cell + "|", end="")
        print("")
    print("")

def main():
    """ Entry point """
    CLEAR()
    print("PY-CHECKERS")
    value_package = dict([("board", init_grid()), ("turn_count", 1), ("cur_turn", PLAYERS.White)])
    while True:
        move(value_package)
