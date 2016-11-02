import argparse
import random


class RepeatedPlay:
    payoff_matrix = {("C", "C"): (3, 3), ("C", "D"): (1, 5),
                     ("D", "C"): (5, 1), ("D", "D"): (2, 2)}

    def __init__(self, trials=100, p=1.0):
        self.trials = trials
        self.p = p

    def run(self, p1, p2):
        sums = [0, 0]
        for i in range(self.trials):
            actions, results = self.play(p1, p2)
            print(actions)

            # notify players of results
            p1.update(self.relative_play(actions, 'p1'))
            p2.update(self.relative_play(actions, 'p2'))

            # update totals
            sums[0] += results[0]
            sums[1] += results[1]

        print("totals: ", str(sums))
        return sums

    def play(self, p1, p2):
        actions = self.actions(p1.action(), p2.action())
        results = self.payoff_matrix[actions]
        return actions, results

    def relative_play(self, actions, player):
        if player == 'p1':
            return actions
        else:
            return actions[::-1]

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
    elif name == "TFT":
        return TitForTat()
    elif name == "RAND":
        return RandomChoice()


# Always Cooperate Agent
class Agent:

    def __init__(self):
        self.previous = None

    def action(self):
        return "C"

    def update(self, results):
        self.previous = results


# Always Defect Agent
class AlwaysDefect(Agent):

    def action(self):
        return "D"


# Tit-for-Tat Agent
class TitForTat(Agent):

    def action(self):
        if self.previous is None:
            return "C"
        else:
            return self.previous[1]  # return whatever the other played last


# Random-Choice Agent
class RandomChoice(Agent):

    def action(self):
        return random.choice(['C', 'D'])


parser = argparse.ArgumentParser()
parser.add_argument('p1', help='the agent type for player 1')
parser.add_argument('p2', help='the agent type for player 2')
parser.add_argument('trials', type=int, nargs='?', default=100, help='the number of repeat trials to run')
args = parser.parse_args()

p1 = get_agent(args.p1)
p2 = get_agent(args.p2)
game = RepeatedPlay(args.trials)
game.run(p1, p2)
