import sys
from tabulate import tabulate

def main():
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    chess_board = [[None for _ in range(8)] for _ in range(8)]
    print(tabulate(chess_board, headers=columns, tablefmt="grid", showindex=rows))
    piece = input("What piece you want to place? (Q, K, B, N, R, P): ").upper().strip()
    coord = input("Enter the coordinate of the white piece (e. g., b5): ")
    x = columns.index(coord[0])
    y = rows.index(int(coord[1]))
    if piece == "Q":
        chess_board[x][y] = "\u2655"
    elif piece == "K":
        chess_board[x][y] = "\u2654"
    elif piece == "B":
        chess_board[x][y] = "\u2657"
    elif piece == "N":
        chess_board[x][y] = "\u2658"
    elif piece == "R":
        chess_board[x][y] = "\u2656"
    elif piece == "P":
        chess_board[x][y] = "WP"
    amount = int(input("Enter the amount of black pieces you want to place: "))
    black_piece_coords(chess_board, amount, columns, rows, x, y)
    print(tabulate(chess_board, headers=columns, tablefmt="grid", showindex=rows))
    count = check_down_pieces(chess_board, x, y, columns, rows)
    print(f"White piece can attack total of {count} pieces.")

def black_piece_coords(chess_board, amount, columns, rows, wx, wy):
    while True:
        for i in range(amount):
            coord = input(f"Enter coordinates of the {i+1} black piece (e.g. a5): ")
            x = columns.index(coord[0])
            y = rows.index(int(coord[1]))
            if (x, y) not in (wx, wy):
                chess_board[x][y] = "B"
            else:
                print("There is already a white piece there.")
                continue
        return chess_board
    
def check_down_pieces(chess_board, x, y, columns, rows):

    count = 0
    if chess_board[x][y] == "WP":
        if chess_board[x + 1][y + 1] == "B" and 0 <= x+1 < 8 and 0 <= y+1 < 8:
            count += 1
            print(f"Piece can attack: \n{columns[y + 1]}{rows[x + 1]}")
        if chess_board[x + 1][y - 1] == "B" and 0 <= x+1 < 8 and 0 <= y-1 < 8:
            count += 1
            print(f"{rows[x - 1]}{columns[y + 1]}")
    
    elif chess_board[x][y] == "\u2654":
        count += check_king(chess_board, x, y, columns, rows)
    elif chess_board[x][y] == "\u2655":
        count += check_straight(chess_board, x, y, columns, rows)
        count += check_diagonal(chess_board, x, y, columns, rows)
    elif chess_board[x][y] == "\u2656":
        count += check_straight(chess_board, x, y, columns, rows)
    elif chess_board[x][y] == "\u2657":
        count += check_diagonal(chess_board, x, y, columns, rows)
    elif chess_board[x][y] == "\u2658":
        count += check_knight(chess_board, x, y, columns, rows)

    return count

def check_king(chess_board, x, y, columns, rows):
    count = 0
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for move in moves:
        new_x = x + move[0]
        new_y = y + move[1]
        if 0 <= new_x < 8 and 0 <= new_y < 8 and chess_board[new_x][new_y] == "B":
            count += 1
            if count == 1:
                print(f"Piece can attack: \n{columns[new_y]}{rows[new_x]}")
            elif count > 1:
                print(f"{columns[new_y]}{rows[new_x]}")
    return count

def check_straight(chess_board, x, y, columns, rows):
    count = 0
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for ix, iy in moves:
        new_x = x + ix
        new_y = y + iy
        while 0 <= new_x < 8 and 0 <= new_y < 8:
            if chess_board[new_x][new_y] == "B": 
                count += 1
                if count == 1:
                    print(f"In straight line, piece can attack: \n{columns[new_y]}{rows[new_x]}")
                elif count > 1:
                    print(f"{columns[new_y]}{rows[new_x]}")
                break
            # elif chess_board[new_x][new_y] is not None: #don't check further black pieces
            #     break
            new_x += ix
            new_y += iy 
    return count

def check_diagonal(chess_board, x, y, columns, rows):
    count = 0
    moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for ix, iy in moves:
        new_x = x + ix
        new_y = y + iy
        while 0 <= new_x < 8 and 0 <= new_y < 8:
            if chess_board[new_x][new_y] == "B":
                count += 1
                if count == 1:
                    print(f"Diagonally, piece can attack: \n{columns[new_y]}{rows[new_x]}")
                elif count > 1:
                    print(f"{columns[new_y]}{rows[new_x]}")
                break
            elif chess_board[new_x][new_y] is not None:
                break
            new_x += ix
            new_y += iy
    return count

def check_knight(chess_board, x, y, columns, rows):
    count = 0
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for ix, iy in moves:
        new_x = x + ix
        new_y = y + iy
        if 0 <= new_x < 8 and 0 <= new_y < 8 and chess_board[new_x][new_y] == "B":
            count += 1
            if count == 1:
                print(f"Piece can attack: \n{columns[new_y]}{rows[new_x]}")
            elif count > 1:
                print(f"{columns[new_y]}{rows[new_x]}")
    return count

main()