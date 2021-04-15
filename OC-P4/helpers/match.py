class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = ""

    def player1win(self):
        self.player1.score += 1
        self.result = "player 1 won"
        pass

    def player2win(self):
        self.player2.score += 1
        self.result = "player 2 won"
        pass

    def draw(self):
        self.player1.score += 0.5
        self.player2.score += 0.5
        self.result = "draw"
        pass

    def __repr__(self):
        return "{} contre {}".format(self.player1, self.player2)
