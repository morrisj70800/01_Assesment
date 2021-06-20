from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


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

    def to_game(self, partner):
        Game(self)

    def to_help(self):
        Help(self)


class Help:
    def __init__(self, partner):
        background = "Yellow"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press 'x' cross at the top, closes help and 'releases' help button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help",
                                 font=("Aerial", "24", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="This quiz is a 15 question quiz"
                                                     "this is a straight forward quiz"
                                                     "there are 4 answers and only one"
                                                     "of them is correct. ", font="yellow",
                                bg=background, justify=LEFT,wrap=350)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="blue", fg="white",
                                  font="Helvetica" "10" "bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


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

        # Top level answers buttons row 1.0
        self.top_left_answer_button = Button(self.top_answers_frame, text="Answer 1",
                                             font="Aerial 10 bold", padx=5, pady=5,
                                             command=lambda: self.reveal_answer(0))
        self.top_left_answer_button.grid(column=0, row=0)

        self.top_right_answer_button = Button(self.top_answers_frame, text="Answer 2",
                                              font="Aerial 10 bold", padx=5, pady=5,
                                              command=lambda: self.reveal_answer(1))
        self.top_right_answer_button.grid(column=1, row=0)

        # Bottom level answers buttons row 2.0
        self.bottom_left_answer_button = Button(self.top_answers_frame, text="Answer 3",
                                                font="Aerial 10 bold", padx=5, pady=5,
                                                command=lambda: self.reveal_answer(2))
        self.bottom_left_answer_button.grid(column=0, row=1)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text="Answer 4",
                                                 font="Aerial 10 bold", padx=5, pady=5,
                                                 command=lambda: self.reveal_answer(3))
        self.bottom_right_answer_button.grid(column=1, row=1)


    def reveal_answer(self, location):
      # Print corresponding number based on location
      print(location)


if __name__ == "__main__":
    root = Tk()
    root.title("Norse God Quiz")
    play = Start(root)
    root.mainloop()
