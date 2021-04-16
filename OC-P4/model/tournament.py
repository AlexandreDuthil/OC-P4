
class Tournament:
    def __init__(self, name, place, date, tours, players, timing_style, description, round_number=4):
        self.name = name.capitalize()
        self.place = place.capitalize()
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
        Joueurs : {}
        Contrôle du temps : {}
        Description : {}
        """.format(self.name, self.place, self.date, self.round_number,
                   Tournament.display_players(self), self.timing_style, self.description)

    def display_players(self):
        display_players = ""
        for player in self.players:
            display_players += player.first_name + " " + player.last_name + ","
        return display_players
