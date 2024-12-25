from tabulate import tabulate

def main():
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    chess_board = [[None for _ in range(8)] for _ in range(8)]
    print(tabulate(chess_board, headers=columns, tablefmt="grid", showindex=rows))
    
    try:
        type = input("What piece you want to place? (Q, K, B, N, R, P): ").upper().strip()
        if type not in ["Q", "K", "B", "N", "R", "P"]:
            raise ValueError("Invalid piece type.")
        
        coord = input("Enter the coordinate of the white piece (e.g., b5): ").strip().lower()
        if len(coord) != 2 or coord[0] not in columns or not coord[1].isdigit() or int(coord[1]) not in rows:
            raise ValueError("Invalid coordinate.")
        
        wx = columns.index(coord[0])
        wy = rows.index(int(coord[1]))
        
        piece = {
            "Q": "\u2655",
            "K": "\u2654",
            "B": "\u2657",
            "N": "\u2658",
            "R": "\u2656",
            "P": "\u2659"
        }[type]
        
        chess_board[wy][wx] = piece
        
        amount = int(input("Enter the amount of black pieces you want to place: "))
        black_piece_coords(chess_board, amount, columns, rows, wx, wy)
        
        print(tabulate(chess_board, headers=columns, tablefmt="grid", showindex=rows))
        
        piece_moves = {
            "P": [(1, 1), (1, -1)],
            "K": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)],
            "Q": [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)],
            "R": [(1, 0), (-1, 0), (0, 1), (0, -1)],
            "B": [(1, 1), (-1, -1), (1, -1), (-1, 1)],
            "N": [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)],
        }
        
        count = check_attackable_pieces(chess_board, columns, rows, piece_moves, type, wx, wy)
        print(f"White piece can attack a total of {count} pieces.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def black_piece_coords(chess_board, amount, columns, rows, wx, wy):
    for i in range(amount):
        try:
            coord = input(f"Enter the coordinate of the {i+1} black piece (e.g., b5): ").strip().lower()
            if len(coord) != 2 or coord[0] not in columns or not coord[1].isdigit() or int(coord[1]) not in rows:
                raise ValueError("Invalid coordinate.")
            
            y = columns.index(coord[0])
            x = rows.index(int(coord[1]))
            if (x, y) != (wx, wy):
                chess_board[x][y] = "BP"  #black piece
            else:
                print("There is already a white piece there.")
                continue
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def check_attackable_pieces(board, c, r, moves, piece, x, y):
    piece_moves = moves[piece]
    count = 0

    for ix, iy in piece_moves:
        new_x, new_y = x + ix, y + iy
        while 0 <= new_x < 8 and 0 <= new_y < 8:
            if board[new_y][new_x] == "BP":
                count += 1
                if count == 1:
                    print(f"White piece can attack:\n{c[new_x]}{r[new_y]}")
                elif count > 1:
                    print(f"{c[new_x]}{r[new_y]}")
                break
            elif board[new_y][new_x] is not None:
                break
            new_x += ix
            new_y += iy
    return count

if __name__ == "__main__":
    main()