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
    def round_matches(match_list):
        print("""
        Voici les matchs de ce round : 
        {}
        {}      
        """.format(match_list[0], match_list[1]))

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
