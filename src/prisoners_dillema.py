import argparse
import random


class RepeatedPlay:
    payoff_matrix = {("C", "C"): (3, 3), ("C", "D"): (1, 5),
                     ("D", "C"): (5, 1), ("D", "D"): (2, 2)}

    def __init__(self, trials=100, p=1.0, log=False):
        self.trials = trials
        self.p = p
        self.log = log

    def run(self, p1, p2):
        sums = [0, 0]
        trials = 0
        for i in range(self.trials):
            actions, results = self.play(p1, p2)
            if self.log:
                print(actions)

            # notify players of results
            p1.update(self.relative_play(actions, 'p1'))
            p2.update(self.relative_play(actions, 'p2'))

            # update totals
            sums[0] += results[0]
            sums[1] += results[1]

            # biased coin flip for continuing
            trials += 1
            if not self.should_continue():
                break

        if self.log:
            print("totals: ", str(sums))
            print("trials: ", trials)
        return sums

    def play(self, p1, p2):
        actions = (p1.action(), p2.action())
        results = self.payoff_matrix[actions]
        return actions, results

    def should_continue(self):
        return random.random() < self.p

    @staticmethod
    def relative_play(actions, player):
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
    elif name == "TF2T":
        return TitForTwoTat()
    elif name == "RAND" or name == "RANDOM":
        return RandomChoice()
    elif name == "PAV" or name == "PAVLOV":
        return Pavlov()
    elif name == "WSLS":
        return WSLS()
    elif name == "NEVER-FORGIVE" or name == "NF" or name == "NEVERFORGIVE" or name == "NEVER_FORGIVE":
        return NeverForgive()
    elif name == "CDCD":
        return CDCD()
    elif name == "DCDC":
        return DCDC()


# Always Cooperate Agent
class Agent:

    def __init__(self):
        # the previous play is a tuple: (M, Y)
        # where M is my previous move, and Y is the other player's previous move
        self.previous = None

    def action(self):
        return "C"

    def update(self, results):
        # results should be of the format: (M, Y) [see above]
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
            # return whatever the other played last
            return self.previous[1]


# Tit-for-Two-Tats Agent
class TitForTwoTat:

    def __init__(self):
        # Stores the last two turns, with previous[0] being the most recent turn
        self.previous = [None, None]

    def action(self):
        # Always Cooperate for the first two moves
        if self.previous[1] is None:
            return "C"
        elif self.previous[0][1] == "D" and self.previous[1][1] == "D":
            return "D"
        else:
            return "C"

    def update(self, results):
        self.previous[1] = self.previous[0]
        self.previous[0] = results


# Random-Choice Agent
class RandomChoice(Agent):

    def action(self):
        return random.choice(['C', 'D'])


# Pavlov Agent
class Pavlov(Agent):

    def action(self):
        if self.previous is not None and self.previous[0] != self.previous[1]:
            return "D"
        else:
            return "C"


class WSLS(Agent):

    def __init__(self):
        super().__init__()
        self.choice = "C"

    def action(self):
        if self.won_previous:
            return self.choice
        else:
            new_choice = self.change()
            return new_choice

    def change(self):
        if self.choice == "C":
            self.choice = "D"
        else:
            self.choice = "C"
        return self.choice

    @property
    def won_previous(self):
        if self.previous is None:
            return True
        return self.previous[1] == "C"


class NeverForgive(Agent):

    def __init__(self):
        super().__init__()
        self.crossed = False

    def action(self):
        if self.crossed:
            return "D"
        elif self.previous is not None and self.previous[1] == "D":
            self.crossed = True
            return "D"
        else:
            return "C"


class CDCD(Agent):

    def action(self):
        if self.previous is None:
            return "C"
        elif self.previous[0] == "C":
            return "D"
        else:
            return "C"


class DCDC(Agent):

    def action(self):
        if self.previous is None:
            return "D"
        elif self.previous[0] == "C":
            return "D"
        else:
            return "C"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p1', help='the agent type for player 1')
    parser.add_argument('p2', help='the agent type for player 2')
    parser.add_argument('trials', type=int, nargs='?', default=100, help='the number of repeat trials to run')
    parser.add_argument('--p', type=float, default=1.0, help='the probability of continuing to another round')
    args = parser.parse_args()

    player_1 = get_agent(args.p1)
    player_2 = get_agent(args.p2)
    game = RepeatedPlay(args.trials, args.p, True)
    game.run(player_1, player_2)
