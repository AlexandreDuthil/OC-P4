import time
import datetime

class Tournament:
    def __init__(self, name, place, date, tours, players, timing_style, description, round_number=4):
        self.name = name
        self.place = place
        self.date = date
        self.tours = tours
        self.players = players
        self.timing_style = timing_style
        self.description = description
        self.round_number = round_number
        self.rounds = []


    def __repr__(self):
        return """
        Nom du tournoi : {}
        Lieu : {}
        Date : {}
        Nombre de tour : {}
        Tournées : {}
        Joueurs : {}
        Contrôle du temps : {}
        Description : {}
        """.format(self.name, self.place, self.date, self.round_number, self.tours,
                Tournament.display_players(self), self.timing_style, self.description)
    def display_players(self):
        display_players = ""
        for player in self.players:
            display_players += player.first_name + " " + player.last_name + ","
        return display_players


class Player:
    def __init__(self, last_name, first_name, birthdate, sex, rating):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.sex = sex
        self.rating = rating
        self.attributs = ["last_name", "first_name", "birthdate", "sex", "rating"]
        self.score = 0

    def __repr__(self):
        return """{} {}, {}, {}, {}, score={}""".format( self.last_name, self.first_name, self.birthdate, self.sex, self.rating, self.score)
        # return """
        # Nom : {}
        # Prénom : {}
        # Date de naissance : {}
        # Sexe : {}
        # Classement : {}
        # """.format(self.last_name, self.first_name, self.birthdate, self.sex, self.rating)

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        # self.match_end = False

    def player1win(self):
        self.player1.score += 1
        # self.match_end = True
        pass

    def player2win(self):
        self.player2.score += 1
        # self.match_end = True
        pass

    def match_nul(self):
        self.player1.score += 0.5
        self.player2.score += 0.5
        # self.match_end = True
        pass

    def __repr__(self):
        return "{} contre {}".format(self.player1, self.player2)

class Round:
    def __init__(self, number):
        self.name = "Round" + str(number)
        self.starting_date = datetime.date.today()
        self.starting_time = time.strftime("%Hh%M")
        self.match_list = []

    def end(self):
        self.ending_date = datetime.date.today()
        self.ending_time = time.strftime("%Hh%M")

players_list = [Player("Duthil", "Alexandre", "02/11/1998", "Homme", "1234"), Player("Ouvrard",
            "Geoffrey", "29/04/1998", "Homme", "1467"), Player("Agassi", "André", "12/12/1987",
            "Homme", "1189"), Player("Federer", "Roger", "25/07/1977", "Homme", "1689")]
mon_tournoi = Tournament("the best", "Poitiers", "24/04/2021", 4, players_list, "blitz", "rien à dire")