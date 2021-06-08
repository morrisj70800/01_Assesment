from tkinter import *
from functools import partial   # To prevent unwanted windows
import random

class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Set Initial balance to zero
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        # Mystery Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Legendary God Quiz",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)
        # Initial Instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, font="arial 10 italic",
                                          text="Please Choose Your Gods ",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # button frame (row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # Buttons go here
        button_font = "Arial 12 bold"
        # Roman God  button (row 3)
        self.Roman_god_button = Button(self.stakes_frame, text="Roman",
                                       command=lambda: self.to_game(1),
                                       font=button_font, bg="Red")
        self.Roman_god_button.grid(row=0, column=0, pady=10)

        # Greek God Button
        self.Greek_god_button = Button(self.stakes_frame, text="Greek",
                                       command=lambda: self.to_game(2),
                                       font=button_font, bg="Pink")
        self.Greek_god_button.grid(row=0, column=1, pady=10)

        # Norse God Button
        self.Norse_god_button = Button(self.stakes_frame, text="Norse",
                                       command=lambda: self.to_game(3),
                                       font=button_font, bg="Yellow")
        self.Norse_god_button.grid(row=0, column=2, pady=10)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Legendary God Quiz")
    play = Start(root)
    root.mainloop()