from constants import ASTEROID_SCORES

class Score:
    def __init__(self):
        self.score = 0
    
    def update_score(self, asteroid_radius):
        self.score += ASTEROID_SCORES[asteroid_radius]