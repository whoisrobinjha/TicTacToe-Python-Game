import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    player_X = "X"
    player_O = "O"
    empty_space = " "

    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.players = [self.player_X, self.player_O]
        self.current_player = self.players[0]
        self.board = [self.empty_space] * 9

        self.create_board()

    def create_board(self):
        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            button = tk.Button(self.master, text=self.board[i], font=("Helvetica", 32), width=3, height=1, command=lambda idx=i: self.button_click(idx))
            button.grid(row=row, column=col)
            self.buttons.append(button)

    def button_click(self, idx):
        if self.board[idx] == self.empty_space:
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player, state="disabled")
            if self.check_winner():
                self.display_winner()
            elif all(i != self.empty_space for i in self.board):
                self.display_draw()
            else:
                self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]

    def check_winner(self):
        winning_position = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
        for position in winning_position:
            if all(self.board[i] == self.current_player for i in position):
                return True
        return False

    def display_winner(self):
        tk.messagebox.showinfo("Winner", self.current_player + " Wins!!")
        self.reset_game()

    def display_draw(self):
        tk.messagebox.showinfo("Draw", "It is a Draw!!")
        self.reset_game()

    def reset_game(self):
        self.board = [self.empty_space] * 9
        self.current_player = self.players[0]
        for button in self.buttons:
            button.config(text=self.empty_space, state="normal")

root = tk.Tk()
game = TicTacToeGUI(root)
root.mainloop()