from player_line import PlayerLine

class BoxScore:
    def __init__(self):
        self.lines = []

    def get_best(self):
        best_score = None
        player = None

        for line in self.lines:
            player_line = PlayerLine(line)
            game_score = player_line.get_game_score()
            if game_score > best_score:
                best_score = game_score
                player = player_line.player

        return player

