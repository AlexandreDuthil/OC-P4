from model.player import Player
from model.tournament import Tournament
from view.show_infos import ShowInfos
from view.ask_infos import AskInfos
from helpers.round import Round
from helpers.match import Match
from model.data_handler import DataHandler
from operator import attrgetter


class Menu:
    play = True
    quit = True

    def __init__(self):
        self.actual_tournament = None

    def create_tournament(self):
        infos = AskInfos.tournament_infos()
        players_list = []
        x = 1
        tours = "rien"
        for i in range(int(infos[3])):
            print("Joueur " + str(x))
            players_list.append(Menu.create_player())
            x += 1
        self.actual_tournament = Tournament(infos[0], infos[1], infos[2],
                                            tours, players_list, infos[4],
                                            infos[5], infos[6])
        Menu.start(self)

    def start(self):
        for i in range(int(self.actual_tournament.round_number)):
            Menu.set_round(self, i + 1)
            ShowInfos.tournament_results(sorted(self.actual_tournament.players,
                                                key=attrgetter("score"),
                                                reverse=True))
        DataHandler.save(self.actual_tournament)
        self.actual_tournament = None

    def set_round(self, round_name):
        this_round = Round(round_name)
        this_round.match_list = Menu.set_matches(self)
        print(this_round.name)
        ShowInfos.round_matches(this_round.match_list)
        for match in this_round.match_list:
            Menu.enter_match_result(match)
        this_round.end()
        self.actual_tournament.rounds.append(this_round)

    # TODO : le méthode setMatches ne prend pas en compte le fait que les
    #  joueurs se soient déja affrontés'
    def set_matches(self):
        match_list = []
        players_list = self.actual_tournament.players
        if self.actual_tournament.round_number == 1:
            players_list = sorted(players_list, key=attrgetter("rating"))
            for i in range(int(len(players_list) / 2)):
                match_list.append(Match(players_list[i],
                                        players_list[i + int(len(
                                            players_list) / 2)]))
        else:
            players_list = sorted(players_list, key=attrgetter("score"))
            for i in range(int(len(players_list))):
                if i % 2 != 0:
                    match_list.append(Match(players_list[i],
                                            players_list[i - 1]))
        return match_list

    @staticmethod
    def enter_match_result(match):
        result = AskInfos.match_result(match)
        if result == "1":
            match.player1win()
        if result == "2":
            match.player2win()
        if result == "3":
            match.draw()

    def display(self):
        response = AskInfos.main()
        if response == "1":
            Menu.create_tournament(self)
        if response == "2":
            Menu.create_player()
        if response == "3":
            if AskInfos.sorting_method() == "1":
                ShowInfos.player_list(sorted(DataHandler.player_deserializer(
                    DataHandler.get_players()),
                    key=attrgetter("last_name", "first_name")))
            else:
                ShowInfos.player_list(sorted(DataHandler.player_deserializer(
                    DataHandler.get_players()),
                    key=attrgetter("rating"), reverse=True))
        if response == "4":
            Menu.modify_rating()
        if response == "5":
            ShowInfos.tournament_list(DataHandler.tournament_deserializer(
                DataHandler.get_tournaments()))
        if response == "6":
            Menu.view_tournament(self)
        if response == "7":
            Menu.play = False

    @staticmethod
    def create_player():
        infos = AskInfos.player_infos()
        new_player = Player(infos[0], infos[1], infos[2], infos[3], infos[4])
        if DataHandler.check_existance(new_player):
            print("Ce joueur existe déja dans la base de donnée")
            return new_player
        else:
            DataHandler.save(new_player)
            print("Le joueur {} a bien été créé".format(new_player.first_name))
            return new_player

    @staticmethod
    def create_with_infos(infos):
        new_player = Player(infos[0], infos[1], infos[2], infos[3], infos[4])
        print("Le joueur {} a bien été créé".format(new_player.first_name))
        # players_list.append(new_player) -> plus nécessaire
        return new_player

    @staticmethod
    def modify_rating():
        last_name, first_name, birthdate, new_rating = AskInfos.new_rating()
        DataHandler.modify_rating(last_name, first_name, birthdate, new_rating)

    def view_tournament(self):
        name, place, date = AskInfos.view_tournament()
        if DataHandler.search_tournament(name, place, date):
            self.actual_tournament = DataHandler.tournament_deserializer(
                DataHandler.search_tournament(name, place, date))[0]
            Menu.quit = False
            while not Menu.quit:
                response = ShowInfos.one_tournament(self.actual_tournament)
                if response == "1":
                    ShowInfos.tournament_results(
                        self.actual_tournament.players)
                if response == "2":
                    ShowInfos.rounds(self.actual_tournament.rounds)
                if response == "3":
                    if AskInfos.sorting_method() == "1":
                        ShowInfos.player_list(
                            sorted(self.actual_tournament.players,
                                   key=attrgetter("last_name", "first_name")))
                    else:
                        ShowInfos.player_list(
                            sorted(self.actual_tournament.players,
                                   key=attrgetter("rating"), reverse=True))
                if response == "4":
                    Menu.quit = True
                    self.actual_tournament = None
        else:
            print("Ce tournoi n'existe pas")
