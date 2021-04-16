# classe destinée à l'affichage d'infos
class ShowInfos:
    def __init__(self):
        pass

    @staticmethod
    def player_list(player_list):
        for player in player_list:
            print(player)
        print("\n")

    @staticmethod
    def tournament_list(tournament_list):
        print("Voici la liste des tournois :")
        for tournament in tournament_list:
            print("Tournoi '{}', à {} le {}".format(tournament.name, tournament.place,
                                                    tournament.date))
        print("\n")

    @staticmethod
    def one_tournament(tournament):
        print(tournament)
        return input("1 = Afficher les joueurs et leurs résultats\n2 = Afficher les tours\n3 = Quitter")

    @staticmethod
    def rounds(round_list):
        for round in round_list:
            print(round)

    @staticmethod
    def round_matches(match_list):
        print("Voici les matchs de ce round :\n")
        for match in match_list:
            print("{}".format(match))

    @staticmethod
    def player_already_exists(player):
        print("""
        Le joueur {} existe déjà dans la base de données
        """.format(player))

    @staticmethod
    def tournament_results(players_list):
        print("Le tournoi est terminée, voici les résultats :\n")
        for i, player in enumerate(players_list):
            print("{}. {}, avec un score de {}".format(i+1, player, player.score))
        print("\n")
