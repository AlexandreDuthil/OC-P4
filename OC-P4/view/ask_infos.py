# classe destinée à la l'input d'informations
class AskInfos:
    def __init__(self):
        pass

    @staticmethod
    def main():
        # menu principal
        print("Bienvenue dans votre gestionnaire de tournoi d'échecs")
        return input("Que voulez-vous faire ? \n1 = Créer un tournoi\n2 = Créer un joueur\n"
                     "3 = Afficher la liste des joueurs\n4 = Modifier le classement d'un joueur\n"
                     "5 = Afficher les liste des tournois\n6 = Afficher les résultats d'un tournoi\n"
                     "7 = Quitter le programme\n")

    @staticmethod
    def sorting_method():
        print("Les joueurs doivent être triés par :")
        return input("1 = Ordre alphabétique\n2 = Classement\n")

    # récupération des infos nécessaires à la création d'un objet Tournament
    @staticmethod
    def tournament_infos():  # TODO : ne permet pas de choisir un joueur déja existant dans la BDD
        name = input("Quel est le nom du tournoi ? : ")
        place = input("Quelle est la ville du tournoi ? : ")
        date = input("Date du tournoi ? : ")
        players_number = input("Combien y a-t-il de joueurs ? : ")
        round_number = input("Combien de tour ? : ")
        timing_style = input("Quel style de partie ? : ")
        description = input("Description ? : ")

        return [name, place, date, players_number, timing_style, description, round_number]

    # récupération des infos nécessaires à la création d'un objet Player
    @staticmethod
    def player_infos():
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birthdate = input("Date de naissance : ")
        sex = input("Sexe : ")
        rating = input("Classement : ")
        return [last_name, first_name, birthdate, sex, rating]

    @staticmethod
    def match_result(match):
        result = input("Qui a gagné le match ?\n1 = {}\n2 = {}\n3 = égalité\n".format(match.player1, match.player2))
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
