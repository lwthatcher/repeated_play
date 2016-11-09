import unittest
from prisoners_dillema import TitForTat


class MyTestCase(unittest.TestCase):

    @staticmethod
    def _run_single_round(agent, other_play):
        my_play = agent.action()
        plays = (my_play, other_play)
        agent.update(plays)
        return plays

    # expected should be a list of (M, Y) tuples
    def _played_expected(self, agent, expected):
        print("hello world")
        for r in expected:
            plays = self._run_single_round(agent, r[1])
            self.assertEqual(plays[0], r[0])
            self.assertEqual(plays[1], r[1])
            print(plays)

    def test_TitForTat(self):
        tft = TitForTat()
        expected = [('C','D'), ('D','C'), ('C','C'), ('C','D'), ('D','D')]
        self._played_expected(tft, expected)

if __name__ == '__main__':
    unittest.main()
