
class RepeatedPlay:
    payoff_matrix = {("C", "C"): (3, 3), ("C", "D"): (1, 5),
                     ("D", "C"): (5, 1), ("D", "D"): (2, 2)}

    def __init__(self, trials=100, p=1.0):
        self.trials = trials
        self.p = p

    def run(self, p1, p2):
        sums = [0, 0]
        for i in range(self.trials):
            results = self.play(p1.action(), p2.action())

            # notify players of results
            p1.results(results)
            p2.results(results)

            # update totals
            sums[0] += results[0]
            sums[1] += results[1]

        print("totals: ", str(sums))

    def play(self, a1, a2):
        return self.payoff_matrix[self.actions(a1, a2)]

    @staticmethod
    def actions(a1, a2):
        a1 = a1.upper()
        a2 = a2.upper()
        return a1, a2


# ---Agents---
def get_agent(name):
    name = name.upper()
    if name == "AC":
        return Agent()
    elif name == "AD":
        return AlwaysDefect()


# Basic, always cooperate agent
class Agent:

    def __init__(self):
        self.previous = None

    def action(self):
        return "C"

    def results(self, results):
        self.previous = results


# Always Defect Agent
class AlwaysDefect(Agent):

    def action(self):
        return "D"
