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


def to_help(self):
    Help(self)

    # Help Button row 3
    self.help_button = Button(self.start_frame, text="Help", font="Helvetica 10 bold", height=2, width=10,
                              borderwidth=3, command=self.to_help)
    self.help_button.grid(row=3, pady=5)