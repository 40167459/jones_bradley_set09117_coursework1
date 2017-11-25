#Draughts.py
#40167459
#Bradley Jones
#27/10/2017
from enum import Enum
grid_height = 8
grid_width = 8
#White Draught
WD = 'w'
#White King
WK = 'W'
#Empty Cell
EC = '_'
#Black Draught
BD = 'b'
#Black King
BK = 'B'
#Yes value
Y = 'Y'
y = 'y'
#No Value
n = 'n'
N = 'N'
#players
Players = Enum("Players", "White Black")
#END OF CONSTANTS SECTION
wpc = 12 #Shows the amount of white pieces on the board
bpc = 12 #Shows the amount of black pieces on the board

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



def main(grid, wpc, bpc):
    value_package=dict([("grid", grid),("cur_turn",Players.White)])
    while True:
        print_board(grid)
        move(value_package, grid, wpc, bpc)
        break


#Prints the board
def print_board(grid):
    acc = 0
    print("    0    1    2    3    4    5    6    7   ")
    for row in grid:
        print(acc, row)
        acc = acc + 1

def move(value_package, grid, wpc, bpc):
    if value_package["cur_turn"] == Players.White:
        print("White Turn\n")
        start_x = int(input("Enter an x coord for where to move from: "))
        start_y = int(input("Enter a y coord for where to move from: "))
        #When error handling for when an empty cell is selected
        if grid[start_y][start_x] == EC:
            print("Empty cell selected try again")
            return move(value_package, grid, wpc, bpc)
        if grid[start_y][start_x] == BD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        if grid[start_y][start_x] == BK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        
        end_x = int(input("Enter an x coord for where to move to: "))
        end_y = int(input("Enter a y coord for where to move to: "))
        
        #Define Mid points here
        mid_x = abs(start_x + end_x) // 2
        mid_y = abs(start_y + end_y) // 2

        #Asks the user if they would like to undo the move
 #       undo_answer =  print(input("Would you like to undo this move? Y/N: "))
 
        #Starts the undo function, if yes is selected
 #       if undo_answer == y or undo_answer == Y:
 #           grid[start_y][start_x] = WD
 #           grid[end_y][grid_x] = EC
 #           print_board(grid)
 #           return move(value_package, grid, wpc, bpc)
        
        #Starts the undo function, if no is selected
 #       if undo_answer == n or undo_answer == N:
 #           return move(value_package, grid, wpc, bpc)

            
        #Error handling
        #For when an occupied cell is selected as the end point
        if grid[end_y][end_x] == BD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        if grid[end_y][end_x] == WD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        if grid[end_y][end_x] == BK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        if grid[end_y][end_x] == WK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        #Else indicates the start of the movement logic   
        else:

             #Taking a piece
            if grid[mid_y][mid_x] == BD or grid[mid_y][mid_x] == BK:
                grid[start_y][start_x] = EC
                grid[end_y][end_x] = WD
                grid[mid_y][mid_x] = EC
                bpc = bpc - 1
                value_package["cur_turn"] = Players.Black
                print("Black pieces remaining: ", bpc)
                print_board(grid)
                if (bpc == 0):
                    print("White team wins")
                    quit()

                else:
                    grid[start_y][start_x] = EC
                    grid[end_y][end_x] = WD
                    return move(value_package, grid, wpc, bpc)
                                   

            #For if the player attempts to capture his own pieces
            if grid[mid_y][mid_x] == WD:
                print("Illegal move, please try again")
                return move(value_package, grid, wpc, bpc)
            if grid[mid_y][mid_x] == WK:
                print("Illegal move, please try again")
                return move(value_package, grid, wpc, bpc)

            #If Y coordinate is equal to 7, the draught becomes a King
            if end_y == 0:
                grid[0][end_x] = WK
                grid[start_y][start_x] = EC
                
             #These if statements ensure that the move is legal
            if end_x > start_x + 2:
                print("Cannot move that far away")
                return move(value_package, grid, wpc, bpc)

            if end_y > start_y + 2:
                print("Cannot move that far away")
                return move(value_package, grid, wpc, bpc)

            if end_y < start_y - 2:
                print("Cannot move that far away")
                return move(value_package, grid, wpc, bpc)

            if grid[start_x] == grid[end_x]:
                print("You can only move diagonally")
                return move(value_package, grid, wpc, bpc)

            if grid[start_y] == grid[end_y]:
                print("You can only move diagonally")
                return move(value_package, grid, wpc, bpc)
            
            else:
                print_board(grid)
                grid[start_y][start_x] = EC
                grid[end_y][end_x] = WD
                value_package["cur_turn"] = Players.Black
                return move(value_package, grid, wpc, bpc)
    
            
    #starts the movement function if it is a black turn
    if value_package["cur_turn"] == Players.Black:
        print("Black Turn\n")
        start_x = int(input("Enter an x coord for where to move from: "))
        start_y = int(input("Enter a y coord for where to move from: "))
        
        #When error handling for when an empty cell or occupied cell is selected
        if grid[start_y][start_x] == EC:
            print("Empty cell selected try again")
            return move(value_package, grid, wpc, bpc)
        if grid[start_y][start_x] == WD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        if grid[start_y][start_x] == WK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)

        end_x = int(input("Enter an x coord for where to move to: "))
        end_y = int(input("Enter a y coord for where to move to: "))

        #Define Mid points here
        mid_x = abs(start_x + end_x) // 2
        mid_y = abs(start_y + end_y) // 2
            
        #Error handling
        #For when an occupied cell is selected as the end point
        if grid[end_y][end_x] == BD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        if grid[end_y][end_x] == WD:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        if grid[end_y][end_x] == BK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        if grid[end_y][end_x] == WK:
            print("An occupied cell has been selected, please try again")
            return move(value_package, grid, wpc, bpc)
        
        #Else indicates the start of the movement logic
        else:

             #Taking a piece
            if grid[mid_y][mid_x] == WD or grid[mid_y][mid_x] == WK:
                grid[start_y][start_x] = EC
                grid[end_y][end_x] = BD
                grid[mid_y][mid_x] = EC
                wpc = wpc - 1
                value_package["cur_turn"] = Players.White
                print("White pieces remaining: ", wpc)
                print_board(grid)
                if (bpc == 0):
                    print("Black team wins")
                    quit()

                else:
                    return move(value_package, grid, wpc, bpc)
            

            #For if the player attempts to capture his own pieces
            if grid[mid_y][mid_x] == BD:
                print("Illegal move, please try again")
                return move(value_package, grid, wpc, bpc)
            if grid[mid_y][mid_x] == BK:
                print("Illegal move, please try again")
                return move(value_package, grid, wpc, bpc)

            #If Y coordinate is equal to 7, the draught becomes a King
            if end_y == 7:
                grid[7][end_x] = BK
                grid[start_y][start_x] = EC
                
             #These if statements ensure that the move is legal
            if end_x > start_x + 2:
                print("Cannot move that far away")
                return move(value_package, grid, wpc, bpc)

            if end_y > start_y + 2:
                print("Cannot move that far away")
                return move(value_package, grid, wpc, bpc)

            if end_y < start_y - 2:
                print("Cannot move that far away")
                return move(value_package, grid, wpc, bpc)

            if [start_x] == [end_x]:
                print("You can only move diagonally")
                return move(value_package, grid, wpc, bpc)

            if [start_y] == [end_y]:
                print("You can only move diagonally")
                return move(value_package, grid, wpc, bpc)


            else:
                grid[start_y][start_x] = EC
                grid[end_y][end_x] = BD
                print_board(grid)
                value_package["cur_turn"] = Players.White
                return move(value_package, grid, wpc, bpc)

main(grid, wpc, bpc)
