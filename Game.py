def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("- - - - -")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("- - - - -")
    print(board[6] + " | " + board[7] + " | " + board[8])

def check_winner(board, player):
    winning_position = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
    for position in winning_position:
        if(all(board[i] == player for i in position)):
            return True
    return False

def play_game():
    players = ["X", "O"]
    current_player = players[0]
    board = [" "," "," "," "," "," "," "," "," "]
    print_board(board)
    
    while True:
        print(current_player + "'s turn...")
        move = int(input(" Enter a position (1-9)")) - 1
        if board[move] != " ":
            print(" Space occupied, try again...")
        else:
            board[move] = current_player
            print_board(board)
            if check_winner(board, current_player):
                print(current_player + " Wins!!")
                break
            if all(i != " " for i in board):
                print(" It is a Draw!!")
                break
            current_player = players[(players.index(current_player) + 1) % 2]

play_game()