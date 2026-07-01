# Tic-Tac-Toe Game

board = [" " for i in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == player:
            return True
    return False

player = "X"

for turn in range(9):
    print_board()

    move = int(input(f"Player {player}, enter position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = player

        if check_winner(player):
            print_board()
            print("Player", player, "wins!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("Position already taken! Try again.")

else:
    print_board()
    print("It's a Draw!")