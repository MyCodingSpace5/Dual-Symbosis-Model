class TrainedAI:
    def __init__(self):
        self.playerBase = set()
        self.cheaterLobbies = set()
        self.cheatedPlayers = set()
        self.CheaterData = set()
        self.PlayerData = set()

class NaturalSelectionAI:
    def __init__(self):
        self.Data = set()
        self.Iterations = set()

class Player:
    def __init__(self):
        self.MatchData = set()
        self.Username = ""
        self.Password = ""

def CheckPlayerForCheats(player, selection):
    if player.MatchData == selection.Data:
        return True
    else:
        return False
