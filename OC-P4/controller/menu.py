from model.player import Player
from model.tournament import Tournament
from view.show_infos import ShowInfos
from view.ask_infos import AskInfos
from helpers.round import Round
from helpers.match import Match
from model.data_handler import DataHandler
from operator import attrgetter
from time import strptime


class Menu:
    play = True
    quit = True

    def __init__(self):
        self.actual_tournament = None

    def create_tournament(self):
        name = AskInfos.tournament_name()
        while not name.replace(" ", "").isalpha():
            print("Le nom du tournoi ne peut être composé que de lettres")
            name = AskInfos.tournament_name()

        place = AskInfos.tournament_place()
        while not place.replace(" ", "").isalpha():
            print("La ville ne peut être composé que de lettres")
            place = AskInfos.tournament_place()

        date_ok = False
        date = AskInfos.tournament_date()
        while not date_ok:
            try:
                strptime(date, '%d/%m/%Y')
                date_ok = True
            except ValueError:
                print("La date doit être au format JJ/MM/AAAA")
                date = AskInfos.tournament_date()

        player_number = AskInfos.tournament_player_number()
        while not player_number.isnumeric():
            print("Le nombre de joueur doit être un chiffre ou un ensemble"
                  "de chiffres")
            player_number = AskInfos.tournament_player_number()
        while not 2 <= int(player_number) <= 1000:
            print("Le nombre de joueur doit être compris entre 2 et 1000")
            player_number = AskInfos.tournament_player_number()

        timing_style = AskInfos.tournament_timing_style().capitalize()
        while timing_style != "Blitz" and timing_style != "Bullet" and \
                timing_style != "Coup rapide":
            print("Le contrôle du temps doit être Bullet, Blitz ou "
                  "Coup rapide")
            timing_style = AskInfos.tournament_timing_style().capitalize()

        description = AskInfos.tournament_description()

        round_number = AskInfos.tournament_round_number()
        while not 1 <= int(round_number) <= 20:
            print("Le nombre de round doit être compris entre 1 et 20")
            round_number = AskInfos.tournament_round_number()

        players_list = []
        x = 1
        tours = "rien"
        for i in range(int(player_number)):
            print("Joueur " + str(x))
            players_list.append(Menu.create_player())
            x += 1
        self.actual_tournament = Tournament(name, place, date,
                                            tours, players_list, timing_style,
                                            description, round_number)
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
        while not result.isnumeric():
            print("Vous devez choisir une réponse entre 1 et 3")
            result = AskInfos.match_result(match)
        while not 1 <= int(result) <= 3:
            print("Vous devez choisir une réponse entre 1 et 3")
            result = AskInfos.match_result(match)
        if result == "1":
            match.player1win()
        if result == "2":
            match.player2win()
        if result == "3":
            match.draw()

    def display(self):
        response = AskInfos.main()
        while not response.isnumeric():
            print("Vous devez choisir une réponse entre 1 et 7")
            response = AskInfos.main()
        while not 1 <= int(response) <= 7:
            print("Vous devez choisir une réponse entre 1 et 7")
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
        last_name = AskInfos.player_last_name()
        while not last_name.replace(" ", "").isalpha():
            print("Le nom de famille ne peut être composé que de lettres")
            last_name = AskInfos.player_last_name()

        first_name = AskInfos.player_first_name()
        while not first_name.replace(" ", "").isalpha():
            print("Le prénom ne peut être composé que de lettres")
            first_name = AskInfos.player_first_name()

        birthdate_ok = False
        birthdate = AskInfos.player_birthdate()
        while not birthdate_ok:
            try:
                strptime(birthdate, '%d/%m/%Y')
                birthdate_ok = True
            except ValueError:
                print("La date doit être au format JJ/MM/AAAA")
                birthdate = AskInfos.player_birthdate()

        sex = AskInfos.player_sex().upper()
        while sex != "H" and sex != "F":
            print("Le sexe doit être au format H/F")
            sex = AskInfos.player_sex()

        rating = AskInfos.player_rating()
        while not rating.isnumeric():
            print("Le classement doit être un nombre")
            rating = AskInfos.player_rating()

        new_player = Player(last_name, first_name, birthdate, sex, rating)
        if DataHandler.check_existance(new_player):
            print("Ce joueur existe déja dans la base de donnée, il n'est donc"
                  " pas rajouté\n")
            return new_player
        else:
            DataHandler.save(new_player)
            print("Le joueur {} a bien été créé\n".format(
                new_player.first_name))
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
                while not response.isnumeric():
                    print("Vous devez choisir une réponse entre 1 et 4")
                    response = ShowInfos.one_tournament(self.actual_tournament)
                while not 1 <= int(response) <= 4:
                    print("Vous devez choisir une réponse entre 1 et 4")
                    response = ShowInfos.one_tournament(self.actual_tournament)
                if response == "1":
                    ShowInfos.tournament_results(
                        self.actual_tournament.players)
                if response == "2":
                    ShowInfos.rounds(self.actual_tournament.rounds)
                if response == "3":
                    result = AskInfos.sorting_method()
                    while not result.isnumeric():
                        print("Vous devez choisir une réponse entre 1 et 2")
                        result = AskInfos.sorting_method()
                    while not 1 <= int(result) <= 2:
                        print("Vous devez choisir une réponse entre 1 et 2")
                        result = AskInfos.sorting_method()
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
