import math


class Abit:
    def __init__(self, id, dirs, exams):
        self.id = id
        self.dirs = dirs
        self.exams = exams
    
    def enter(self):
        return self.dirs.pop(0)

    def calc(self, combinations):
        max_scores = 0
        for comb in combinations:
            score = 0
            for exam in comb:
                if exam not in self.exams:
                    score = -math.inf
                    continue
                score += self.exams[exam]
                if score > max_scores:
                    max_scores = score
        return max_scores

    def __str__(self):
        return f"{self.id}: {self.dirs}, {self.exams}"
