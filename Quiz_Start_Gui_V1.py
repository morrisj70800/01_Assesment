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

        # GUI Setup
        self.game_box = Toplevel()

        self.game_frame = Frame(self.start_frame, padx=10)
        self.game_frame.grid()

        # button frame (row 3)
        self.start_frame = Frame(self.start_frame)
        self.start_frame.grid(row=3)

        # Buttons go here
        button_font = "Arial 12 bold"
        # Roman God  button (row 3)
        self.Roman_god_button = Button(self.start_frame, text="Roman",
                                       command=lambda: self.to_game(1),
                                       font=button_font, bg="Yellow")
        self.Roman_god_button.grid(row=0, column=0, pady=10)

        # Greek God Button
        self.Greek_god_button = Button(self.start_frame, text="Greek",
                                       command=lambda: self.to_game(2),
                                       font=button_font, bg="Yellow")
        self.Greek_god_button.grid(row=0, column=1, pady=10)

        # Norse God Button
        self.Norse_god_button = Button(self.start_frame, text="Norse",
                                       command=lambda: self.to_game(3),
                                       font=button_font, bg="Yellow")
        self.Norse_god_button.grid(row=0, column=2, pady=10)

        # Boxes go here (row 2)
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="Odin.gif")

        self.god1_label = Label(self.box_frame, image=photo,
                                  padx=10, pady=10)
        self.god1_label.photo = photo
        self.god1_label.grid(row=0, column=0)

        self.god2_label = Label(self.box_frame, image=photo,
                                  padx=10, pady=10)
        self.god2_label.photo = photo
        self.god2_label.grid(row=0, column=1)

        self.god3_label = Label(self.box_frame, image=photo,
                                  padx=10, pady=10)
        self.god3_label.photo = photo
        self.god3_label.grid(row=0, column=2)





if __name__ == "__main__":
    root = Tk()
    root.title("Legendary God Quiz")
    play = Start(root)
    root.mainloop()
