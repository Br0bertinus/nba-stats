class PlayerLine:
    def __init__(self, **kwargs):
        self.player = kwargs.get("player", None)
        self.minutes = kwargs.get("minutes", 0)
        self.fgm = kwargs.get("fgm", 0)
        self.fga = kwargs.get("fga", 0)
        self.pts = kwargs.get("pts", 0)
        self.ftm = kwargs.get("ftm", 0)
        self.fta = kwargs.get("fta", 0)
        self.threepm = kwargs.get("threepm", 0)
        self.threepa = kwargs.get("threepa", 0)
        self.drb = kwargs.get("drb", 0)
        self.orb = kwargs.get("orb", 0)
        self.ast = kwargs.get("ast", 0)
        self.stl = kwargs.get("stl", 0)
        self.blk = kwargs.get("blk", 0)
        self.pf = kwargs.get("pf", 0)
        self.tov = kwargs.get("tov", 0)

    def get_game_score(self):
        return self.pts + (0.4 * self.fgm) - (0.7 * self.fga) - 0.4*(self.fta - self.ftm) + (0.7 * self.orb) + (0.3 * self.drb) + self.stl + (0.7 * self.ast) + (0.7 * self.blk) - (0.4 * self.pf) - self.tov

        