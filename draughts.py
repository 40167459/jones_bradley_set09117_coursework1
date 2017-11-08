#Draughts.py
#40167459
#Bradley Jones
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

#END OF CONSTANTS SECTION

#Defines the game board
"""Initialize the new game grid"""
grid = [[EC, BD, EC, BD, EC, BD, EC, BD, EC, BD],
        [BD, EC, BD, EC, BD, EC, BD, EC, BD, EC],
        [EC, BD, EC, BD, EC, BD, EC, BD, EC, BD],
        [BD, EC, BD, EC, BD, EC, BD, EC, BD, EC],
        [EC, EC, EC, EC, EC, EC, EC, EC, EC, EC],
        [EC, EC, EC, EC, EC, EC, EC, EC, EC, EC],
        [EC, WD, EC, WD, EC, WD, EC, WD, EC, WD],
        [WD, EC, WD, EC, WD, EC, WD, EC, WD, EC],
        [EC, WD, EC, WD, EC, WD, EC, WD, EC, WD],
        [WD, EC, WD, EC, WD, EC, WD, EC, WD, EC]]


def print_board(grid):
    acc = 0
    print(" 0 1 2 3 4 5 6 7 8 9 10 ")
    for row in grid:
        print(acc, row)
        acc = acc + 1
