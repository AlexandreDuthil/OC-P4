from Model.main import *
from View.main import *
from operator import attrgetter

class TournamentController:
    def __init__(self):
        pass

    @staticmethod
    def create():
        players_list = [Player("Duthil", "Alexandre", "02/11/1998", "Homme", "1234"), Player("Ouvrard",
                     "Geoffrey", "29/04/1998","Homme", "1467"),Player("Agassi", "André", "12/12/1987","Homme", "1189"),
                        Player("Federer", "Roger", "25/07/1977", "Homme", "1689")]
        tours = "infos tournées" #j'invente une info de tournée pour l'instant, calcul plus tard
        # infos = AskInfos.tournamentInfos()
        # players_list = []
        # for player in infos[3]:
        #     players_list.append(PlayerController.createWithInfos(player))
        # new_tournament = Tournament(infos[0], infos[1], infos[2], tours, players_list, infos[4], infos[5], infos[6])
        new_tournament = Tournament("Tournoi test", "Poitiers", "24/04/2021", "tournée", players_list, "blitz", "rien à dire")
        print(new_tournament)
        TournamentController.start(new_tournament)

    @staticmethod
    def start(tournament):
        for i in range(int(tournament.round_number)):
            TournamentController.setRound(i+1, tournament)

    @staticmethod
    def setRound(round_number, tournament):
        this_round = Round(round_number)
        this_round.match_list = TournamentController.setMatches(round_number, tournament)
        print(this_round.name)
        ShowInfos.show_round_matches(this_round.match_list)
        for match in this_round.match_list:
            TournamentController.enterMatchResult(match)



    @staticmethod
    def setMatches(round_number, tournament):
        match_list = []
        players_list = tournament.players
        if round_number == 1:
            players_list = sorted(players_list, key=attrgetter("rating"))
            for i in range(int(len(players_list)/2)):
                # match_list.append(((players_list[i]), players_list[i + int(len(players_list)/2)]))
                match_list.append(Match(players_list[i], players_list[i + int(len(players_list)/2)]))
        else:
            players_list = sorted(players_list, key=attrgetter("score"))
            for i in range(int(len(players_list))):
                if i%2 != 0:
                    # match_list.append((players_list[i], players_list[i - 1]))
                    match_list.append(Match(players_list[i], players_list[i - 1]))
        return match_list

    @staticmethod
    def enterMatchResult(match):
        result = AskInfos.matchResult(match)
        if result == "1":
            match.player1win()
        if result == "2":
            match.player2win()
        if result == "3":
            match.draw()


    @staticmethod
    def menu():
        response = AskInfos.menu()
        if response == "1":
            TournamentController.create()
        if response == "2":
            PlayerController.create()
        if response == "3":
            ShowInfos.player_list(sorted(players_list, key=attrgetter("last_name", "first_name")))

class PlayerController:
    def __init__(self):
        self.player_number = 1
        pass

    @staticmethod
    def create():
        infos = AskInfos.playerInfos()
        new_player = Player(infos[0], infos[1], infos[2], infos[3], infos[4])
        print("Le joueur {} a bien été créé".format(new_player.first_name))
        players_list.append(new_player)
        return new_player

    @staticmethod
    def createWithInfos(infos):
        new_player = Player(infos[0], infos[1], infos[2], infos[3], infos[4])
        print("Le joueur {} a bien été créé".format(new_player.first_name))
        players_list.append(new_player)
        return new_player

    @staticmethod
    def modifyScore(player, score):
        players_list

