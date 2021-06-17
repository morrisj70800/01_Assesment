from tkinter import *
from functools import partial   # To prevent unwanted windows
import random

class Game:
    def __init__(self, partner):
        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # God Label row 0
        self.capital_label = Label(self.game_frame, text="Norse Gods",
                                   font="Aerial 15 bold")
        self.capital_label.grid(row=0)

        # Setup grid for answer buttons row 2

        self.top_answers_frame = Frame(self.game_box)
        self.top_answers_frame.grid(row=2)

       # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text="Top left",
                                             font="Aerial 10 bold", padx=5, pady=5,
                                             command=lambda: self.reveal_answer(0))
        self.top_left_answer_button.grid(column=0, row=0)

        self.top_right_answer_button = Button(self.top_answers_frame, text="Top right",
                                              font="Aerial 10 bold", padx=5, pady=5,
                                              command=lambda: self.reveal_answer(1))
        self.top_right_answer_button.grid(column=1, row=0)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text="Bottom left",
                                                font="Aerial 10 bold", padx=5, pady=5,
                                                command=lambda: self.reveal_answer(2))
        self.bottom_left_answer_button.grid(column=0, row=1)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text="Bottom right",
                                                 font="Aerial 10 bold", padx=5, pady=5,
                                                 command=lambda: self.reveal_answer(3))
        self.bottom_right_answer_button.grid(column=1, row=1)

    def reveal_answer(self, location):
         # Print corresponding number based on location
        # TL = 0 TR =1 BL = 2 BR = 3
        print(location)










if __name__ == "__main__":
    root = Tk()
    root.title("Norse God Quiz")
    play = Game(root)
    root.mainloop()
