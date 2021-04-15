from model.player import Player
from model.tournament import Tournament
from helpers.round import Round
from helpers.match import Match
from tinydb import TinyDB, Query

db = TinyDB("chess.json")
tournament_table = db.table("tournament")
players_table = db.table("players")
Searcher = Query()


class DataHandler:
    def __init__(self):
        pass

    @staticmethod
    def serializer(object):
        if isinstance(object, Player):
            return {"last_name": object.last_name, "first_name": object.first_name,
                    "birthdate": object.birthdate, "sex": object.sex, "rating": object.rating}
        if isinstance(object, Tournament):
            return {"name": object.name, "place": object.place, "date": object.date, "tours": object.tours,
                    "players": DataHandler.serializer(object.players), "timing_style": object.timing_style,
                    "description": object.description, "round_number": object.round_number,
                    "rounds": DataHandler.serializer(object.rounds)}
        if isinstance(object, Match):
            return {"player1": object.player1, "player2": object.player2,
                    "result": object.result}
        if isinstance(object, Round):
            return {"name": object.name, "starting_date": object.starting_date,
                    "starting_time": object.starting_time, "match_list": DataHandler.serializer(object.match_list),
                    "ending_date": object.ending_date, "ending_time": object.ending_time}
        if isinstance(object, list):
            if isinstance(object[0], Player):
                players_list = []
                for player in object:
                    players_list.append({"lastname": player.last_name, "firstname": player.first_name,
                                         "birthdate": player.birthdate, "sex": player.sex, "rating": player.rating})
                return players_list
            if isinstance(object[0], Tournament):
                tournament_list = []
                for tournament in object:
                    players_list = []
                    for player in tournament.players:
                        players_list.append(DataHandler.serializer(player))
                    tournament_list.append({"name": tournament.name, "place": tournament.place, "date": tournament.date,
                                            "tours": tournament.tours,
                                            "players": players_list, "timing_style": tournament.timing_style,
                                            "description": tournament.description,
                                            "round_number": tournament.round_number})
                return tournament_list
            if isinstance(object[0], Round):
                round_list = []
                for round in object:
                    round_list.append({"name": round.name, "starting_date": round.starting_date,
                                       "starting_time": round.starting_time, "match_list": round.match_list,
                                       "ending_date": round.ending_date, "ending_time": round.ending_time})
                return round_list
            if isinstance(object[0], Match):
                match_list = []
                for match in object:
                    match_list.append({"player1": match.player1, "player2": match.player2,
                                       "result": match.result})
        # TODO : erreur de serialisation des objets Date à gérer

    @staticmethod
    def player_deserializer(object): # TODO : création d'un deserializer pour les tournoi, round et match
        players_list = []
        for player in object:
            players_list.append(Player(player["last_name"], player["first_name"], player["birthdate"],
                                       player["sex"], player["rating"]))
        return players_list

    @staticmethod
    def get_players():
        return players_table.all()

    @staticmethod
    def save(object):
        if isinstance(object, Player):
            players_table.insert(DataHandler.serializer(object))
        if isinstance(object, Tournament):
            tournament_table.insert(DataHandler.serializer(object))
        if isinstance(object, list):
            if isinstance(object[0], Player):
                for player in object:
                    players_table.insert(DataHandler.serializer(object))
            if isinstance(object[0], Tournament):
                for tournament in object:
                    tournament_table.insert(DataHandler.serializer(object))

    @staticmethod
    def search(object, first_name=None, birthdate=None):
        if isinstance(object, Player):
            return players_table.search(
                Searcher.first_name == object.first_name and Searcher.last_name == object.last_name and Searcher.birthdate == object.birthdate)
        if isinstance(object, Tournament):
            return tournament_table.search(Searcher.name == object.name and Searcher.date == object.date)
        else:
            return players_table.search(
                Searcher.last_name == object and Searcher.first_name == first_name and Searcher.birthdate == birthdate)

    @staticmethod
    def modify_rating(last_name, first_name, birthdate, new_rating):
        if not DataHandler.check_existance(last_name, first_name, birthdate):
            print("Joueur introuvable dans la base de données")
        else:
            players_table.update({"rating": new_rating},
                                 Searcher.last_name == last_name and Searcher.first_name == first_name and Searcher.birthdate == birthdate)
            print("Le classement du joueur a bien été mis à jour")

    @staticmethod
    def check_existance(object, first_name=None, birthdate=None):
        if isinstance(object, Player):
            return True if DataHandler.search(object) else False
        else:
            return True if DataHandler.search(object, first_name, birthdate) else False
