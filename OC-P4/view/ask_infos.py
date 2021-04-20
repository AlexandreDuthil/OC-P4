# classe destinée à la l'input d'informations
class AskInfos:
    def __init__(self):
        pass

    @staticmethod
    def main():
        # menu principal
        print("Bienvenue dans votre gestionnaire de tournoi d'échecs")
        return input("Que voulez-vous faire ? \n1 = Créer un tournoi\n"
                     "2 = Créer un joueur\n"
                     "3 = Afficher la liste des joueurs\n"
                     "4 = Modifier le classement d'un joueur\n"
                     "5 = Afficher les liste des tournois\n"
                     "6 = Afficher les résultats d'un tournoi\n"
                     "7 = Quitter le programme\n")

    @staticmethod
    def sorting_method():
        print("Les joueurs doivent être triés par :")
        return input("1 = Ordre alphabétique\n2 = Classement\n")

    # récupération des infos nécessaires à la création d'un objet Tournament
    @staticmethod
    def tournament_name():
        name = input("Quel est le nom du tournoi ? : ")
        return name

    @staticmethod
    def tournament_place():
        place = input("Quelle est la ville du tournoi ? : ")
        return place

    @staticmethod
    def tournament_date():
        date = input("Date du tournoi ? : ")
        return date

    @staticmethod
    def tournament_player_number():
        players_number = input("Combien y a-t-il de joueurs ? : ")
        return players_number

    @staticmethod
    def tournament_round_number():
        round_number = input("Combien de tour ? : ")
        return round_number

    @staticmethod
    def tournament_timing_style():
        timing_style = input("Quel style de partie ? (Bullet, Blitz ou "
                             "Coup rapide ) : ")
        return timing_style

    @staticmethod
    def tournament_description():
        description = input("Description ? : ")
        return description

    # récupération des infos nécessaires à la création d'un objet Player
    @staticmethod
    def player_last_name():
        last_name = input("Nom de famille : ")
        return last_name

    @staticmethod
    def player_first_name():
        first_name = input("Prénom : ")
        return first_name

    @staticmethod
    def player_birthdate():
        birthdate = input("Date de naissance ( XX/XX/XXXX ) : ")
        return birthdate

    @staticmethod
    def player_sex():
        sex = input("Sexe (H/F): ")
        return sex

    @staticmethod
    def player_rating():
        rating = input("Classement : ")
        return rating

    @staticmethod
    def match_result(match):
        result = input("Qui a gagné le match ?\n1 = {}\n2 = {}\n3 = égalité\n"
                       "".format(match.player1, match.player2))
        return result

    @staticmethod
    def new_rating():
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birthdate = input("Date de naissance : ")
        new_rating = input("Nouveau classement : ")
        return last_name, first_name, birthdate, new_rating

    @staticmethod
    def view_tournament():
        name = (input("Nom du tournoi : ")).capitalize()
        place = (input("Ville : ")).capitalize()
        date = input("Date du tournoi : ")
        return name, place, date
