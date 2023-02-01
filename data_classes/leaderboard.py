from box_score import BoxScore


class Leaderboard:
    def __init__(self):
        self.bipocs = {}

    def populate_bipocs(self, box_scores: list[BoxScore]):
        for box_score in box_scores:
            bipoc = box_score.get_best()
            
            if bipoc not in self.bipocs:
                self.bipocs[bipoc] = 0
            
            self.bipocs[bipoc] += 1
