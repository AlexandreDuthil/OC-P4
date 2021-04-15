
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
        print("Le tournoi a commencé")

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
