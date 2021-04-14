import Model.main as model
import View.main as view
from operator import attrgetter


class Tournament:
    play = True
    def __init__(self):
        pass

    @staticmethod
    def create():
        players_list = [model.Player("Duthil", "Alexandre", "02/11/1998", "Homme", "1234"), model.Player("Ouvrard",
                     "Geoffrey", "29/04/1998","Homme", "1467"),model.Player("Agassi", "André", "29/04/1970","Homme", "1189"),
                        model.Player("Federer", "Roger", "09/08/1981", "Homme", "1689")]
        tours = "infos tournées" #j'invente une info de tournée pour l'instant, calcul plus tard
        # infos = AskInfos.tournamentInfos()
        # players_list = []
        # for player in infos[3]:
        #     players_list.append(PlayerController.createWithInfos(player))
        # new_tournament = Tournament(infos[0], infos[1], infos[2], tours, players_list, infos[4], infos[5], infos[6])
        new_tournament = model.Tournament("Tournoi test", "Poitiers", "24/04/2021", "tournée", players_list, "blitz", "rien à dire")
        print(new_tournament)
        Tournament.start(new_tournament)

    @staticmethod
    def start(tournament):
        for i in range(int(tournament.round_number)):
            Tournament.setRound(i + 1, tournament)
            view.ShowInfos.tournamentResults(sorted(tournament.players, key=attrgetter("score"), reverse=True))
            # TODO : c'est là que je dois continuer le tournoi, créer l'affichage des scores et enregistrer l'objet Tournament
            # TODO : le système ne sait pas comment classer les joueurs qui ont le même score sur le tournoi
            tournament.end()

    @staticmethod
    def setRound(round_number, tournament):
        this_round = model.Round(round_number)
        this_round.match_list = Tournament.setMatches(round_number, tournament)
        print(this_round.name)
        view.ShowInfos.round_matches(this_round.match_list)
        for match in this_round.match_list:
            Tournament.enterMatchResult(match)

    # TODO : le méthode setMatches ne prend pas en compte le fait que les joueurs se soient déja affrontés pour l'instant'
    @staticmethod
    def setMatches(round_number, tournament):
        match_list = []
        players_list = tournament.players
        if round_number == 1:
            players_list = sorted(players_list, key=attrgetter("rating"))
            for i in range(int(len(players_list)/2)):
                match_list.append(model.Match(players_list[i], players_list[i + int(len(players_list)/2)]))
        else:
            players_list = sorted(players_list, key=attrgetter("score"))
            for i in range(int(len(players_list))):
                if i%2 != 0:
                    match_list.append(model.Match(players_list[i], players_list[i - 1]))
        return match_list

    @staticmethod
    def enterMatchResult(match):
        result = view.AskInfos.matchResult(match)
        if result == "1":
            match.player1win()
        if result == "2":
            match.player2win()
        if result == "3":
            match.draw()


    @staticmethod
    def menu():
        response = view.Menu.main()
        if response == "1":
            Tournament.create()
        if response == "2":
            Player.create()
        if response == "3":
            view.ShowInfos.player_list(sorted(model.dataHandler.playerDeserializer(model.dataHandler.getPlayers()),
                                         key=attrgetter("last_name", "first_name")))
        if response == "4":
            Player.modifyRating()
        if response == "5":
            Tournament.play = False



class Player:
    def __init__(self):
        pass

    @staticmethod
    def create():
        infos = view.AskInfos.playerInfos()
        new_player = model.Player(infos[0], infos[1], infos[2], infos[3], infos[4])
        if model.dataHandler.checkExistance(new_player):
            print("Ce joueur existe déja dans la base de donnée")
        else:
            model.dataHandler.save(new_player)
            print("Le joueur {} a bien été créé".format(new_player.first_name))
            return new_player

    @staticmethod
    def createWithInfos(infos):
        new_player = model.Player(infos[0], infos[1], infos[2], infos[3], infos[4])
        print("Le joueur {} a bien été créé".format(new_player.first_name))
        # players_list.append(new_player) -> plus nécessaire
        return new_player

    @staticmethod
    def modifyRating():
        last_name, first_name, birthdate, new_rating = view.AskInfos.newRating()
        model.dataHandler.modifyRating(last_name, first_name, birthdate, new_rating)


