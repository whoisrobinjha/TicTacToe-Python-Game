class TicTacToe:
    player_X = "X"
    player_O = "O"
    empty_space = " "

    def __init__(self):
        self.players = [self.player_X, self.player_O]
        self.current_player = self.players[0]
        self.board = [self.empty_space] * 9

    def print_board(self):
        """print the current state of the board"""
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("- - - - -")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("- - - - -")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def check_winner(self):
        """Check if the current player has won"""
        winning_position = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
        for position in winning_position:
            if all(self.board[i] == self.current_player for i in position):
                return True
        return False
    
    def get_move(self):
        """Get user's move"""
        while True:
            move = input(self.current_player + "'s turn... Enter a position (1-9): ")
            if move.isdigit():
                move = int(move) - 1
                if 0 <= move and self.board[move] == self.empty_space:
                    return move
            print("Invalid move, please try again.")

    def play_game(self):
        """Play the game"""
        print("Welcome to Tic Tac Toe!")
        self.print_board()
        while True:
            move = self.get_move()
            self.board[move] = self.current_player
            self.print_board()
            if self.check_winner():
                print(self.current_player + " Wins!!")
                break
            if all(i != self.empty_space for i in self.board):
                    print("It is a Draw!!")
                    break              
            self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]

TicTacToe().play_game()