import random
from tabulate import tabulate
import sys
import os

def clear_console():
    #clear the console based on the operating system, windows nt - 'cls', other os - 'clear'
    os.system('cls' if os.name == 'nt' else 'clear') 

def main():
    clear_console()
    
    #print the welcome message and instructions for the user
    print("""Welcome to the Chess Question! Let's solve what pieces can be attacked in a given situation:
    *You can choose between two random white pieces and then place up to 16 black pieces on the board.
    *The program will then calculate how many black pieces can be attacked in the next move.
    *List that two pieces will be randomly selected: Queen, King, Bishop, Knight, Rook, Pawn.
    *Follow the guidelines to place the pieces on the board or exit the program if you want to quit.""")

    #randomly select two pieces for the user to choose
    available_pieces = ["Queen", "King", "Bishop", "Knight", "Rook", "Pawn"]
    piece_options = random.sample(available_pieces, 2)

    #create empty chess board layout
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    chess_board = [[None for _ in range(8)] for _ in range(8)]

    #show the board with empty cells for reference
    print(tabulate(chess_board, headers=columns, tablefmt="grid", showindex=rows))

    while True:
        try:
            #ask the user to choose one of the two pieces
            type = input(f"What piece do you want to place? Choose between {piece_options[0]} and {piece_options[1]} (Type 'exit' to exit program): ").capitalize().strip()
            if type == "Exit":
                sys.exit(0)
            if type not in piece_options:
                raise ValueError("Invalid piece type. Please choose from the provided options.")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
    
    while True:
        try:
        #ask user to enter the coordinate of the white piece:
            wcoord = input("Enter the coordinate of the white piece (e.g., b5): (type 'exit' to exit) ").strip().lower()
            if wcoord == "exit":
                sys.exit(0)
            validate_coordinate(wcoord, columns, rows)

            #get the index of the coordinate:
            wx = columns.index(wcoord[0]) 
            wy = rows.index(int(wcoord[1]))
            
            #assign the unicode character for the piece type:
            piece = {
                "Queen": "\u2655",
                "King": "\u2654",
                "Bishop": "\u2657",
                "Knight": "\u2658",
                "Rook": "\u2656",
                "Pawn": "\u2659"
            }[type]
            
            #assign white piece type to the board, vertical placement index comes first:
            chess_board[wy][wx] = piece 
            
            #place black pieces on the board:
            black_piece_coords(chess_board, columns, rows)
            
            #show the board with white and black pieces:
            print(tabulate(chess_board, headers=columns, tablefmt="grid", showindex=rows))
            
            piece_moves = { 
                #possible moves for each piece type
                "Pawn": [(1, 1), (-1, 1)],
                "King": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)],
                "Queen": [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)],
                "Rook": [(1, 0), (-1, 0), (0, 1), (0, -1)],
                "Bishop": [(1, 1), (-1, -1), (1, -1), (-1, 1)],
                "Knight": [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)],

            }
            
            #check how many black pieces can be attacked by the white piece in next move:
            count = check_attackable_pieces(chess_board, columns, rows, piece_moves, type, wx, wy)
            print(f"White piece can attack a total of {count} pieces.")
            sys.exit(0)

        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue

def black_piece_coords(chess_board, columns, rows):

    #initiate the count of black pieces placed on the board:
    i = 0

    while i < 16: #place 16 or less black pieces on the board
        try:
            coord = input(f"Enter the coordinate of the {i+1} black piece (e.g., b5) (type 'done' to exit): ").strip().lower()
            if coord == "done":
                break
            validate_coordinate(coord, columns, rows)
           
            y = columns.index(coord[0])
            x = rows.index(int(coord[1]))

            if chess_board[x][y] is not None:
                raise ValueError("There is already a piece in this position.")
            chess_board[x][y] = "BP"  #place black piece
            i += 1
        except ValueError as e:
            print(f"Error: {e}")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue

#check if the coordinate is in the correct format:
def validate_coordinate(coord, columns, rows):

    if len(coord) != 2 or coord[0] not in columns or not coord[1].isdigit() or int(coord[1]) not in rows:
        raise ValueError("Invalid coordinate")
    return rows.index(int(coord[1])), columns.index(coord[0])

#check what can white piece attack in next move:
def check_attackable_pieces(board, c, r, moves, piece_type, x, y):

    #assign all possible moves for chosen piece type:
    piece_moves = moves[piece_type]
    count = 0

    #check if the white piece can attack
    for ix, iy in piece_moves: #ix = x-axis, iy = y-axis in attack direction 
        new_x, new_y = x + ix, y + iy #new_x = new x-axis, new_y = new y-axis after attack
        while 0 <= new_x < 8 and 0 <= new_y < 8: 
            if board[new_y][new_x] == "BP": 
                count += 1
                if count == 1:
                    print(f"White piece can attack:\n{c[new_x]}{r[new_y]}")
                elif count > 1:
                    print(f"{c[new_x]}{r[new_y]}")
                break
            
            #stop making new axis coordinates if not these piece types:
            elif piece_type not in ["Queen", "Rook", "Bishop"]: 
                break 
 
            #check next cell in the same direction if black piece is not found:
            new_x += ix 
            new_y += iy

    #return the total number of black pieces that can be attacked by the white piece:
    return count

if __name__ == "__main__":
    main()