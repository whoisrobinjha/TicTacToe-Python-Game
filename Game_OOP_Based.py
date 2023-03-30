class TicTacToe:
    def __init__(self):
        self.players = ["X", "O"]
        self.current_player = self.players[0]
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def print_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("- - - - -")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("- - - - -")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def check_winner(self):
        winning_position = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
        for position in winning_position:
            if all(self.board[i] == self.current_player for i in position):
                return True
        return False

    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()
        while True:
            move = int(input(self.current_player + "'s turn... Enter a position (1-9): ")) - 1
            if self.board[move] != " ":
                print("Space occupied, try again...")
            else:
                self.board[move] = self.current_player
                self.print_board()
                if self.check_winner():
                    print(self.current_player + " Wins!!")
                    break
                if all(i != " " for i in self.board):
                    print("It is a Draw!!")
                    break
                self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]

TicTacToe().play_game()