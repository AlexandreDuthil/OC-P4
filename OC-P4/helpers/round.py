import time
import datetime


class Round:
    def __init__(self, number=1):
        self.name = "Round" + str(number)
        self.starting_date = datetime.date.today().strftime("%d/%m/%Y")
        self.starting_time = time.strftime("%Hh%M")
        self.match_list = []
        self.ending_date = None
        self.ending_time = None

    def end(self):
        self.ending_date = datetime.date.today().strftime("%d/%m/%Y")
        self.ending_time = time.strftime("%Hh%M")

    def __repr__(self): # TODO : problème d'affichage des joueurs dans les matchs
        return """{}
              Date et heure de début : {}, {}
              Liste des matchs : {}
              Date et heure de fin : {} {}""".format(self.name, self.starting_date, self.starting_time,
                                                    self.match_list, self.ending_date, self.ending_time)
