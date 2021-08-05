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
                                                      "gods this quiz is a 25 question"
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
                                  font=button_font, bg="yellow", command=lambda: self.to_game(1),
                                  fg="blue", height=2, width=13, borderwidth=2)
        self.play_button.grid(row=0, column=0, padx=10, pady=5)

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


class Game:
    def __init__(self, partner, level):
        print(level)

        # Import the csv file, name of csv file goes here
        with open('q_and_a_csv.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # choose an item from the main list, this item is itself a list
        question_ans = random.choice

        # result
        self.result = 0

        answers = random.sample
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
        self.norse_god_label = Label(self.game_frame, text="Norse God Quiz",
                                     font="Arial 15", fg="blue")
        self.norse_god_label.grid(row=16, column=0)

        # Label showing answer
        self.answer_label = Label(self.game_frame, text="Norse God Quiz", font="Arial 15")
        self.answer_label.grid(row=10)

        # Setup grid for answer buttons row 3
        self.answers_frame = Frame(self.game_box)
        self.answers_frame.grid(row=3)

        photo = PhotoImage(file="Gods.gif")

        # Boxes go here (row 2)
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=6, pady=10)

        self.god1_label = Label(self.box_frame, image=photo,
                                padx=10, pady=10)
        self.god1_label.photo = photo
        self.god1_label.grid(row=1, column=0)

        # Top level button

        self.top_left_button = Button(self.answers_frame, text="",
                                      font="Arial 15", width=35, bg="yellow", fg="blue",
                                      command=lambda: self.reveal_answer(self.top_left))
        self.top_left_button.grid(column=0, row=0, padx=5, pady=5)

        self.top_right_button = Button(self.answers_frame, text="",
                                       font="Arial 15", width=35, bg="yellow", fg="blue",
                                       command=lambda: self.reveal_answer(self.top_right))
        self.top_right_button.grid(column=1, row=0)

        # Bottom level button
        self.bottom_left_button = Button(self.answers_frame, text="",
                                         font="Arial 15", width=35, bg="yellow", fg="blue",
                                         command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_left_button.grid(column=0, row=1)

        self.bottom_right_button = Button(self.answers_frame, text="",
                                          font="Arial 15", width=35, bg="yellow", fg="blue",
                                          command=lambda: self.reveal_answer(self.bottom_right))
        self.bottom_right_button.grid(column=1, row=1)

        # Label for results
        self.result_label = Label(self.game_box, font="Arial 14 bold", fg="black")
        self.result_label = Label(self.game_box, font="Arial 14 bold", fg="blue",
                                  text="{} correct / {} rounds played".format(self.result,
                                                                             self.rounds_played))
        self.result_label.grid(row=4, column=0)

        self.all_calc_list = [self.result, self.rounds_played]

        # Help button (row 5)
        self.help_button_frame = Frame(self.game_box, pady=10)
        self.help_button_frame.grid(row=6, column=0, pady=10)

        # Help button
        self.help_button = Button(self.game_box, text="Help/Rules",
                                  font="Arial 10 bold",
                                  bg="yellow", fg="blue", width=20,
                                  command=self.to_help)
        self.help_button.grid(row=7, column=0, pady=10)

        # history Button (row 1)
        self.history_button = Button(self.game_box, text="Norse God Quiz Export/Save", fg="blue",
                                     font="Arial 10 bold", width=25, height=2,
                                     bg="yellow", command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=8, padx=15, pady=15)

        # Next button
        self.next_button = Button(self.game_box, width=15, height=1, text="next", background="yellow", fg="blue",
                                  command=lambda: self.to_next(my_list))
        self.next_button.grid(row=6, column=0, pady=10)

        # Disable the next button
        self.next_button.config(state=DISABLED)
        self.to_next(my_list)

    # check answer
    def reveal_answer(self, location):

        # Disable all the buttons
        self.top_left_button.config(state=DISABLED)
        self.top_right_button.config(state=DISABLED)
        self.bottom_left_button.config(state=DISABLED)
        self.bottom_right_button.config(state=DISABLED)

        # Enable the next_button again
        self.next_button.config(state=NORMAL)

        # Rounds played as game played
        self.rounds_played += 1

        # Check
        if location == self.answer:
            self.answer_label.config(text="Nice!!!", fg="Light Green")
            self.answer_label.config(text="Nice One!!!", fg="Light Green")
            self.result += 1
        else:
            self.answer_label.config(text="No!", fg="Red")
            self.answer_label.config(text="Better Luck Next Time!", fg="Red")

        # refreshed result after right or wrong
        self.result_label.config(text="{} correct / {} Questions Answered".format(self.result, self.rounds_played))

    # To Next defined
    # the next function
    def to_next(self, list):
        self.top_left_button.config(state=NORMAL)
        self.top_right_button.config(state=NORMAL)
        self.bottom_left_button.config(state=NORMAL)
        self.bottom_right_button.config(state=NORMAL)
        self.next_button.config(state=DISABLED)
        self.answer_label.config(text="")

        # Randomized four gods from list again
        question_answer = random.choice(list)
        nope = random.choice(list)
        no = random.choice(list)
        close = random.choice(list)

        # defining variables, correct and wrong answer defined again
        self.question = question_answer[1]
        self.answer = question_answer[0]
        incorrect_answer_1 = nope[0]
        incorrect_answer_2 = no[0]
        incorrect_answer_3 = close[0]
        print(question_answer)

        self.norse_god_label.config(text=self.question)


        # Answer List again
        answer_list = [self.answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3]
        random.shuffle(answer_list)

        # Define said answer again
        self.top_left = answer_list[0]
        self.top_right = answer_list[1]
        self.bottom_right = answer_list[2]
        self.bottom_left = answer_list[3]

        # Defining the randomized list
        # Top level
        self.top_left_button.config(text=self.top_left, command=lambda: self.reveal_answer(self.top_left))

        self.top_right_button.config(text=self.top_right, command=lambda: self.reveal_answer(self.top_right))

        # Bottom level
        self.bottom_left_button.config(text=self.bottom_left, command=lambda:
        self.reveal_answer(self.bottom_left))

        self.bottom_right_button.config(text=self.bottom_right, command=lambda:
        self.reveal_answer(self.bottom_right))

        # History function
    def history(self, calc_history):
        History(self, calc_history)

    def to_quit(self):
        root.destroy()

    def to_help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="You will choose 1 of the 4 answers and one of them will"
                                          "be the correct answer. \n\n "
                                          "There are 25 different questions all on the different"
                                          " norse gods."
                                          "You Can save your results when ever you feel like you want"
                                          " to. \n\n After the 25 questions it will repeat a question. ")


