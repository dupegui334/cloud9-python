class Participant:
    def __init__(self):
        self.points = 0
        self.choice = ""


class GameRound:
    pass

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant()
        self.secondParticipant = Participant()