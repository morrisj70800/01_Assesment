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

        # Get list from csv and import it
        # name of csv file goes here...
        with open('q_and_a_csv.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        valid_questions = []
        for item in data:
            if item[0] != "ignore_me":
                valid_questions.append(item)

            question_ans = random.choice(valid_questions)
            question = question_ans[0]
            answer = question_ans[1]

            answer_options = [answer]
            for option in range(0, 3):
                # choose answer
                wrong_ans = random.choice(data)
                wrong = wrong_ans[1]
                answer_options.append(wrong)

        # choose an item from the main list, this item is itself a list
        question_ans = random.choice

        # List to store the answers
        self.game_history = []

        # result
        self.result = 0
        # Amounts of game
        self.rounds_played = 0

        # define  answers
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
                                     font="Arial 15", bg="yellow")
        self.Norse_god_label.grid(row=0)

        # Answer Label
        self.answer_label = Label(self.game_frame, text="", font="Arial 15")
        self.answer_label.grid(row=1)

        # Setup grid for answer buttons row 3
        self.answers_frame = Frame(self.game_box)
        self.answers_frame.grid(row=3)

        # Top  buttons
        self.top_left_button = Button(self.answers_frame, text="Top Left",
                                      font="Arial 20", bg="yellow",
                                      command=lambda: self.reveal_answer(self.top_left))
        self.top_left_button.grid(column=0, row=0, pady=10)

        self.top_right_button = Button(self.answers_frame, text="Top Right",
                                       font="Arial 20", bg="yellow",
                                       command=lambda: self.reveal_answer(self.top_right))
        self.top_right_button.grid(column=1, row=0, pady=10, padx=5)

        # Bottom level button
        self.bottom_left_button = Button(self.answers_frame, text="Bottom Left",
                                         font="Arial 20", bg="green",
                                         command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_left_button.grid(column=0, row=1, pady=10)

        self.bottom_right_button = Button(self.answers_frame, text="Bottom Right",
                                          font="Arial 20", bg="green",
                                          command=lambda: self.reveal_answer(self.bottom_right))
        self.bottom_right_button.grid(column=1, row=1, pady=10, padx=5)

        # results label
        self.result_label = Label(self.game_box, text="{} right / {} rounds played".format(self.result,
                                                                                           self.rounds_played))
        self.result_label.grid(row=5)

        # Next button
        self.next_button = Button(self.game_box, text="next", bg="yellow", command=lambda: self.to_next)
        self.next_button.grid(row=4)

        # Disable the next button
        self.next_button.config(state=DISABLED)

    def reveal_answer(self, location):

        # refreshed result after right or wrong
        self.result_label.config(text="{} right / {} rounds played".format(self.result, self.rounds_played))

    # To Next defined
    def to_next(self):
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

        self.Norse_god_label.config(text=self.question)

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
        self.bottom_left_button.config(text=self.bottom_left, command=lambda: self.reveal_answer(self.bottom_left))

        self.bottom_right_button.config(text=self.bottom_right, command=lambda: self.reveal_answer(self.bottom_right))


if __name__ == "__main__":
    root = Tk()
    root.title("Norse God Quiz")
    play = Start(root)
    root.mainloop()
