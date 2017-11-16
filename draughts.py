#Draughts.py
#40167459
#Bradley Jones
#27/10/2017
from enum import Enum
grid_height = 8
grid_width = 8
#White Draught
WD = "w"
#White King
WK = 'W'
#Empty Cell
EC = '_'
#Black Draught
BD = "b"
#Black King
BK = 'B'
#players
Players = Enum("Players", "White Black")
#END OF CONSTANTS SECTION

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



def main(grid):
    value_package=dict([("grid", grid),("cur_turn",Players.White)])
    while True:
        print_board(grid)
        move(value_package, grid)
        break


#Prints the board
def print_board(grid):
    acc = 0
    print("    0    1    2    3    4    5    6    7   ")
    for row in grid:
        print(acc, row)
        acc = acc + 1

def move(value_package, grid):
    if value_package["cur_turn"] == Players.White:
        print_board(grid)
        print("White Turn\n")
        start_x = int(input("Enter an x coord for where to move from: "))
        start_y = int(input("Enter a y coord for where to move from: "))
        #When error handling for when an empty cell is selected
        if grid[start_y][start_x] == EC:
            print("Empty cell selected try again")
            return move(value_package, grid)
        if grid[start_y][start_x] == BD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
        if grid[start_y][start_x] == BK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
    
        end_x = int(input("Enter an x coord for where to move to: "))
        end_y = int(input("Enter a y coord for where to move to: "))
        #Define Mid points here
        midval_x = abs(start_x + end_x) // 2
        midval_y = abs(end_y + end_y) // 2
        if Turns["Turn"] == players.White:

        #Error handling
        #For when an occupied cell is selected
        if grid[end_y][end_x] == BD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
        if grid[end_y][end_x] == WD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
        if grid[end_y][end_x] == BK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
        if grid[end_y][end_x] == WK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
        #Else indicates the start of the movement logic   
        else:

            if end_x > start_x + 2:
                print("Can not move that far away")
                return move(value_package, grid)

            if end_x < start_x - 2:
                print("Can not move that far away")
                return move(value_package, grid)

            if end_y > start_y + 2:
                print("Can not move that far away")
                return move(value_package, grid)

            if end_y < start_y - 2:
                print("Can not move that far away")
                return move(value_package, grid)

            if grid[start_x] == grid[end_x]:
                print("You can only move diagonally")
                return move(value_package, grid)

            if grid[start_x] == grid[end_x]:
                print("You can only move diagonally")
                return move(value_package, grid)

            else:
                grid[start_y][start_x] = EC
                grid[end_y][end_x] = WD
                value_package["cur_turn"] = Players.Black
                return move(value_package, grid)


    
    if value_package["cur_turn"] == Players.Black:
        print_board(grid)
        print("Black Turn\n")
        start_x = int(input("Enter an x coord for where to move from: "))
        start_y = int(input("Enter a y coord for where to move from: "))
        #Define Mid points here
        midval_x = abs(start_x + end_x) // 2
        midval_y = abs(end_y + end_y) // 2
        
        #When error handling for when an empty cell or occupied cell is selected
        if grid[start_y][start_x] == EC:
            print("Empty cell selected try again")
            return move(value_package, grid)
        if grid[start_y][start_x] == WD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
        if grid[start_y][start_x] == WK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)

    
        end_x = int(input("Enter an x coord for where to move to: "))
        end_y = int(input("Enter a y coord for where to move to: "))
        #Error handling
        #For when an occupied cell is selected
        if grid[end_y][end_x] == BD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
        if grid[end_y][end_x] == WD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
        if grid[end_y][end_x] == BK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
        if grid[end_y][end_x] == WK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid)
            
        #Else indicates the start of the movement logic
        else:

            if end_x > start_x + 2:
                print("Can not move that far away")
                return move(value_package, grid)

            if end_x < start_x - 2:
                print("Can not move that far away")
                return move(value_package, grid)

            if end_y > start_y + 2:
                print("Can not move that far away")
                return move(value_package, grid)

            if end_y < start_y - 2:
                print("Can not move that far away")
                return move(value_package, grid)

            if grid[start_x] == grid[end_x]:
                print("You can only move diagonally")
                return move(value_package, grid)

            if grid[start_x] == grid[end_x]:
                print("You can only move diagonally")
                return move(value_package, grid)

            else:
                grid[start_y][start_x] = EC
                grid[end_y][end_x] = BD
                value_package["cur_turn"] = Players.White
                return move(value_package, grid)
    


main(grid)
