# Tic-Tac-Toe AI using Minimax

import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print()

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in available_moves():
        board[i] = "O"
        score = minimax(False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move

def play_game():
    print("Tic-Tac-Toe AI")
    print("You are X, AI is O")
    print("Positions are numbered 1 to 9")
    print_board()

    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue

        board[move] = "X"
        print_board()

        if winner("X"):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        ai_move = best_move()
        board[ai_move] = "O"
        print("AI played:")
        print_board()

        if winner("O"):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

play_game()
