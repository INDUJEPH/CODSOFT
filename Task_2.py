
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_win(player):
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True

    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True

    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

def check_draw():
    for i in range(9):
        if board[i] == " ":
            return False
    return True

def minimax(ai_turn):
    if check_win("O"):
        return 1
    if check_win("X"):
        return -1
    if check_draw():
        return 0

    if ai_turn:
        best = -10
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                if score > best:
                    best = score
        return best
    else:
        best = 10
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                if score < best:
                    best = score
        return best

def ai_play():
    best_score = -10
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

print("Tic Tac Toe Game")
print("You = X | Computer = O")

while True:
    show_board()

    pos = int(input("Choose position (1-9): ")) - 1

    if board[pos] != " ":
        print("Position already filled")
        continue

    board[pos] = "X"

    if check_win("X"):
        show_board()
        print("You Win")
        break

    if check_draw():
        show_board()
        print("Match Draw")
        break

    ai_play()

    if check_win("O"):
        show_board()
        print("Computer Wins")
        break

    if check_draw():
        show_board()
        print("Match Draw")
        break
