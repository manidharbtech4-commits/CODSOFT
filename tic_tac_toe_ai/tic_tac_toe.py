board = [" "] * 9

def show_board():
    print("\n  " + board[0] + " | " + board[1] + " | " + board[2])
    print(" ---+---+---")
    print("  " + board[3] + " | " + board[4] + " | " + board[5])
    print(" ---+---+---")
    print("  " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def space_is_free(position):
    return board[position] == " "

def board_is_full():
    if " " in board:
        return False
    else:
        return True

def check_win(player):
    wins = [[0,1,2], [3,4,5], [6,7,8], 
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]]
    for combo in wins:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def get_available_positions():
    moves = []
    for i in range(9):
        if board[i] == " ":
            moves.append(i)
    return moves

def place_move(position, symbol):
    board[position] = symbol

def remove_move(position):
    board[position] = " "

def minimax_function(is_max_player, alpha=-1000, beta=1000):
    if check_win("O"):
        return 10
    elif check_win("X"):
        return -10
    elif board_is_full():
        return 0

    if is_max_player:
        best_value = -1000
        for pos in get_available_positions():
            place_move(pos, "O")
            value = minimax_function(False, alpha, beta)
            remove_move(pos)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    
    else:
        best_value = 1000
        for pos in get_available_positions():
            place_move(pos, "X")
            value = minimax_function(True, alpha, beta)
            remove_move(pos)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value

def find_best_computer_move():
    best_score = -1000
    best_position = -1
    
    print("AI is thinking...")
    
    for possible_move in get_available_positions():
        place_move(possible_move, "O")
        move_score = minimax_function(False)
        remove_move(possible_move)
        
        if move_score > best_score:
            best_score = move_score
            best_position = possible_move
            
    return best_position

print("Hey! Let's play Tic Tac Toe :)")
print("I'm X and computer is O")
print("Positions are like this:")
print("7 | 8 | 9")
print("4 | 5 | 6")
print("1 | 2 | 3")
print("Enter number 1-9 to play\n")

show_board()

turn = "X"

while True:
    if turn == "X":
        while True:
            try:
                player_input = int(input("Your turn (1-9): "))
                move_pos = player_input - 1
                
                if move_pos >= 0 and move_pos <= 8 and space_is_free(move_pos):
                    place_move(move_pos, "X")
                    print("You placed X at", move_pos+1)
                    break
                else:
                    print("That spot is taken or wrong number, try again!")
            except:
                print("Please enter a valid number 1-9")
    else:
        computer_pos = find_best_computer_move()
        place_move(computer_pos, "O")
        print(f"Computer played at position {computer_pos+1}")

    show_board()

    if check_win(turn):
        if turn == "X":
            print("Wow you won!! Good job!")
        else:
            print("Haha computer won this time! 😄")
        break
    
    if board_is_full():
        print("Oh it's a draw... nice game!")
        break

    if turn == "X":
        turn = "O"
    else:
        turn = "X"

print("Thanks for playing my internship project!")