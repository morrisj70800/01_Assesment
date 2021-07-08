from tkinter import *
from functools import partial   # To prevent unwanted windows
import random
import csv


class Start:
    def __init__(self, parent):

        # GUI to get type of questions
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Quiz Heading (row 0)
        self.legendary_quiz_label = Label(self.start_frame, text="Norse God Quiz",
                                          font="Arial 19 bold")
        self.legendary_quiz_label.grid(row=0)
        # Initial Instructions (row 1)
        self.legendary_quiz_instructions = Label(self.start_frame, font="arial 10 italic",
                                                text="Please Press play. you will"
                                                     "be taken to a quiz full of norse"
                                                     "gods this quiz is a 15 question"
                                                     " quiz ",
                                                     wrap=275, justify=LEFT, padx=10, pady=10)
        self.legendary_quiz_instructions.grid(row=1)

        # GUI Setup
        self.game_box = Toplevel()

        self.game_frame = Frame(self.start_frame, padx=10)
        self.game_frame.grid()

        # button frame (row 3)
        self.start_frame = Frame(self.start_frame)
        self.start_frame.grid(row=3)

        # to_game button frame row 2
        self.to_game_frame = Frame(self.start_frame)
        self.to_game_frame.grid(row=2)

        # Button goes here
        button_font = "Arial 12 bold"

        # Norse God Button
        self.play_button = Button(self.to_game_frame, text="Play",
                                  font=button_font, bg="yellow",command=lambda: self.to_game(1),
                                  height=2, width=13, borderwidth=2)
        self.play_button.grid(row=0, column=0, padx=10, pady=5)

        # Help Button row 3
        self.help_button = Button(self.start_frame, text="Help", font="Helvetica 10 bold", height=2, width=10,
                                  borderwidth=3, command=self.to_help)
        self.help_button.grid(row=3, pady=5)

        # Boxes go here (row 2)
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="Odin.gif")

        self.god1_label = Label(self.box_frame, image=photo,
                                padx=10, pady=10)
        self.god1_label.photo = photo
        self.god1_label.grid(row=0, column=0)

    def to_game(self, level):
        Game(self, level)

    def to_help(self):
        Help(self)


if __name__ == "__main__":
    root = Tk()
    root.title("Legendary God Quiz")
    play = Start(root)
    root.mainloop()