import time
import datetime

# classe destinée à la l'input d'informations
class AskInfos:
    def __init__(self):
        pass

    # récupération des infos nécessaires à la création d'un objet Tournament
    @staticmethod
    def tournamentInfos():
        name = input("Quel est le nom du tournoi ? : ")
        place = input("Quelle est la ville du tournoi ? : ")
        date = input("Date du tournoi ? : ")
        players_number = input("Combien y a-t-il de joueurs ? : ")
        round_number = input("Combien de tour ? : ")
        players_list = []
        x = 1
        for i in range(int(players_number)):
            print("Joueur " + str(x))
            players_list.append(AskInfos.playerInfos())
            x += 1
        timing_style = input("Quel style de partie ? : ")
        description = input("Description ? : ")

        return [name, place, date, players_list, timing_style, description, round_number]

    # récupération des infos nécessaires à la création d'un objet Player
    @staticmethod
    def playerInfos():
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birthdate = input("Date de naissance : ")
        sex = input("Sexe : ")
        rating = input("Classement : ")
        return [last_name, first_name, birthdate, sex, rating]

    @staticmethod
    def matchResult(match):
        result = input("Qui a gagné le match ?\n1 = {}\n2 = {}\n3 = égalité".format(match.player1, match.player2))
        return result



    @staticmethod
    def menu():
        # menu principal
        print("Bienvenue dans votre gestionnaire de tournoi d'échecs")
        response = input("Que voulez-vous faire ? \n1 = Créer un tournoi\n2 = Créer un joueur\n"
                         "3 = Afficher la liste des joueurs\n" )
        return response

# classe destinée à l'affichage d'infos
class ShowInfos:
    def __init__(self):
        pass

    @staticmethod
    def player_list(player_list):
        for player in player_list:
            print(player)

    @staticmethod
    def show_round_matches(match_list):
        print("""
        Voici les matchs de ce round : 
        {}
        {}      
        """.format(match_list[0], match_list[1]))
