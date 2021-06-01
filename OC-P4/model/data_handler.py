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
            return {"last_name": object.last_name,
                    "first_name": object.first_name,
                    "birthdate": object.birthdate, "sex": object.sex,
                    "rating": object.rating, "score": object.score}
        if isinstance(object, Tournament):
            return {"name": object.name, "place": object.place,
                    "date": object.date, "tours": object.tours,
                    "players": DataHandler.serializer(object.players),
                    "timing_style": object.timing_style,
                    "description": object.description,
                    "round_number": object.round_number,
                    "rounds": DataHandler.serializer(object.rounds)}
        if isinstance(object, Match):
            return {"player1": DataHandler.serializer(object.player1),
                    "player2": DataHandler.serializer(object.player2),
                    "result": object.result}
        if isinstance(object, Round):
            return {"name": object.name, "starting_date": object.starting_date,
                    "starting_time": object.starting_time,
                    "match_list": DataHandler.serializer(object.match_list),
                    "ending_date": object.ending_date,
                    "ending_time": object.ending_time}
        if isinstance(object, list):
            if isinstance(object[0], Player):
                players_list = []
                for player in object:
                    players_list.append({"last_name": player.last_name,
                                         "first_name": player.first_name,
                                         "birthdate": player.birthdate,
                                         "sex": player.sex,
                                         "rating": player.rating,
                                         "score": player.score})
                return players_list
            if isinstance(object[0], Tournament):
                tournament_list = []
                for tournament in object:
                    tournament_list.append({"name": tournament.name,
                                            "place": tournament.place,
                                            "date": tournament.date,
                                            "tours": tournament.tours,
                                            "players": DataHandler.serializer(
                                                tournament.players),
                                            "timing_style":
                                                tournament.timing_style,
                                            "description":
                                                tournament.description,
                                            "round_number":
                                                tournament.round_number,
                                            "rounds": DataHandler.serializer(
                                                tournament.rounds)})
                return tournament_list
            if isinstance(object[0], Round):
                round_list = []
                for round in object:
                    round_list.append({"name": round.name,
                                       "starting_date": round.starting_date,
                                       "starting_time": round.starting_time,
                                       "match_list": DataHandler.serializer(
                                           round.match_list),
                                       "ending_date": round.ending_date,
                                       "ending_time": round.ending_time})
                return round_list
            if isinstance(object[0], Match):
                match_list = []
                for match in object:
                    match_list.append({"player1": DataHandler.serializer(
                        match.player1),
                                       "player2": DataHandler.serializer(
                                           match.player2),
                                       "result": match.result})
                return match_list

    @staticmethod
    def player_deserializer(object):
        players_list = []
        if isinstance(object, list):
            for player in object:
                this_player = (Player(player["last_name"],
                                      player["first_name"],
                                      player["birthdate"],
                                      player["sex"], int(player["rating"])))
                this_player.score = player["score"]
                players_list.append(this_player)
        elif isinstance(object, Player):
            this_player = (Player(object["last_name"], object["first_name"],
                                  object["birthdate"],
                                  object["sex"], int(object["rating"])))
            this_player.score = object["score"]
            players_list.append(this_player)
        elif isinstance(object, dict):
            this_player = (Player(object["last_name"], object["first_name"],
                                  object["birthdate"],
                                  object["sex"], int(object["rating"])))
            players_list.append(this_player)
        return players_list

    @staticmethod
    def tournament_deserializer(object):
        tournament_list = []
        for tournament in object:
            this_tournament = Tournament(tournament["name"],
                                         tournament["place"],
                                         tournament["date"],
                                         tournament["tours"],
                                         DataHandler.player_deserializer(
                                             tournament["players"]),
                                         tournament["timing_style"],
                                         tournament["description"],
                                         tournament["round_number"])
            this_tournament.rounds = DataHandler.round_deserializer(
                tournament["rounds"])
            tournament_list.append(this_tournament)
        return tournament_list

    @staticmethod
    def round_deserializer(object):
        round_list = []
        for round in object:
            this_round = Round()
            this_round.name = round["name"]
            this_round.starting_date = round["starting_date"]
            this_round.starting_time = round["starting_time"]
            this_round.match_list = DataHandler.match_deserializer(
                round["match_list"])
            this_round.ending_date = round["ending_date"]
            this_round.ending_time = round["ending_time"]
            round_list.append(this_round)
        return round_list

    @staticmethod
    def match_deserializer(object):
        match_list = []
        for match in object:
            this_match = (Match((DataHandler.player_deserializer(
                match["player1"])[0]),
                                (DataHandler.player_deserializer(
                                    match["player2"])[0])))
            this_match.result = match["result"]
            match_list.append(this_match)
        return match_list

    @staticmethod
    def get_players():
        return players_table.all()

    @staticmethod
    def get_tournaments():
        return tournament_table.all()

    @staticmethod
    def save(object):
        if isinstance(object, Player):
            players_table.insert(DataHandler.serializer(object))
        elif isinstance(object, Tournament):
            tournament_table.insert(DataHandler.serializer(object))
        elif isinstance(object, list):
            if isinstance(object[0], Player):
                for player in object:
                    players_table.insert(DataHandler.serializer(player))
            if isinstance(object[0], Tournament):
                for tournament in object:
                    tournament_table.insert(DataHandler.serializer(tournament))

    @staticmethod
    def search_player(object, first_name=None, birthdate=None):
        if isinstance(object, Player):
            return players_table.search(
                Searcher.first_name == object.first_name and
                Searcher.last_name == object.last_name and
                Searcher.birthdate == object.birthdate)
        else:
            return players_table.search(
                Searcher.last_name == object and
                Searcher.first_name == first_name and
                Searcher.birthdate == birthdate)

    @staticmethod
    def search_tournament(name, place, date):
        return tournament_table.search(Searcher.name == name and
                                       Searcher.place == place and
                                       Searcher.date == date)

    @staticmethod
    def modify_rating(last_name, first_name, birthdate, new_rating):
        if not DataHandler.check_existance(last_name, first_name, birthdate):
            print("Joueur introuvable dans la base de données")
        else:
            players_table.update({"rating": new_rating},
                                 Searcher.last_name == last_name and
                                 Searcher.first_name == first_name and
                                 Searcher.birthdate == birthdate)
            print("Le classement du joueur a bien été mis à jour")

    @staticmethod
    def check_existance(object, info2=None, info3=None):
        if isinstance(object, Player):
            return True if DataHandler.search_player(object) else False
        else:
            return True if DataHandler.search_player(object, info2, info3)\
                else False
