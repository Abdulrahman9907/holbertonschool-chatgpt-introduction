#!/usr/bin/python3

def print_board(board):
    """
    Function Description:
    Displays the current state of the tic-tac-toe board in a formatted grid
    
    Parameters:
    board (list): A 3x3 list representing the game board
    
    Returns:
    None
    """
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Don't print separator after last row
            print("-" * 9)
    print()

def check_winner(board):
    """
    Function Description:
    Checks if there is a winner on the current board by examining
    all possible winning combinations (rows, columns, diagonals)
    
    Parameters:
    board (list): A 3x3 list representing the game board
    
    Returns:
    str: The winning player ("X" or "O"), or None if no winner
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    # Check diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """
    Function Description:
    Checks if the board is completely filled (no empty spaces left)
    
    Parameters:
    board (list): A 3x3 list representing the game board
    
    Returns:
    bool: True if board is full, False otherwise
    """
    for row in board:
        if " " in row:
            return False
    return True

def get_player_input(prompt, player):
    """
    Function Description:
    Safely gets player input with error handling for invalid values
    
    Parameters:
    prompt (str): The message to display to the player
    player (str): The current player ("X" or "O")
    
    Returns:
    int: A valid coordinate (0, 1, or 2), or None if player wants to quit
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if user_input.lower() in ['quit', 'exit']:
                return None
            value = int(user_input)
            if value in [0, 1, 2]:
                return value
            else:
                print("Please enter 0, 1, or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2) or 'quit' to exit.")

def tic_tac_toe():
    """
    Function Description:
    Main game loop that manages the tic-tac-toe game flow, handles player
    turns, input validation, winner detection, and game termination
    
    Parameters:
    None
    
    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Players will alternate placing X and O on a 3x3 board.")
    print("Enter coordinates as 0, 1, or 2. Type 'quit' to exit.\n")
    
    while True:
        print_board(board)
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print(f"🎉 Player {winner} wins! 🎉")
            break
        
        # Check for tie
        if is_board_full(board):
            print("It's a tie! The board is full.")
            break
        
        # Get player input
        print(f"Player {player}'s turn")
        row = get_player_input(f"Enter row (0, 1, or 2) for player {player}: ", player)
        if row is None:
            print("Game terminated by player.")
            break
            
        col = get_player_input(f"Enter column (0, 1, or 2) for player {player}: ", player)
        if col is None:
            print("Game terminated by player.")
            break
        
        # Check if spot is available
        if board[row][col] == " ":
            board[row][col] = player
            # Switch players
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    try:
        tic_tac_toe()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
