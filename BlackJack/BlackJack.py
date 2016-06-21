#Name: Blackjack - Final Project
#Author: Taylor Sherer

from tkinter import *
import tkinter.messagebox
from random import *
from copy import *
from Deck import Deck
from Card import Card
import sys

class Blackjack(Frame):

    deck =  Deck()
    board = []
    game_start = FALSE    

    money = 0.0

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Blackjack!")
        self.master.geometry("400x280")
        self.pack(fill = BOTH, expand = 1)
        menubar = Menu(self.master)
        self.master.config(menu = menubar)

        self.label1 = Label(self.master, text = "Play Area", padx = 5, pady = 5)
        self.label1.pack()

        self.play_area = Text(self.master, state = DISABLED, width = 35, height = 10)
        self.play_area.pack()

        self.hit = Button(self.master, text = "Hit Me!", command = self.hit_me, padx = 5, pady = 5, bd = 5)
        self.hit.pack(fill = X)

        menubar.add_command(label = "Play the Game!", command = self.game_deal)
        menubar.add_command(label = "Display Available Funds!", command = self.show_money)
        menubar.add_command(label = "Reset Funds to Zero!", command = self.reset_money)
        menubar.add_command(label = "Quit", command = self.client_exit)

    def client_exit(self):
        if (tkinter.messagebox.askyesno("Quit?", "Are you sure you want to quit?")):
            self.master.destroy()
            sys.exit()

    def game_deal(self):
        if (self.check_bank()):
            self.game_start = TRUE
            self.board = []
            self.board.extend(self.deck.get_deal())
            self.display_board()



    def show_money(self):
        tkinter.messagebox.showinfo("Your Bank", "Your funds are $" + str(self.money))

    def hit_me(self):
        if(self.game_start is FALSE):
            tkinter.messagebox.showinfo("Play Error", "Start a new game!")
        else:
            card = self.deck.get_card()
            self.board.append(card)
            self.display_board()


    def write_line(self, str):
        self.play_area.insert(END, '\n' + str)

    def display_board(self):

        text = self.play_area
        text.config(state = NORMAL)

        text.delete(1.0, END)

        line_ind = 1
        for card in self.board:
            self.write_line(str(line_ind) + ". " + card.get_display())
            line_ind += 1

        text.config(state = DISABLED)

        self.check_win()
       
    def reset_money(self):
        tkinter.messagebox.showinfo("Reset!", "Your Bank has been reset to $0.00.")
        self.money = 0.0

    def check_win(self):
        sum_ace_eleven = 0
        sum_ace_one = 0
        for card in self.board:
            if (card.get_val() >= 11 and card.get_val() <= 13):
                sum_ace_eleven += 10
                sum_ace_one += 10
            elif (card.get_val() == 14):
                sum_ace_eleven += 11
                sum_ace_one += 1
            elif(card.get_val() < 11):
                sum_ace_eleven += card.get_val()
                sum_ace_one += card.get_val()

        if (sum_ace_one > 21):
            tkinter.messagebox.showinfo("Game Finish!", "You lose! $50.00 removed from Bank.")
            self.game_start = FALSE
            self.money -= 50.0
        elif(sum_ace_eleven == 21 or sum_ace_one == 21):
            tkinter.messagebox.showinfo("Game Finish!", "You win! $100.00 added to Bank.")
            self.game_start = FALSE
            self.money += 100.0

        self.check_bank()
            
    def check_bank(self):
         if (self.money <= -1000.0):
             tkinter.messagebox.showinfo("Game Finish!", "You are a thousand dollars in debt! Reset Bank to continue.")
             return FALSE
         else:
             return TRUE
   # def show_money(self):

def main():
    root = Tk()
    Blackjack(root).mainloop()

if __name__ == '__main__':
    main()
