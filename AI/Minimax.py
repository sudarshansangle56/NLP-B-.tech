import math

# Display the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for winner
def check_winner(board):
    # Rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

# Check if any moves left
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Find the best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main Game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("=== TIC TAC TOE (You: X | AI: O) ===")

    while True:
        print_board(board)
        if check_winner(board) or is_full(board):
            break

        # Player move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        board[row][col] = "X"

        if check_winner(board) or is_full(board):
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"Winner is {winner}!")
    else:
        print("It's a Draw!")

# Run
play_game()
