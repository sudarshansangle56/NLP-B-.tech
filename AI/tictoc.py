import math

def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
    print("-" * 9)

def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def evaluate(board):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            return 10 if board[row][0] == "X" else -10
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return 10 if board[0][col] == "X" else -10
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return 10 if board[0][0] == "X" else -10
    
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return 10 if board[0][2] == "X" else -10
    
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# -------- PLAY GAME --------
board = [[" " for _ in range(3)] for _ in range(3)]

print("Welcome to Tic-Tac-Toe!")
print("You are O, AI is X\n")

while True:
    print_board(board)

    # Player move
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] != " ":
        print("Invalid move! Try again.")
        continue

    board[row][col] = "O"

    # Check if player wins
    if evaluate(board) == -10:
        print_board(board)
        print("🎉 You WIN!")
        break

    # Check draw
    if not is_moves_left(board):
        print_board(board)
        print("It's a DRAW!")
        break

    # AI Move
    print("\nAI is thinking...")
    ai_row, ai_col = find_best_move(board)
    board[ai_row][ai_col] = "X"

    # Check if AI wins
    if evaluate(board) == 10:
        print_board(board)
        print("🤖 AI WINS!")
        break

    # Check draw
    if not is_moves_left(board):
        print_board(board)
        print("It's a DRAW!")
        break
