# Module 1 Sprint 1 Project The Chess Question

This program is designed to simulate a chess scenario where you:

Choose one of two randomly selected white chess pieces.

Place it on a chessboard.

Place up to 16 black chess pieces.

Calculate and display how many black pieces the selected white piece can attack in its next move.

Features

Randomized Choices: The program randomly selects two chess pieces (e.g., Queen, King, Bishop, Knight, Rook, Pawn) for you to choose from.

Interactive Board Setup: Allows you to input the coordinates of the white and black pieces.

Attack Calculation: Computes how many black pieces the selected white piece can attack based on chess rules.

Console Clear: Automatically clears the console screen for a clean user interface.

Code Logic and Flow

1. Program Initialization

The main() function is the entry point of the program.

The console is cleared using the clear_console() function to ensure a clean interface. This works across Windows (os.name == 'nt') and other systems (e.g., Linux, macOS).

2. Welcome Message and Instructions

The program starts by displaying:

Welcome message.

Brief instructions explaining the process of selecting and placing pieces.

Rules for input format (e.g., b5 for coordinates).

3. Random Piece Selection

The program uses the random.sample() function to randomly select two pieces from the list:

available_pieces = ["Queen", "King", "Bishop", "Knight", "Rook", "Pawn"]
piece_options = random.sample(available_pieces, 2)

The user must choose one of these two pieces to proceed.

4. Chessboard Setup

A chessboard is represented as an 8x8 grid initialized with None values.

Column headers (a to h) and row indices (1 to 8) are used for reference.

The tabulate module is utilized to display the chessboard in a grid format.

5. White Piece Placement

The user inputs the coordinates for the white piece (e.g., b5).

The program validates the input format using the validate_coordinate() function.

The piece is placed on the board using Unicode chess symbols:

piece = {
    "Queen": "\u2655",
    "King": "\u2654",
    "Bishop": "\u2657",
    "Knight": "\u2658",
    "Rook": "\u2656",
    "Pawn": "\u2659"
}[type]

6. Black Piece Placement

The user can place up to 16 black pieces by entering their coordinates.

Each coordinate is validated to ensure no overlap with existing pieces.

Black pieces are represented as BP on the board.

7. Attack Calculation

The program calculates which black pieces the selected white piece can attack in its next move using the check_attackable_pieces() function.

The function checks valid moves for the chosen white piece and tracks attackable black pieces based on:

Move sets defined in the piece_moves dictionary.

Chess rules (e.g., movement patterns for Rook, Bishop, Knight, etc.).

Results are displayed as a list of coordinates and the total count.

Functions

clear_console()

Clears the console screen for a clean user interface.

main()

Handles the program flow:

Displays welcome message and instructions.

Randomly selects two white pieces.

Manages user inputs for placing white and black pieces.

Displays the board and calculates attackable pieces.

black_piece_coords()

Allows the user to place up to 16 black pieces on the board.

Ensures valid and non-overlapping positions.

validate_coordinate(coord, columns, rows)

Validates if a given coordinate (e.g., b5) is within the valid range of the chessboard.

check_attackable_pieces(board, c, r, moves, piece_type, x, y)

Calculates how many black pieces the chosen white piece can attack based on:

Possible move sets for the piece type.

The positions of black pieces on the board.

Input Examples

White Piece Selection:

Program randomly selects: Queen and Knight.

User chooses: Knight.

White Piece Placement:

Input: e4.

Black Piece Placement:

Input: d6, f5, done.

Output Examples

The program outputs the chessboard with all pieces placed.

Lists coordinates of attackable black pieces and the total count.

White piece can attack:
d6
f5
White piece can attack a total of 2 pieces.

Notes

Follow input formats strictly (e.g., b5 for coordinates).

Type exit to quit the program at any prompt.

For black piece placement, type done to finish.

