#Draughts.py
#40167459
#Bradley Jones
#27/10/2017

grid_height = 8
grid_width = 8
#White Draught
WD = "%"
#White King
WK = '£'
#Empty Cell
EC = '_'
#Black Draught
BD = "&"
#Black King
BK = '$'
#players

#END OF CONSTANTS SECTION

#def main():
   

#Defines the game board
"""Initialize the new game grid"""
grid = [[BD, EC, BD, EC, BD, EC, BD, EC],
        [EC, BD, EC, BD, EC, BD, EC, BD],
        [BD, EC, BD, EC, BD, EC, BD, EC],
        [EC, EC, EC, EC, EC, EC, EC, EC],
        [EC, EC, EC, EC, EC, EC, EC, EC],
        [EC, WD, EC, WD, EC, WD, EC, WD],
        [WD, EC, WD, EC, WD, EC, WD, EC],
        [EC, WD, EC, WD, EC, WD, EC, WD]]

#Prints the board
def print_board(grid):
    acc = 0
    print("   0    1    2    3    4    5    6    7   ")
    for row in grid:
        print(acc, row)
        acc = acc + 1

def move():
    start_x = int(input("Enter an x coord for where to move from"))
    start_y = int(input("Enter a y coord for where to move from"))
    end_x = int(input("Enter an x coord for where to move to"))
    end_y = int(input("Enter a y coord for where to move to"))
    if grid[start_y][start_x] == EC:
        print("Empty cell selected try again")
        return wrong_move()
    if grid[start_y][start_x] == BD:
        grid[start_y][start_x] = EC
        grid[end_y][end_x] = BD


def jump():
