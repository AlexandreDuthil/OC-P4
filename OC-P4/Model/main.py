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
        """.format(self.name, self.place, self.date, self.round_number, self.tours, self.players, self.timing_style, self.description)


class Player:
    def __init__(self, last_name, first_name, birthdate, sex, rating):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.sex = sex
        self.rating = rating
        self.attributs = ["last_name", "first_name", "birthdate", "sex", "rating"]

    def __repr__(self):
        return """
        Nom : {}
        Prénom : {}
        Date de naissance : {}
        Sexe : {}
        Classement : {}
        """.format(self.last_name, self.first_name, self.birthdate, self.sex, self.rating)

class Match:
    def __init__(self, player1_name, player2_name):
        self.player1 = [player1_name, player1_score]
        self.player2 = [player2_name, player2_score]
    def __str__(self):
        return (self.player1, self.player2)

class Round:
    def __init__(self, name):
        self.name = name
        self.starting_date = datetime.date.today()
        self.starting_time = time.strftime("%Hh%M")
        self.match_list = []

    def end(self):
        self.ending_date = datetime.date.today()
        self.ending_time = time.strftime("%Hh%M")