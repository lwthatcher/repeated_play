import unittest
from prisoners_dillema import TitForTat, TitForTwoTat, Pavlov, WSLS, NeverForgive


class MyTestCase(unittest.TestCase):

    # ===== Helper Methods =====
    @staticmethod
    def _run_single_round(agent, other_play):
        my_play = agent.action()
        plays = (my_play, other_play)
        agent.update(plays)
        return plays

    # expected should be a list of (M, Y) tuples
    def _played_expected(self, agent, expected):
        print("Agent Other")
        for r in expected:
            plays = self._run_single_round(agent, r[1])
            self.assertEqual(plays[0], r[0])
            self.assertEqual(plays[1], r[1])
            print(plays)
        print()

    # ===== TESTS ======
    def test_TitForTat(self):
        print("Tit-For-Tat Agent")
        tft = TitForTat()
        p1 = ['D', 'C', 'C', 'D', 'D']
        me = ['C', 'D', 'C', 'C', 'D']
        self._played_expected(tft, zip(me, p1))

    def test_tf2t(self):
        print("Tit-For-Two-Tats Agent")
        tf2t = TitForTwoTat()
        p1 = ['D', 'C', 'C', 'D', 'D', 'C', 'C', 'C']
        me = ['C', 'C', 'C', 'C', 'C', 'D', 'C', 'C']
        self._played_expected(tf2t, zip(me, p1))

    def test_pavlov(self):
        print("Pavlov Agent")
        pav = Pavlov()
        p1 = ['D', 'D', 'C', 'D', 'D', 'D']
        me = ['C', 'D', 'C', 'C', 'D', 'C']
        self._played_expected(pav, zip(me, p1))

    def test_WSLS(self):
        print("Win-Stay/Lose-Shift Agent")
        wsls = WSLS()
        p1 = ['D', 'D', 'C', 'C', 'D', 'D']
        me = ['C', 'D', 'C', 'C', 'C', 'D']
        self._played_expected(wsls, zip(me, p1))

    def test_NeverForgive(self):
        print("Never Forgive Agent")
        nf = NeverForgive()
        p1 = ['C', 'C', 'C', 'D', 'C', 'C', 'D', 'C']
        me = ['C', 'C', 'C', 'C', 'D', 'D', 'D', 'D']
        self._played_expected(nf, zip(me, p1))

if __name__ == '__main__':
    unittest.main()
