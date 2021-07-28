class Stats:
    def __init__(self, partner):
        print(Stats)

        # The color is yellow
        background = "yellow"

        # Amounts of rounds that were played.
        self.rounds_played = partner.rounds_played

        # Disable stats button
        partner.start_statistics_button.config(state=DISABLED)

        # Sets up child window (ie: stats box)
        self.stats_box = Toplevel()

        # If users press 'x' cross at the top, closes stats and 'releases' stats button.
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box, bg=background)
        self.stats_frame.grid()

        # Set up Help heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics", bg="yellow", fg="blue",
                                         font="Arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # Stats text (label, row 1)
        self.stats_text = Label(self.stats_frame, text="", bg="yellow", fg="blue",
                                justify=LEFT, width=40, wrap=250)
        self.stats_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_buttom = Button(self.stats_frame, text="Dismiss", width=10, bg="yellow",
                                  fg="blue",
                                  font="arial" "10" "bold",
                                  command=partial(self.close_stats, partner))
        self.dismiss_buttom.grid(row=2, pady=10)

        # Label for results
        self.result_label = Label(self.stats_frame, font="Arial 14 bold", fg="blue", bg="yellow",
                                  text="{} correct / {} rounds played".format(self.result,
                                                                              self.rounds_played))
        self.result_label.grid(row=4, column=0)

        # refreshed result after right or wrong
        self.result_label.config(text="{} correct / {} rounds played".format(self.result, self.rounds_played))

    def close_stats(self, partner):
        # Put help button back to normal...
        partner.start_statistics_button.config(state=NORMAL)
        self.stats_box.destroy()