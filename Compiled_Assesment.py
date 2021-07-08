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
                                                     "of them is correct. ", font="green",
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
    def __init__(self, partner, level):
        print(level)

        # Import the csv file, name of csv file goes here
        with open('q_and_a_csv.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # result
        self.result = 0

        # Amounts of game
        self.rounds_played = 0

        # Define said answer
        self.top_left = ""
        self.top_right = ""
        self.bottom_right = ""
        self.bottom_left = ""

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Label for the quiz
        self.Norse_god_label = Label(self.game_frame, text="Norse Gods Quiz",
                                     font="Arial 15")
        self.Norse_god_label.grid(row=0)

        # Label showing answer
        self.answer_label = Label(self.game_frame, text="", font="Arial 15")
        self.answer_label.grid(row=1)

        # Setup grid for answer buttons row 3
        self.answers_frame = Frame(self.game_box)
        self.answers_frame.grid(row=3)

        # Top level button
        self.top_left_button = Button(self.answers_frame, text="Top Left",
                                      font="Arial 15", padx=5, pady=5,
                                      command=lambda: self.reveal_answer(self.top_left))
        self.top_left_button.grid(column=0, row=0)

        self.top_right_button = Button(self.answers_frame, text="Top Right",
                                      font="Arial 15", padx=5, pady=5,
                                      command=lambda: self.reveal_answer(self.top_right))
        self.top_right_button.grid(column=1, row=0)

        # Bottom level button
        self.bottom_left_button = Button(self.answers_frame, text="Bottom Left",
                                      font="Arial 15", padx=5, pady=5,
                                      command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_left_button.grid(column=0, row=1)

        self.bottom_right_button = Button(self.answers_frame, text="Bottom Right",
                                      font="Arial 15", padx=5, pady=5,
                                      command=lambda: self.reveal_answer(self.bottom_right))
        self.bottom_right_button.grid(column=1, row=1)

        # Label for results
        self.result_label = Label(self.game_box, text="{} correct / {} roundsplayed".format(self.result,
                                                                                            self.rounds_played))
        self.result_label.grid(row=3)

        # Next button
        self.next_button = Button(self.game_box, text="next", command=lambda:self.to_next(my_list))
        self.next_button.grid(row=4)

        # Disable the next button
        self.next_button.config(state=DISABLED)

        self.to_next(my_list)

    def reveal_answer(self, location):

        # refreshed result after right or wrong
        self.result_label.config(text="{} correct / {} rounds played".format(self.result, self.rounds_played))

        # To Next defined
    def to_next(self, list):
        self.top_left_button.config(state=NORMAL)
        self.top_right_button.config(state=NORMAL)
        self.bottom_left_button.config(state=NORMAL)
        self.bottom_right_button.config(state=NORMAL)
        self.next_button.config(state=DISABLED)
        self.answer_label.config(text="")


if __name__ == "__main__":
    root = Tk()
    root.title("Norse God Quiz")
    play = Start(root)
    root.mainloop()
