import time
import datetime


class Round:
    def __init__(self, number):
        self.name = "Round" + str(number)
        self.starting_date = datetime.date.today()
        self.starting_time = time.strftime("%Hh%M")
        self.match_list = []
        self.ending_date = None
        self.ending_time = None

    def end(self):
        self.ending_date = datetime.date.today()
        self.ending_time = time.strftime("%Hh%M")