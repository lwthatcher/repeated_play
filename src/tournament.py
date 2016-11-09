import argparse
import csv
from prisoners_dillema import *

class Tournament:
    OUTPUT_FILE = 'results.csv'

    def __init__(self, trials=100, p=1.0):
        self.game = RepeatedPlay(trials, p)

    def run(self):
        results = self.results_map()
        for a1 in self.AGENTS:
            for a2 in self.AGENTS:
                agent1 = get_agent(a1)
                agent2 = get_agent(a2)
                r = self.game.run(agent1, agent2)
                results[a1][a2] = r
        self.export(results)

    def export(self, results):
        with open(self.OUTPUT_FILE, 'a') as csv_file:
            fieldnames = self.AGENTS
            fieldnames.insert(0, 'name')
            print("fieldnames", fieldnames)
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            print('AGENTS', self.AGENTS)
            for name in self.AGENTS:
                writer.writerow(results[name])

    @property
    def AGENTS(self):
        return ["AC", "AD", "TFT", "TF2T", "RANDOM", "PAVLOV", "WSLS", "NF", "DCDC"]

    def results_map(self):
        results = {}
        for name in self.AGENTS:
            results[name] = {"name": name}
        return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('trials', type=int, nargs='?', default=100, help='the number of repeat trials to run')
    parser.add_argument('--p', type=float, default=1.0, help='the probability of continuing to another round')
    args = parser.parse_args()

    tournament = Tournament(args.trials, args.p)
    tournament.run()
