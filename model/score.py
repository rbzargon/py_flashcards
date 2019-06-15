

class Score:

    def __init__(self, maximum: int):
        super().__init__()
        self.score = 0
        self.maximum = maximum

    @property
    def score(self):
        return self.score

    @property
    def maximum(self):
        return self.maximum
