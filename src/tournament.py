import argparse
from prisoners_dillema import *


class Tournament:
    def __init__(self, trials=100, p=1.0):
        self.game = RepeatedPlay(trials, p)

    def run(self):
        results = self.results_map()
        for a1 in AGENTS:
            for a2 in AGENTS:
                agent1 = get_agent(a1)
                agent2 = get_agent(a2)
                r = self.game.run(agent1, agent2)
                results[a1][a2] = r
        print(results)

    @staticmethod
    def results_map():
        results = {}
        for name in AGENTS:
            results[name] = {}
        return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('trials', type=int, nargs='?', default=100, help='the number of repeat trials to run')
    parser.add_argument('--p', type=float, default=1.0, help='the probability of continuing to another round')
    args = parser.parse_args()

    tournament = Tournament(args.trials, args.p)
    tournament.run()