class Help:
    def __init__(self, partner):
        background = "white"

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
        self.help_text = Label(self.help_frame, text=". ", font="arial 15 bold",
                               fg="blue", bg=background, justify=LEFT, wrap=350)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="yellow", fg="blue",
                                  font="Aerial" "10" "bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class History:
    def __init__(self, partner, calc_history):


        self.result = partner.result


        self.rounds_played = partner.rounds_played

        # This color is black
        background = "white"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press 'x' cross at the top, closes history and 'releases' history button.
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation history",
                                 font=("Arial", "15", "bold",), fg="blue",
                                 bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your calculations in the most recent run.",
                                  fg="blue",
                                  justify=LEFT, width=40, bg=background, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # Label for results
        self.result_label = Label(self.history_frame, font="Arial 14 bold", fg="blue", bg="white",
                                  text="{} correct / {} rounds played".format(self.result,
                                                                              self.rounds_played))
        self.result_label.grid(row=2, column=0)

        # refreshed result after right or wrong
        self.result_label.config(text="{} correct / {} rounds played".format(self.result, self.rounds_played))

        # history Output goes here... (Row 2)
        # Generate string from list of calcualtions...
        self.history_text.config(text="Here are your most game results ", fg="blue")

        # Export /Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export", fg="blue",
                                    background="yellow",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss", background="yellow",
                                  fg="blue",
                                  font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)


class Export:
    def __init__(self, partner, calc_history):
        print(calc_history)

        self.result = partner.result
        self.rounds_played = partner.rounds_played

        # This color is black
        background = "white"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press 'x' cross at the top, closes export and 'releases' export button.
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font=("Arial", "15", "bold",), fg="blue",
                                 bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below", fg="blue",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename you entered already exists,"
                                                         "it will overwrite anything that is there.", justify=LEFT, bg=background,
                                 fg='blue', font="Arial 10 italic",
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="blue",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save", bg=background,
                                  background="yellow", fg="blue",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", bg=background,
                                    background="yellow", fg="blue",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

    def save_history(self, partner, calc_history):

        global problem
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = " (no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.save_error_label.config(text="Invalid  - {}".format(problem))

            self.filename_entry.config(bg="yellow")
            print()

        else:
            filename = filename + ".txt"

            f = open(filename, "w+")

            for item in calc_history:
                f.write("You got {}/{} right. Nice Job !!\n".format(self.result, self.rounds_played))

            f.close()

            self.close_export(partner)


if __name__ == "__main__":
    root = Tk()
    root.title("Norse God Quiz")
    play = Start(root)
    root.mainloop()

    # Had help from David Pham, Yichen Hsiao And Woojin Jeon
    # Help from Mrs G as well as most of my code was recycled from her mystery box code.